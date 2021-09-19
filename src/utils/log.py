import calendar
import logging
import platform
from datetime import datetime


from src.consts.consts import Consts
from colorlog import ColoredFormatter

os_name = platform.system()  # Mac: Darwin | Win: Windows
LOG_LEVEL = logging.INFO # 20 -info
LOG_FORMAT = "\t%(asctime)-6s %(log_color)s%(levelname)7s | %(log_color)s%(message)s"
# LOG_FORMAT = "\t%(asctime)-6s.%(msecs)03d %(log_color)s%(levelname)7s | %(log_color)s%(message)s"
LOG_FORMAT_WIN = "\t%(asctime)-6s %(levelname)7s | %(message)s"
logging.root.setLevel(LOG_LEVEL)
logger = logging.getLogger('pythonConfig')
logger.propagate = False

def create_new_handler_logger(log_level):
    if not logger.handlers:
        stream = logging.StreamHandler()  # pylint: disable=invalid-name
        stream.setLevel(log_level)
        if os_name == "Windows":
            formatter = logging.Formatter(LOG_FORMAT_WIN, "%H:%M:%S")
            stream.setFormatter(formatter)
        else:
            stream.setFormatter(ColoredFormatter(LOG_FORMAT, "%H:%M:%S"))  # "%Y-%m-%d %H:%M:%S"
        logger.setLevel(log_level)
        logger.addHandler(stream)


def create_logfile(iscreate):
    if(iscreate):
        logfile_name = Consts.LOG_FILE % (datetime.now().strftime("logfile_%Y%m%d_%H_%M_%S"))
    else:
        logfile_name = Consts.LOG_FILE % (datetime.now().strftime("logfile"))
    fh = logging.FileHandler(logfile_name)
    fh.setLevel(LOG_LEVEL)
    #logfile_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logfile_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(logfile_format)
    logger.addHandler(fh)

create_new_handler_logger(LOG_LEVEL)
create_logfile(False)

logger.info("---> Start log")
logger.info("QCKhanh----Welcome to automation test for mobile")