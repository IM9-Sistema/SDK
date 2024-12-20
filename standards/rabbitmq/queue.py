from typing import Callable
import pika
import pika.channel
import pika.exceptions
from pydantic import BaseModel
from ..structures.generics import RabbitMQAddress, RabbitMQPool

class Queue:
    def __init__(self, host, port, queue, durable, stream=None, max_size=None, ttl=None):
        self.connection = None
        self.channel = None
        self.queue = None
        self.host = host
        self.port = port
        self.durable = durable
        self.queue_name = queue
        self.stream = stream
        self.max_size = max_size
        self.ttl = ttl
        self.connect()

    @property
    def queue_arguments(self) -> dict[str, str]:
        return {} | ({ 'x-queue-type': 'stream' } if self.stream else {}) | ({ 'x-max-length-bytes': self.max_size } if self.max_size else {}) | ({ 'x-max-age': self.ttl } if self.ttl else {})

    def connect(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(self.host, self.port))
        self.channel = self.connection.channel()
        self.channel.basic_qos(prefetch_count=1)
        self.queue = self.channel.queue_declare(queue=self.queue_name, durable=self.durable, arguments=self.queue_arguments)

    @classmethod
    def from_config(cls, config: RabbitMQAddress):
        return cls(host=config.host, port=config.port, queue=config.queue, durable=config.durable, stream=config.stream, max_size=config.max_size)


    def produce_message(self, message: BaseModel):
        try:
            self.channel.basic_publish(
                                    exchange='',
                                    routing_key=self.queue_name,
                                    body=message.model_dump_json(),
                                    properties=pika.BasicProperties(
                                        delivery_mode = pika.DeliveryMode.Persistent
                                        )
                                    )
        except pika.exceptions.StreamLostError:
            self.connect()
            return self.produce_message(message)

    def consume_messages(self):
        def wrapper(function: Callable[[pika.channel.Channel, pika.spec.Basic.Deliver, pika.spec.BasicProperties, bytes], None]) -> None:
            self.channel.basic_qos(prefetch_count=16)
            self.channel.basic_consume(queue=self.queue_name,
                                auto_ack=False,
                                on_message_callback=function)
            self.channel.start_consuming()
        return wrapper
