import logging
import configparser
from constants.constants import APPLICATIONCONFIG

config = configparser.RawConfigParser() 
config.read(APPLICATIONCONFIG)

logger = logging.getLogger(__name__)

logpath = config.get("log", "logpath")
encoding = config.get("log", "encoding")
loglevel = config.get("log", "loglevel")

logging.basicConfig(
                    #filename=str(logpath), 
                    encoding=str(encoding), 
                    level=getattr(logging, str(loglevel)), 
                    format="%(asctime)s - %(levelname)s - %(message)s")


#This method used to print ssh logs, it checks the length of log then print if length is greater then 0. 
def printLOG(out, err):
    logger.info("\n\n"+ str(out) + "\n\n")
    logger.error("\n\n"+ str(err)+ "\n\n")