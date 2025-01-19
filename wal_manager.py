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

    @staticmethod
    def _read_lines_pointers(filename: str):
        lines = [0]

        current_symbol_ptr = 0
        with open(filename, "r") as f:
            current_symbol = f.read(1)
            while current_symbol:
                if current_symbol == "\n":
                    lines.append(current_symbol_ptr)
                current_symbol_ptr += 1
                current_symbol = f.read(1)
        return lines

    @staticmethod
    def _readlines_reverse(lines_ptrs: list[int], filename: str):
        least_char_ptr = len(lines_ptrs) - 1
        with open(filename, "r") as f:
            next_char_ptr = least_char_ptr - 1
            while next_char_ptr >= 0:
                f.seek(lines_ptrs[next_char_ptr])
                line = f.read(lines_ptrs[least_char_ptr] - lines_ptrs[next_char_ptr])
                yield line
                least_char_ptr -= 1
                next_char_ptr -= 1
