import io
from typing import Generator, List, Union


def file_filter(
    filename: Union[str, io.IOBase], search_list: List[str], stop_list: List[str]
) -> Generator[str, None, None]:
    search_set = {word.lower() for word in search_list}
    stop_set = {word.lower() for word in stop_list}
    if isinstance(filename, io.IOBase):
        context = filename
    else:
        context = open(filename, "r", encoding="utf-8")
    with context as f:
        for line in f:
            words = set(line.lower().split())
            if words & stop_set:
                continue
            if words & search_set:
                yield line
