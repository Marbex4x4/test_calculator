import os
import sys

from Objects import *
from General import * 
from Decorators import *
from Operations import * 

class Calculator:
    
    def __init__(self, expression):
        self.expression = expression["data"]

    @valid_input()
    async def start(self):            

        exercise = clean_exp(self.expression)
        exercise = self.get_mul_div(exercise)
        exercise = self.get_add_sub(exercise)        
        res = "{} = {}".format(self.expression, round(float(exercise)))
        return ObjectResponseHttp(HTTP_SUCCESS_CODE,res)

    def get_operation_result(self, simbol, n1, n2):
        operation = Operations()
        if simbol == "*":
            res = operation.get_multiply(n1, n2)
        elif simbol == "/":
            res = operation.get_divide(n1, n2)
        elif simbol == "+":
            res = operation.get_add(n1, n2)
        elif simbol == "-":
            res = operation.get_subtract(n1, n2)

        return str(res)

    def get_num_one(self, txt, pos):

        i = pos-1
        num1 = ""
        while i >= 0:
            try:
                if txt[i] not in ('+','-','*','/') or (i == 0 and txt[i]=='-'):
                    num1 = txt[i] + num1
                else:
                    break
                i -= 1
            except Exception as e:
                print(e)

        print("num1: {}".format(num1))
        return num1


    def get_num_two(self, txt, pos):

        i = pos+1
        num2 = ""
        while i < len(txt):
            try:
                if txt[i]not in ('+','-','*','/'):
                    num2 = num2 + txt[i]
                else:
                    break
                i += 1
            except Exception as e:
                print(e)
        
        print("num2: {}".format(num2))    
        return num2

    def solve_operation(self, txt, pos):

        num1 = self.get_num_one(txt, pos)
        num2 = self.get_num_two(txt, pos)
        result = self.get_operation_result(txt[pos], float(num1), float(num2))
        print(num1+txt[pos]+num2)
        newTxt = txt.replace(num1+txt[pos]+num2, result, 1)
        print("RESULT",result)
        return newTxt


    def get_mul_div(self, txt):

        for i, char in enumerate(txt):
            if char == "*" or char == "/":
                txt = self.solve_operation(txt, i)
                txt = self.get_mul_div(txt)
                break        

        return txt

    def get_add_sub(self, txt):

        for i, char in enumerate(txt):
            if (char == "+" or char == "-") and i != 0:     
                txt = self.solve_operation(txt, i)
                txt = self.get_add_sub(txt)
                break        

        return txt