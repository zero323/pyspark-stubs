# Stubs for pyspark.ml.fpm (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from pyspark.ml.util import *
from pyspark.ml.wrapper import JavaEstimator, JavaParams, JavaModel
from pyspark.ml.param.shared import *

class HasSupport(Params):
    minSupport = ...  # type: Any
    def setMinSupport(self, value): ...
    def getMinSupport(self): ...

class HasConfidence(Params):
    minConfidence = ...  # type: Any
    def setMinConfidence(self, value): ...
    def getMinConfidence(self): ...

class HasItemsCol(Params):
    itemsCol = ...  # type: Any
    def setItemsCol(self, value): ...
    def getItemsCol(self): ...

class FPGrowthModel(JavaModel, JavaMLWritable, JavaMLReadable):
    @property
    def freqItemsets(self): ...
    @property
    def associationRules(self): ...

class FPGrowth(JavaEstimator, HasItemsCol, HasPredictionCol, HasSupport, HasConfidence, JavaMLWritable, JavaMLReadable):
    def __init__(self, minSupport: float = ..., minConfidence: float = ..., itemsCol: str = ..., predictionCol: str = ..., numPartitions: Optional[Any] = ...) -> None: ...
    def setParams(self, minSupport: float = ..., minConfidence: float = ..., itemsCol: str = ..., predictionCol: str = ..., numPartitions: Optional[Any] = ...): ...

class PrefixSpan(JavaParams):
    minSupport: Any = ...
    maxPatternLength: Any = ...
    maxLocalProjDBSize: Any = ...
    sequenceCol: Any = ...
    def __init__(self, minSupport: float = ..., maxPatternLength: int = ..., maxLocalProjDBSize: int = ..., sequenceCol: str = ...) -> None: ...
    def setParams(self, minSupport: float = ..., maxPatternLength: int = ..., maxLocalProjDBSize: int = ..., sequenceCol: str = ...): ...
    def findFrequentSequentialPatterns(self, dataset: Any): ...
