from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import os, json
import asyncio
import logging
import Calculator
from General import * 

app = Flask(__name__)
api = Api(app)

logging.basicConfig(
    
    format="%(message)s level=%(levelname)-7s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)

@app.route('/calculate', methods=["POST"])
def exec_calculate():
    payload = request.json
    operate = Calculator.Calculator(payload)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    task = asyncio.ensure_future(operate.start())
    result = loop.run_until_complete(task)
    loop.close()
    result = json.loads(json.dumps(result,  default = obj_to_dict))
    return result, result['code']

    

if __name__ == '__main__':
     app.run(port='8080', host='0.0.0.0', debug=True)
