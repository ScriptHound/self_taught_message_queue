from typing import Any

from pydantic import BaseModel


class CreateTopicResponse(BaseModel):
    name: str


class DeleteTopicResponse(BaseModel):
    name: str


class PublishMessageResponse(BaseModel):
    ...


class ReadMessageResponse(BaseModel):
    message: dict[str, Any]
