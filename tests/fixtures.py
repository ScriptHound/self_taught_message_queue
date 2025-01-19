import os

import pytest


@pytest.fixture
def create_multiline_file():
    filename = "test.txt"
    random_string = "\n".join([f"line {i}" for i in range(10)])
    with open(filename, "w") as f:
        f.write(random_string)
    yield filename
    os.remove(filename)
