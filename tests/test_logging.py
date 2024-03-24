import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler("logfile.log")

    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)

    logger.setLevel(logging.INFO)
    logger.info("Information statement")
    logger.warning("Warning Statement")
    logger.error("ERROR")
    logger.critical("critical issue")
