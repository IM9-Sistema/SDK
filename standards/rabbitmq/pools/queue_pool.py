from random import choice

from pydantic import BaseModel

from ..queue import Queue, RabbitMQPool

class QueuePool(Queue):
    def __init__(self, host, port, queue, max_size: int, min_size: int):
        super().__init__(host, port, queue)
        self.max_size = max_size
        self.min_size = min_size
        self.connections: list[Queue] = []

    def connect(self):
        for i in range(self.min_size):
            self.connections.append(Queue(self.host, self.port, self.queue))

    @classmethod
    def from_config(cls, config: RabbitMQPool):
        return cls(config.host, config.port, config.queue, max_size=config.max_size, min_size=config.min_size)

    def select_conn(self):
        return choice(self.connections)


    def consume_messages(self):
        selected_conn = self.select_conn()
        return selected_conn.consume_messages()

    def produce_message(self, message: BaseModel):
        selected_conn = self.select_conn()
        selected_conn.produce_message(message)

