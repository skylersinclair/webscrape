import pytest
from job_recorder import JobRecorder


def test_example():
    assert 4 == 4


def test_job_recorder():
    job_recorder = JobRecorder()
    assert job_recorder.pagination_limit == 10


'''
what do I want as a test?
given link, can I
(a) identify correct app type
(b) given app type, link, get correct text

so code structure should be
(1) get_job_type(link) --> app_type: str
(2) get_job_text(app_type

'''