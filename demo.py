from USA_visa.logger import logging
from USA_visa.exception import USvisaException
import sys

logging.info("Welcome to the custom log")

try:
    a = 2/0
except Exception as e:
    raise USvisaException(e, sys)