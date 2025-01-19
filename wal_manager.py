import os
import uuid
from datetime import datetime
from typing import Any

from pydantic import BaseModel


class WalEntry(BaseModel):
    topic_name: str
    update: str
    created_at: datetime


class WriteAheadLogManager:
    def __init__(self):
        creation_datetime = datetime.now()
        file_uuid = str(uuid.uuid4())
        filename = f"{creation_datetime.isoformat()}_{file_uuid}.wal"
        self.filename = filename
        self.file = open(f'wal/{filename}', "a+")

    def write(self, topic_name: str, update: dict[str, Any]):
        created_at = datetime.now().isoformat()
        entry = WalEntry(topic_name=topic_name, update=update, created_at=created_at)
        self.file.write(entry.model_dump_json() + "\n")

    def read(self):
        ...

    def _readlines_reverse(self, filename: str):
        EOF = self.file.seek(0, 2)



manager = WriteAheadLogManager()

