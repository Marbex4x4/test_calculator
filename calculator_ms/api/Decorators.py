
import json
import pprint, traceback, functools

from Objects import *
from General import * 

def valid_input():
    def wrapper(func):
        @functools.wraps(func)
        async def wrapped(self):
            txt = clean_exp(self.expression)
            try: 
                print(eval(txt))
                eval(txt)
                return await func(self)
            except:
                return ObjectResponseHttp(HTTP_BAD_REQUEST_CODE,'')
        return wrapped
    return wrapper