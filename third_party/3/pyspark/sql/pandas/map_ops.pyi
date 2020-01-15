from pyspark import since as since
from pyspark.rdd import PythonEvalType as PythonEvalType
from typing import Any

class PandasMapOpsMixin:
    def mapInPandas(self, udf: Any): ...
