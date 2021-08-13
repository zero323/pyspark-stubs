# Stubs for pyspark (Python 3)
#

from typing import Callable, Optional, TypeVar

from pyspark.conf import SparkConf as SparkConf
from pyspark.context import SparkContext as SparkContext
from pyspark.rdd import RDD as RDD
from pyspark.files import SparkFiles as SparkFiles
from pyspark.storagelevel import StorageLevel as StorageLevel
from pyspark.accumulators import (
    Accumulator as Accumulator,
    AccumulatorParam as AccumulatorParam,
)
from pyspark.broadcast import Broadcast as Broadcast
from pyspark.serializers import (
    MarshalSerializer as MarshalSerializer,
    PickleSerializer as PickleSerializer,
)
from pyspark.status import *
from pyspark.profiler import Profiler as Profiler, BasicProfiler as BasicProfiler

# Compatiblity imports
from pyspark.sql import SQLContext as SQLContext, HiveContext as HiveContext, Row as Row

T = TypeVar("T")
F = TypeVar("F", bound=Callable)

def since(version: str) -> Callable[[T], T]: ...
def copy_func(
    f: F,
    name: Optional[str] = ...,
    sinceversion: Optional[str] = ...,
    doc: Optional[str] = ...,
) -> F: ...
def keyword_only(func: F) -> F: ...

# Names in __all__ with no definition:
#   SparkJobInfo
#   SparkStageInfo
#   StatusTracker
