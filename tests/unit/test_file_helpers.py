from wal_manager import WriteAheadLogManager
from tests.fixtures import create_multiline_file


def test_read_lines_pointers(create_multiline_file):
    file = create_multiline_file
    lines = WriteAheadLogManager._read_lines_pointers(file)
    assert len(lines) == 10


def test_read_lines_reverse(create_multiline_file):
    file = create_multiline_file
    lines = WriteAheadLogManager._read_lines_pointers(file)
    reversed_lines = [line for line in WriteAheadLogManager._readlines_reverse(lines, file)]
    assert reversed_lines == ["line 9", "line 8", "line 7", "line 6", "line 5", "line 4", "line 3", "line 2", "line 1", "line 0"]
