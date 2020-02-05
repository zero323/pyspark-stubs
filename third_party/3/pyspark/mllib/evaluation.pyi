# Stubs for pyspark.mllib.evaluation (Python 3.5)
#

from typing import Any, List, Optional, Tuple, TypeVar
from pyspark.rdd import RDD
from pyspark.mllib.common import JavaModelWrapper
from pyspark.mllib.linalg import Matrix

T = TypeVar("T")

class BinaryClassificationMetrics(JavaModelWrapper):
    def __init__(self, scoreAndLabels: RDD[Tuple[float, float]]) -> None: ...
    @property
    def areaUnderROC(self) -> float: ...
    @property
    def areaUnderPR(self) -> float: ...
    def unpersist(self) -> None: ...

class RegressionMetrics(JavaModelWrapper):
    def __init__(self, predictionAndObservations: RDD[Tuple[float, float]]) -> None: ...
    @property
    def explainedVariance(self) -> float: ...
    @property
    def meanAbsoluteError(self) -> float: ...
    @property
    def meanSquaredError(self) -> float: ...
    @property
    def rootMeanSquaredError(self) -> float: ...
    @property
    def r2(self) -> float: ...

class MulticlassMetrics(JavaModelWrapper):
    def __init__(self, predictionAndLabels: RDD[Tuple[float, float]]) -> None: ...
    def confusionMatrix(self) -> Matrix: ...
    def truePositiveRate(self, label: float) -> float: ...
    def falsePositiveRate(self, label: float) -> float: ...
    def precision(self, label: float = ...) -> float: ...
    def recall(self, label: float = ...) -> float: ...
    def fMeasure(self, label: float = ..., beta: Optional[float] = ...) -> float: ...
    @property
    def accuracy(self) -> float: ...
    @property
    def weightedTruePositiveRate(self) -> float: ...
    @property
    def weightedFalsePositiveRate(self) -> float: ...
    @property
    def weightedRecall(self) -> float: ...
    @property
    def weightedPrecision(self) -> float: ...
    def weightedFMeasure(self, beta: Optional[float] = ...) -> float: ...

class RankingMetrics(JavaModelWrapper):
    def __init__(self, predictionAndLabels: RDD[Tuple[List[T], List[T]]]) -> None: ...
    def precisionAt(self, k: int) -> float: ...
    @property
    def meanAveragePrecision(self) -> float: ...
    def meanAveragePrecisionAt(self, k: int) -> float: ...
    def ndcgAt(self, k: int) -> float: ...
    def recallAt(self, k: int) -> float: ...

class MultilabelMetrics(JavaModelWrapper):
    def __init__(
        self, predictionAndLabels: RDD[Tuple[List[float], List[float]]]
    ) -> None: ...
    def precision(self, label: Optional[float] = ...) -> float: ...
    def recall(self, label: Optional[float] = ...) -> float: ...
    def f1Measure(self, label: Optional[float] = ...) -> float: ...
    @property
    def microPrecision(self) -> float: ...
    @property
    def microRecall(self) -> float: ...
    @property
    def microF1Measure(self) -> float: ...
    @property
    def hammingLoss(self) -> float: ...
    @property
    def subsetAccuracy(self) -> float: ...
    @property
    def accuracy(self) -> float: ...
