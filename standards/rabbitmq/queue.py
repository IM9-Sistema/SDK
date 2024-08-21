from typing import Callable
import pika
import pika.channel
from pydantic import BaseModel

class Queue:
	def __init__(self, host, port, queue):
		self.host = host
		self.port = port
		self.connection = pika.BlockingConnection(pika.ConnectionParameters(host, port))
		self.channel = self.connection.channel()
		self.channel.basic_qos(prefetch_count=1)
		self.queue_name = queue
		self.queue = self.channel.queue_declare(queue=queue)



	def produce_message(self, message: BaseModel):
		self.channel.basic_publish(
								exchange='',
								routing_key=self.queue_name,
								body=message.model_dump_json(),
								properties=pika.BasicProperties(
						 			delivery_mode = pika.DeliveryMode.Persistent
					 				)
								)

	def consume_messages(self):
		def wrapper(function: Callable[[pika.channel.Channel, pika.spec.Basic.Deliver, pika.spec.BasicProperties, bytes], None]) -> None:
			self.channel.basic_qos(prefetch_count=1)
			self.channel.basic_consume(queue=self.queue_name,
								auto_ack=False,
								on_message_callback=function)
			self.channel.start_consuming()
		return wrapper
