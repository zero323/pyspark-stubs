# Stubs for pyspark.ml.base (Python 3)
#

from typing import Optional

from pyspark.ml._typing import P
from pyspark.ml.util import *
from pyspark.ml.wrapper import JavaEstimator, JavaParams, JavaModel
from pyspark.ml.param.shared import *
from pyspark.sql.dataframe import DataFrame

class HasMinSupport(Params):
    minSupport: Param[float]
    def setMinSupport(self: P, value: float) -> P: ...
    def getMinSupport(self) -> float: ...

class HasNumPartitions(Params):
    numPartitions: Param[int]
    def setNumPartitions(self: P, value: int) -> P: ...
    def getNumPartitions(self) -> int: ...

class HasMinConfidence(Params):
    minConfidence: Param[float]
    def setMinConfidence(self: P, value: float) -> P: ...
    def getMinConfidence(self) -> float: ...

class HasItemsCol(Params):
    itemsCol: Param[str]
    def setItemsCol(self: P, value: str) -> P: ...
    def getItemsCol(self) -> str: ...

class FPGrowthModel(JavaModel, JavaMLWritable, JavaMLReadable[FPGrowthModel]):
    @property
    def freqItemsets(self) -> DataFrame: ...
    @property
    def associationRules(self) -> DataFrame: ...

class FPGrowth(
    JavaEstimator[FPGrowthModel],
    HasItemsCol,
    HasPredictionCol,
    HasMinSupport,
    HasNumPartitions,
    HasMinConfidence,
    JavaMLWritable,
    JavaMLReadable[FPGrowth],
):
    def __init__(
        self,
        *,
        minSupport: float = ...,
        minConfidence: float = ...,
        itemsCol: str = ...,
        predictionCol: str = ...,
        numPartitions: Optional[int] = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        minSupport: float = ...,
        minConfidence: float = ...,
        itemsCol: str = ...,
        predictionCol: str = ...,
        numPartitions: Optional[int] = ...
    ) -> FPGrowth: ...

class PrefixSpan(JavaParams):
    minSupport: Param[float]
    maxPatternLength: Param[int]
    maxLocalProjDBSize: Param[int]
    sequenceCol: Param[str]
    def __init__(
        self,
        *,
        minSupport: float = ...,
        maxPatternLength: int = ...,
        maxLocalProjDBSize: int = ...,
        sequenceCol: str = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        minSupport: float = ...,
        maxPatternLength: int = ...,
        maxLocalProjDBSize: int = ...,
        sequenceCol: str = ...
    ) -> PrefixSpan: ...
    def findFrequentSequentialPatterns(self, dataset: DataFrame) -> DataFrame: ...
