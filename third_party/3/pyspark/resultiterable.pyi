# Stubs for pyspark.resultiterable (Python 3.5)
#

from typing import Any, Generic, Iterable, Iterator, TypeVar
import collections

T = TypeVar('T')

class ResultIterable(collections.Iterable, Generic[T]):
    data: Iterable[T]
    index: int
    maxindex: int
    def __init__(self, data: Iterable[T]) -> None: ...
    def __iter__(self) -> Iterator[T]: ...
    def __len__(self) -> int: ...
