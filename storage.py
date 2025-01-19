from queue import Queue
from typing import Any

from schemas.schemas import Storage, Topic


class TopicsHandler:
    def __init__(self):
        self.storage = Storage()

    def create_topic(self, name: str) -> Topic:
        if self.storage.topics is None:
            self.storage.topics = {}
        topic = Topic(name=name, storage=Queue())
        self.storage.topics[name] = topic
        return topic

    def delete_topic(self, name: str):
        if self.storage.topics is None:
            self.storage.topics = {}
        del self.storage.topics[name]

    def publish_messsage(self, data: dict[str, Any], topic_name: str):
        topic = self.storage.topics[topic_name]
        topic.storage.put(data)

    def read_message(self, topic_name: str) -> dict[str, Any] | None:
        topic = self.storage.topics[topic_name]
        if topic.storage.qsize() == 0:
            return None
        return topic.storage.get()


storage = TopicsHandler()


def get_topics_handler():
    return storage
