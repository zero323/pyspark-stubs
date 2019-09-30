# Stubs for pyspark.statcounter (Python 3.5)
#

from typing import Any, Dict, Iterable, Optional, Union

maximum: Any
minimum: Any
sqrt: Any

class StatCounter:
    n: int
    mu: float
    m2: float
    maxValue: float
    minValue: float
    def __init__(self, values: Optional[Iterable[float]] = ...) -> None: ...
    def merge(self, value: float) -> StatCounter: ...
    def mergeStats(self, other: 'StatCounter') -> StatCounter: ...
    def copy(self) -> StatCounter: ...
    def count(self) -> int: ...
    def mean(self) -> float: ...
    def sum(self) -> float: ...
    def min(self) -> float: ...
    def max(self) -> float: ...
    def variance(self) -> float: ...
    def sampleVariance(self) -> float: ...
    def stdev(self) -> float: ...
    def sampleStdev(self) -> float: ...
    def asDict(self, sample: bool = ...) -> Dict[str, Union[float, int]]: ...
