from pyspark.sql.types import *
from pyspark import since as since
from pyspark.sql.pandas.serializers import ArrowCollectSerializer as ArrowCollectSerializer
from pyspark.sql.types import IntegralType as IntegralType
from pyspark.traceback_utils import SCCallSiteSync as SCCallSiteSync
from typing import Any, Optional

basestring = str
unicode = str
xrange = range

class PandasConversionMixin:
    def toPandas(self): ...

class SparkConversionMixin:
    def createDataFrame(self, data: Any, schema: Optional[Any] = ..., samplingRatio: Optional[Any] = ..., verifySchema: bool = ...): ...
