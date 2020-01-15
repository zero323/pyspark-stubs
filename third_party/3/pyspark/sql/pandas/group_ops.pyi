from pyspark import since as since
from pyspark.rdd import PythonEvalType as PythonEvalType
from pyspark.sql.column import Column as Column
from pyspark.sql.dataframe import DataFrame as DataFrame
from typing import Any

class PandasGroupedOpsMixin:
    def apply(self, udf: Any): ...
    def cogroup(self, other: Any): ...

class PandasCogroupedOps:
    sql_ctx: Any = ...
    def __init__(self, gd1: Any, gd2: Any) -> None: ...
    def apply(self, udf: Any): ...
