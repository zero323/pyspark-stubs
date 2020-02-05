# Stubs for pyspark.ml.evaluation (Python 3)

import abc
from typing import Any, Dict, Optional, Type
from pyspark.ml._typing import (
    ParamMap,
    BinaryClassificationEvaluatorMetricType,
    ClusteringEvaluatorMetricType,
    MulticlassClassificationEvaluatorMetricType,
    RegressionEvaluatorMetricType,
)

from pyspark.ml.wrapper import JavaParams
from pyspark.ml.param import Param, Params
from pyspark.ml.param.shared import (
    HasFeaturesCol,
    HasLabelCol,
    HasPredictionCol,
    HasRawPredictionCol,
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
    JavaMLReadable[BinaryClassificationEvaluator],
    JavaMLWritable,
):
    metricName: Param[BinaryClassificationEvaluatorMetricType]
    def __init__(
        self,
        *,
        rawPredictionCol: str = ...,
        labelCol: str = ...,
        metricName: BinaryClassificationEvaluatorMetricType = ...
    ) -> None: ...
    def setMetricName(
        self, value: BinaryClassificationEvaluatorMetricType
    ) -> BinaryClassificationEvaluator: ...
    def getMetricName(self) -> BinaryClassificationEvaluatorMetricType: ...
    def setParams(
        self,
        *,
        rawPredictionCol: str = ...,
        labelCol: BinaryClassificationEvaluatorMetricType = ...,
        metricName: str = ...
    ) -> BinaryClassificationEvaluator: ...

class RegressionEvaluator(
    JavaEvaluator,
    HasLabelCol,
    HasPredictionCol,
    JavaMLReadable[RegressionEvaluator],
    JavaMLWritable,
):
    metricName: Param[RegressionEvaluatorMetricType]
    def __init__(
        self,
        *,
        predictionCol: str = ...,
        labelCol: str = ...,
        metricName: RegressionEvaluatorMetricType = ...
    ) -> None: ...
    def setMetricName(
        self, value: RegressionEvaluatorMetricType
    ) -> RegressionEvaluator: ...
    def getMetricName(self) -> RegressionEvaluatorMetricType: ...
    def setParams(
        self,
        *,
        predictionCol: str = ...,
        labelCol: str = ...,
        metricName: RegressionEvaluatorMetricType = ...
    ) -> RegressionEvaluator: ...

class MulticlassClassificationEvaluator(
    JavaEvaluator,
    HasLabelCol,
    HasPredictionCol,
    JavaMLReadable[MulticlassClassificationEvaluator],
    JavaMLWritable,
):
    metricName: Param[MulticlassClassificationEvaluatorMetricType]
    def __init__(
        self,
        *,
        predictionCol: str = ...,
        labelCol: str = ...,
        metricName: MulticlassClassificationEvaluatorMetricType = ...
    ) -> None: ...
    def setMetricName(
        self, value: MulticlassClassificationEvaluatorMetricType
    ) -> MulticlassClassificationEvaluator: ...
    def getMetricName(self) -> MulticlassClassificationEvaluatorMetricType: ...
    def setParams(
        self,
        *,
        predictionCol: str = ...,
        labelCol: str = ...,
        metricName: MulticlassClassificationEvaluatorMetricType = ...
    ) -> MulticlassClassificationEvaluator: ...

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
    def setMetricName(
        self, value: ClusteringEvaluatorMetricType
    ) -> ClusteringEvaluator: ...
    def getMetricName(self) -> ClusteringEvaluatorMetricType: ...
    def setParams(
        self,
        *,
        predictionCol: str = ...,
        featuresCol: str = ...,
        metricName: ClusteringEvaluatorMetricType = ...,
        distanceMeasure: str = ...
    ) -> MulticlassClassificationEvaluator: ...
    def setDistanceMeasure(self, value: str) -> MulticlassClassificationEvaluator: ...
    def getDistanceMeasure(self) -> str: ...
