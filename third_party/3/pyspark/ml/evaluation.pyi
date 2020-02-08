# Stubs for pyspark.ml.evaluation (Python 3.5)
#

import abc
from typing import Any, Dict, Optional, Type
from pyspark.ml._typing import (
    ParamMap,
    BinaryClassificationEvaluatorMetricType,
    ClusteringEvaluatorMetricType,
    MulticlassClassificationEvaluatorMetricType,
    MultilabelClassificationEvaluatorMetricType,
    RankingEvaluatorMetricType,
    RegressionEvaluatorMetricType,
)

from pyspark.ml.wrapper import JavaParams
from pyspark.ml.param import Param, Params
from pyspark.ml.param.shared import (
    HasFeaturesCol,
    HasLabelCol,
    HasPredictionCol,
    HasProbabilityCol,
    HasRawPredictionCol,
    HasWeightCol,
)
from pyspark.ml.util import JavaMLReadable, JavaMLWritable

class Evaluator(Params):
    __metaclass__: Type[abc.ABCMeta]
    def evaluate(self, dataset, params: Optional[ParamMap] = ...) -> float: ...
    def isLargerBetter(self) -> bool: ...

class JavaEvaluator(JavaParams, Evaluator):
    __metaclass__: Type[abc.ABCMeta]
    def isLargerBetter(self) -> bool: ...

class BinaryClassificationEvaluator(
    JavaEvaluator,
    HasLabelCol,
    HasRawPredictionCol,
    HasWeightCol,
    JavaMLReadable[BinaryClassificationEvaluator],
    JavaMLWritable,
):
    metricName: Param[BinaryClassificationEvaluatorMetricType]
    numBins: Param[int]
    def __init__(
        self,
        *,
        rawPredictionCol: str = ...,
        labelCol: str = ...,
        metricName: BinaryClassificationEvaluatorMetricType = ...,
        weightCol: Optional[str] = ...,
        numBins: int = ...
    ) -> None: ...
    def setMetricName(
        self, value: BinaryClassificationEvaluatorMetricType
    ) -> BinaryClassificationEvaluator: ...
    def getMetricName(self) -> BinaryClassificationEvaluatorMetricType: ...
    def setNumBins(self, value: int) -> BinaryClassificationEvaluator: ...
    def getNumBins(self) -> int: ...
    def setLabelCol(self, value: str) -> BinaryClassificationEvaluator: ...
    def setRawPredictionCol(self, value: str) -> BinaryClassificationEvaluator: ...
    def setWeightCol(self, value: str) -> BinaryClassificationEvaluator: ...

def setParams(
    self,
    *,
    rawPredictionCol: str = ...,
    labelCol: str = ...,
    metricName: BinaryClassificationEvaluatorMetricType = ...,
    weightCol: Optional[str] = ...,
    numBins: int = ...
) -> BinaryClassificationEvaluator: ...

class RegressionEvaluator(
    JavaEvaluator,
    HasLabelCol,
    HasPredictionCol,
    HasWeightCol,
    JavaMLReadable[RegressionEvaluator],
    JavaMLWritable,
):
    metricName: Param[RegressionEvaluatorMetricType]
    throughOrigin: Param[bool]
    def __init__(
        self,
        *,
        predictionCol: str = ...,
        labelCol: str = ...,
        metricName: RegressionEvaluatorMetricType = ...,
        weightCol: Optional[str] = ...,
        throughOrigin: bool = ...
    ) -> None: ...
    def setMetricName(
        self, value: RegressionEvaluatorMetricType
    ) -> RegressionEvaluator: ...
    def getMetricName(self) -> RegressionEvaluatorMetricType: ...
    def setThroughOrigin(self, value: bool) -> RegressionEvaluator: ...
    def getThroughOrigin(self) -> bool: ...
    def setLabelCol(self, value: str) -> RegressionEvaluator: ...
    def setPredictionCol(self, value: str) -> RegressionEvaluator: ...
    def setWeightCol(self, value: str) -> RegressionEvaluator: ...
    def setParams(
        self,
        *,
        predictionCol: str = ...,
        labelCol: str = ...,
        metricName: RegressionEvaluatorMetricType = ...,
        weightCol: Optional[str] = ...,
        throughOrigin: bool = ...
    ) -> RegressionEvaluator: ...

