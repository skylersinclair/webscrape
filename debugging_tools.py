"""
Misc functions to help debug/understand frontend status.
"""
import logging


def print_all_iframes(driver) -> None:
    """Prints all iframes in a current driver page source.
    Should not be in a class, should be a general tool"""
    logging.info("all iframes: ")
    iframes = driver.find_elements_by_xpath("//iframe")
    logging.info(f"found {len(iframes)} frames")
    for frame in iframes:
        logging.info(frame)
        logging.info(frame.get_attribute('id'))
        logging.info(frame.get_attribute('title'))


def print_all_ids_avail(driver) -> None:
    """
    Prints all named ids of elements in the self.driver page source.
    Should not be in a class, is a general tool (or at least, static)

    Returns:

    """
    logging.info("all ids:")
    ids = driver.find_elements_by_xpath('//*[@id]')
    for ii in ids:
        # if 'apply' in ii.get_attribute('id'):
        logging.info(ii.get_attribute('id'))


def print_all_aria_labels_avail(driver) -> None:
    """
    Prints all named ids of elements in the self.driver page source.
    Should not be in a class, is a general tool (or at least, static)

    Returns:

    """
    logging.info("all ids:")
    ids = driver.find_elements_by_xpath('//*[@aria-label]')
    for ii in ids:
        # if 'apply' in ii.get_attribute('id'):
        logging.info(ii.get_attribute('aria-label'))
