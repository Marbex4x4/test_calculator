import pika
import json

import logging

logging.basicConfig(
    
    format="%(message)s ",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)

class Listener():

    def __init__(self):

        logging.info("Connecting to rabbitmq server")

        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost', port='5672'))

        channel = connection.channel()

        channel.queue_declare(queue='queue_add')

        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue='queue_add', on_message_callback=self.on_request)

        logging.info("###Awaiting requests###")

        channel.start_consuming()


    def on_request(self, ch, method, props, body):
        list_nums = body.decode('utf-8')
        list_nums = list_nums[1:-1].split(',')
        logging.info("Handle request, add:{}".format(list_nums) )
        response = Operation.add(list_nums)

        ch.basic_publish(exchange='',
                        routing_key=props.reply_to,
                        properties=pika.BasicProperties(correlation_id = \
                                                            props.correlation_id),
                        body=str(response))
        ch.basic_ack(delivery_tag=method.delivery_tag)

class Operation():
    def add(list_nums):
        result = float(list_nums[0]) + float(list_nums[1])
        logging.info("Handle response, add result:{}".format(result) )
        return result