class MulticlassClassificationEvaluator(
    JavaEvaluator,
    HasLabelCol,
    HasPredictionCol,
    HasWeightCol,
    HasProbabilityCol,
    JavaMLReadable[MulticlassClassificationEvaluator],
    JavaMLWritable,
):
    metricName: Param[MulticlassClassificationEvaluatorMetricType]
    metricLabel: Param[float]
    beta: Param[float]
    eps: Param[float]
    def __init__(
        self,
        *,
        predictionCol: str = ...,
        labelCol: str = ...,
        metricName: MulticlassClassificationEvaluatorMetricType = ...,
        weightCol: Optional[str] = ...,
        metricLabel: float = ...,
        beta: float = ...,
        probabilityCol: str = ...,
        eps: float = ...
    ) -> None: ...
    def setMetricName(
        self, value: MulticlassClassificationEvaluatorMetricType
    ) -> MulticlassClassificationEvaluator: ...
    def getMetricName(self) -> MulticlassClassificationEvaluatorMetricType: ...
    def setMetricLabel(self, value: float) -> MulticlassClassificationEvaluator: ...
    def getMetricLabel(self) -> float: ...
    def setBeta(self, value: float) -> MulticlassClassificationEvaluator: ...
    def getBeta(self) -> float: ...
    def setEps(self, value: float) -> MulticlassClassificationEvaluator: ...
    def getEps(self) -> float: ...
    def setLabelCol(self, value: str) -> MulticlassClassificationEvaluator: ...
    def setPredictionCol(self, value: str) -> MulticlassClassificationEvaluator: ...
    def setProbabilityCol(self, value: str) -> MulticlassClassificationEvaluator: ...
    def setWeightCol(self, value: str) -> MulticlassClassificationEvaluator: ...
    def setParams(
        self,
        *,
        predictionCol: str = ...,
        labelCol: str = ...,
        metricName: MulticlassClassificationEvaluatorMetricType = ...,
        weightCol: Optional[str] = ...,
        metricLabel: float = ...,
        beta: float = ...,
        probabilityCol: str = ...,
        eps: float = ...
    ) -> MulticlassClassificationEvaluator: ...

class MultilabelClassificationEvaluator(
    JavaEvaluator,
    HasLabelCol,
    HasPredictionCol,
    JavaMLReadable[MultilabelClassificationEvaluator],
    JavaMLWritable,
):
    metricName: Param[MultilabelClassificationEvaluatorMetricType]
    metricLabel: Param[float]
    def __init__(
        self,
        *,
        predictionCol: str = ...,
        labelCol: str = ...,
        metricName: MultilabelClassificationEvaluatorMetricType = ...,
        metricLabel: float = ...
    ) -> None: ...
    def setMetricName(
        self, value: MultilabelClassificationEvaluatorMetricType
    ) -> MultilabelClassificationEvaluator: ...
    def getMetricName(self) -> MultilabelClassificationEvaluatorMetricType: ...
    def setMetricLabel(self, value: float) -> MultilabelClassificationEvaluator: ...
    def getMetricLabel(self) -> float: ...
    def setLabelCol(self, value: str) -> MultilabelClassificationEvaluator: ...
    def setPredictionCol(self, value: str) -> MultilabelClassificationEvaluator: ...
    def setParams(
        self,
        *,
        predictionCol: str = ...,
        labelCol: str = ...,
        metricName: MultilabelClassificationEvaluatorMetricType = ...,
        metricLabel: float = ...
    ) -> MultilabelClassificationEvaluator: ...

class ClusteringEvaluator(
    JavaEvaluator,
    HasPredictionCol,
    HasFeaturesCol,
    JavaMLReadable[ClusteringEvaluator],
    JavaMLWritable,
):
    metricName: Param[ClusteringEvaluatorMetricType]
    distanceMeasure: Param[str]
    def __init__(
        self,
        *,
        predictionCol: str = ...,
        featuresCol: str = ...,
        metricName: ClusteringEvaluatorMetricType = ...,
        distanceMeasure: str = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        predictionCol: str = ...,
        featuresCol: str = ...,
        metricName: ClusteringEvaluatorMetricType = ...,
        distanceMeasure: str = ...
    ) -> ClusteringEvaluator: ...
    def setMetricName(
        self, value: ClusteringEvaluatorMetricType
    ) -> ClusteringEvaluator: ...
    def getMetricName(self) -> ClusteringEvaluatorMetricType: ...
    def setDistanceMeasure(self, value: str) -> ClusteringEvaluator: ...
    def getDistanceMeasure(self) -> str: ...
    def setFeaturesCol(self, value: str) -> ClusteringEvaluator: ...
    def setPredictionCol(self, value: str) -> ClusteringEvaluator: ...

class RankingEvaluator(
    JavaEvaluator,
    HasLabelCol,
    HasPredictionCol,
    JavaMLReadable[RankingEvaluator],
    JavaMLWritable,
):
    metricName: Param[RankingEvaluatorMetricType]
    k: Param[int]
    def __init__(
        self,
        *,
        predictionCol: str = ...,
        labelCol: str = ...,
        metricName: RankingEvaluatorMetricType = ...,
        k: int = ...
    ) -> None: ...
    def setMetricName(self, value: RankingEvaluatorMetricType) -> RankingEvaluator: ...
    def getMetricName(self) -> RankingEvaluatorMetricType: ...
    def setK(self, value: int) -> RankingEvaluator: ...
    def getK(self) -> int: ...
    def setLabelCol(self, value: str) -> RankingEvaluator: ...
    def setPredictionCol(self, value: str) -> RankingEvaluator: ...
    def setParams(
        self,
        *,
        predictionCol: str = ...,
        labelCol: str = ...,
        metricName: RankingEvaluatorMetricType = ...,
        k: int = ...
    ) -> RankingEvaluator: ...
