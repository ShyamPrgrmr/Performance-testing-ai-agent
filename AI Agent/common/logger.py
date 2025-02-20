import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='./output/application.log', 
                    encoding='utf-8', 
                    level=logging.DEBUG, 
                    format="%(asctime)s - %(levelname)s - %(message)s")
