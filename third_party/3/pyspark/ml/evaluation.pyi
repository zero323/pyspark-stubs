# Stubs for pyspark.ml.evaluation (Python 3.5)
#

import abc
from typing import Any, Dict, Optional, Type

from pyspark.ml.wrapper import JavaParams
from pyspark.ml.param import Param, Params
from pyspark.ml.param.shared import HasFeaturesCol, HasLabelCol, HasPredictionCol, HasRawPredictionCol, HasWeightCol
from pyspark.ml.util import JavaMLReadable, JavaMLWritable

ParamMap = Dict[Param, Any]

class Evaluator(Params):
    __metaclass__: Type[abc.ABCMeta]
    def evaluate(self, dataset, params: Optional[ParamMap] = ...) -> float: ...
    def isLargerBetter(self) -> bool: ...

class JavaEvaluator(JavaParams, Evaluator):
    __metaclass__: Type[abc.ABCMeta]
    def isLargerBetter(self) -> bool: ...

class BinaryClassificationEvaluator(JavaEvaluator, HasLabelCol, HasRawPredictionCol, HasWeightCol, JavaMLReadable[BinaryClassificationEvaluator], JavaMLWritable):
    metricName: Param
    numBins: Param
    def __init__(self, *, rawPredictionCol: str = ..., labelCol: str = ..., metricName: str = ..., weightCol: Optional[str] = ..., numBins: int = ...) -> None: ...
    def setMetricName(self, value: str) -> BinaryClassificationEvaluator: ...
    def getMetricName(self) -> str: ...
    def setParams(self, *, rawPredictionCol: str = ..., labelCol: str = ..., metricName: str = ..., weightCol: Optional[str] = ..., numBins: int = ...) -> BinaryClassificationEvaluator: ...
    def setNumBins(self, value: int) -> BinaryClassificationEvaluator: ...
    def getNumBins(self) -> int: ...

class RegressionEvaluator(JavaEvaluator, HasLabelCol, HasPredictionCol, HasWeightCol, JavaMLReadable[RegressionEvaluator], JavaMLWritable):
    metricName: Param
    throughOrigin: Param
    def __init__(self, *, predictionCol: str = ..., labelCol: str = ..., metricName: str = ..., weightCol: Optional[str] = ..., throughOrigin: bool = ...) -> None: ...
    def setMetricName(self, value: str) -> RegressionEvaluator: ...
    def getMetricName(self) -> str: ...
    def setParams(self, *, predictionCol: str = ..., labelCol: str = ..., metricName: str = ..., weightCol: Optional[str] = ..., throughOrigin: bool = ...) -> RegressionEvaluator: ...
    def setThroughOrigin(self, value: bool) -> RegressionEvaluator: ...
    def getThroughOrigin(self) -> bool: ... 

class MulticlassClassificationEvaluator(JavaEvaluator, HasLabelCol, HasPredictionCol, HasWeightCol, JavaMLReadable[MulticlassClassificationEvaluator], JavaMLWritable):
    metricName: Param
    metricLabel: Param
    beta: Param
    def __init__(self, *, predictionCol: str = ..., labelCol: str = ..., metricName: str = ..., weightCol: Optional[str] = ..., metricLabel: float = ..., beta: float = ...) -> None: ...
    def setMetricName(self, value: str) -> MulticlassClassificationEvaluator: ...
    def getMetricName(self) -> str: ...
    def setMetricLabel(self, value: float) -> MulticlassClassificationEvaluator: ...
    def getMetricLabel(self) -> float: ...
    def setBeta(self, value: float) -> MulticlassClassificationEvaluator: ...
    def getBeta(self) -> float: ...
    def setParams(self, *, predictionCol: str = ..., labelCol: str = ..., metricName: str = ..., weightCol: Optional[str] = ..., metricLabel: float = ..., beta: float = ...) -> MulticlassClassificationEvaluator: ...

class MultilabelClassificationEvaluator(JavaEvaluator, HasLabelCol, HasPredictionCol, JavaMLReadable[MultilabelClassificationEvaluator], JavaMLWritable):
    metricName: Param
    metricLabel: Param
    def __init__(self, *, predictionCol: str = ..., labelCol: str = ..., metricName: str = ..., metricLabel: float = ...) -> None: ...
    def setMetricName(self, value: str) -> MultilabelClassificationEvaluator: ...
    def getMetricName(self) -> str: ...
    def setMetricLabel(self, value: float) -> MultilabelClassificationEvaluator: ...
    def getMetricLabel(self) -> float: ...
    def setParams(self, *, predictionCol: str = ..., labelCol: str = ..., metricName: str = ..., metricLabel: float = ...) -> MultilabelClassificationEvaluator: ...

class ClusteringEvaluator(JavaEvaluator, HasPredictionCol, HasFeaturesCol, JavaMLReadable[ClusteringEvaluator], JavaMLWritable):
    metricName: Param
    distanceMeasure: Param
    def __init__(self, *, predictionCol: str = ..., featuresCol: str = ..., metricName: str = ..., distanceMeasure: str = ...) -> None: ...
    def setMetricName(self, value: str) -> ClusteringEvaluator: ...
    def getMetricName(self) -> str: ...
    def setParams(self, *, predictionCol: str = ..., featuresCol: str = ..., metricName: str = ..., distanceMeasure: str = ...) -> MulticlassClassificationEvaluator: ...
    def setDistanceMeasure(self, value: str) -> MulticlassClassificationEvaluator: ...
    def getDistanceMeasure(self) -> str: ...

class RankingEvaluator(JavaEvaluator, HasLabelCol, HasPredictionCol, JavaMLReadable[RankingEvaluator], JavaMLWritable):
    metricName: Param
    k: Param
    def __init__(self, *, predictionCol: str = ..., labelCol: str = ..., metricName: str = ..., k: int = ...) -> None: ...
    def setMetricName(self, value: str) -> RankingEvaluator: ...
    def getMetricName(self) -> str: ...
    def setK(self, value: int) -> RankingEvaluator: ...
    def getK(self) -> int: ...
    def setParams(self, *, predictionCol: str = ..., labelCol: str = ..., metricName: str = ..., k: int = ...) -> RankingEvaluator: ...
