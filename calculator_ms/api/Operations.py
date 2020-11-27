import os
import sys
import MQClient

class Operations:

    def get_multiply(self, n1, n2):
    
        multiply = MQClient.MQClient()
        print(" [x] Requesting Multiply(n1*n2)")
        kwargs = {'n1':n1, 'n2':n2}
        args = [n1, n2]
        response = multiply.call(*args)
        print(" [.] Got %r" % response)
        return response

    def get_divide(self, n1, n2):
        return n1 / n2

    def get_add(self, n1, n2):
        return n1 + n2

    def get_subtract(self, n1, n2):
        return n1 - n2