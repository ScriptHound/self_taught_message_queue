from queue import Queue

from pydantic import BaseModel


class Topic(BaseModel):
    model_config = dict(arbitrary_types_allowed=True)
    name: str
    storage: Queue


class Storage(BaseModel):
    topics: dict[str, Topic] | None = None
