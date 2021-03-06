"""
Actually run the queries here yay
"""
from sql_queries import create_jobs_table, create_queries_table
from search_recorder import SearchRecorder
from job_recorder import JobRecorder
from typing import List
import sqlite3
from constants import DB_PATH
import logging
import argparse


class Orchestration:

    def __init__(self):
        self.search_recorder = SearchRecorder()
        self.job_recorder = JobRecorder()
        self.conn = self.create_db_connection()

    def run_single_query(self, query_text: str, location: str):
        # First, make the query and write the query info to the DB
        query_info = self.search_recorder.make_query(query_text=query_text, location=location)
        query_id = self.search_recorder.write_query_to_db(conn=self.conn, query_info=query_info)

        # Next, write the query job results to the DB
        self.job_recorder.write_all_jobs_to_db(query_url=query_info.result_url, conn=self.conn, query_id=query_id)

    def run_all_queries(self, query_text_list: List[str], location_list: List[str]):
        for query_text in query_text_list:
            for location in location_list:
                self.run_single_query(query_text, location)

    @staticmethod
    def create_db_connection(db_file: str = DB_PATH) -> sqlite3.Connection:
        """ create a database connection to a SQLite database """
        try:
            conn = sqlite3.connect(db_file)
            logging.info("Connected to {} using sqlite3 version {}".format(db_file, sqlite3.version))
            return conn
        except sqlite3.Error:
            logging.error("Unable to connect to the database.")
            raise

    @staticmethod
    def execute_sql(conn, sql_query):
        try:
            c = conn.cursor()
            c.execute(sql_query)
        except sqlite3.Error as e:
            print(e)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--log', help='level of logging to display (error, warn, info, debug)')
    args = parser.parse_args()
    if args.log:
        log_level = getattr(logging, args.log.upper())
        logging.basicConfig(level=log_level)
    else:
        logging.basicConfig(level=logging.INFO)

    orchestration = Orchestration()
    logging.info("Creating Tables")
    orchestration.execute_sql(orchestration.conn, create_jobs_table)
    orchestration.execute_sql(orchestration.conn, create_queries_table)
    logging.info("Running Query")
    for location in ["Austin, TX", "New York, NY"]:
        for job in ["Product Manager", "Teacher"]:
            orchestration.run_single_query(job, location)
