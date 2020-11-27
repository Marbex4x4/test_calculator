import os
import sys
import MQClient

from Logging import * 

class Operations:

    def get_multiply(self, n1, n2):
        logging.info("Operation: {} * {}".format(n1, n2))
        multiply = MQClient.MQClient('queue_multiply')
        args = [n1, n2]
        response = multiply.call(*args)
        logging.info("Operation result: {} * {} = {}".format(n1, n2, response))
        return response

    def get_divide(self, n1, n2):
        logging.info("Operation: {} * {}".format(n1, n2))
        multiply = MQClient.MQClient('queue_divide')
        args = [n1, n2]
        response = multiply.call(*args)
        logging.info("Operation result: {} / {} = {}".format(n1, n2, response))
        return response

    def get_add(self, n1, n2):
        return n1 + n2

    def get_subtract(self, n1, n2):
        return n1 - n2