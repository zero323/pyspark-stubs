# Stubs for pyspark.mllib.regression (Python 3.5)
#

from typing import overload
from typing import Any, Iterable, Optional, Tuple, TypeVar, Union
from pyspark.rdd import RDD
from pyspark.mllib._typing import VectorLike
from pyspark.context import SparkContext
from pyspark.mllib.linalg import Vector
from pyspark.mllib.util import Saveable, Loader
from pyspark.streaming.dstream import DStream
from numpy import ndarray  # type: ignore

K = TypeVar("K")

class LabeledPoint:
    label: int
    features: Vector
    def __init__(self, label: float, features: Iterable[float]) -> None: ...
    def __reduce__(self) -> Tuple[type, Tuple[bytes]]: ...

class LinearModel:
    def __init__(self, weights: Vector, intercept: float) -> None: ...
    @property
    def weights(self) -> Vector: ...
    @property
    def intercept(self) -> float: ...

class LinearRegressionModelBase(LinearModel):
    @overload
    def predict(self, x: Vector) -> float: ...
    @overload
    def predict(self, x: RDD[Vector]) -> RDD[float]: ...

class LinearRegressionModel(LinearRegressionModelBase):
    def save(self, sc: SparkContext, path: str) -> None: ...
    @classmethod
    def load(cls, sc: SparkContext, path: str) -> LinearRegressionModel: ...

class LinearRegressionWithSGD:
    @classmethod
    def train(
        cls,
        data: RDD[LabeledPoint],
        iterations: int = ...,
        step: float = ...,
        miniBatchFraction: float = ...,
        initialWeights: Optional[VectorLike] = ...,
        regParam: float = ...,
        regType: Optional[str] = ...,
        intercept: bool = ...,
        validateData: bool = ...,
        convergenceTol: float = ...,
    ) -> LinearRegressionModel: ...

class LassoModel(LinearRegressionModelBase):
    def save(self, sc: SparkContext, path: str) -> None: ...
    @classmethod
    def load(cls, sc: SparkContext, path: str) -> LassoModel: ...

class LassoWithSGD:
    @classmethod
    def train(
        cls,
        data: RDD[LabeledPoint],
        iterations: int = ...,
        step: float = ...,
        regParam: float = ...,
        miniBatchFraction: float = ...,
        initialWeights: Optional[VectorLike] = ...,
        intercept: bool = ...,
        validateData: bool = ...,
        convergenceTol: float = ...,
    ) -> LassoModel: ...

class RidgeRegressionModel(LinearRegressionModelBase):
    def save(self, sc: SparkContext, path: str) -> None: ...
    @classmethod
    def load(cls, sc: SparkContext, path: str) -> RidgeRegressionModel: ...

class RidgeRegressionWithSGD:
    @classmethod
    def train(
        cls,
        data: RDD[LabeledPoint],
        iterations: int = ...,
        step: float = ...,
        regParam: float = ...,
        miniBatchFraction: float = ...,
        initialWeights: Optional[VectorLike] = ...,
        intercept: bool = ...,
        validateData: bool = ...,
        convergenceTol: float = ...,
    ) -> RidgeRegressionModel: ...

class IsotonicRegressionModel(Saveable, Loader[IsotonicRegressionModel]):
    boundaries: ndarray
    predictions: ndarray
    isotonic: bool
    def __init__(
        self, boundaries: ndarray, predictions: ndarray, isotonic: bool
    ) -> None: ...
    @overload
    def predict(self, x: Vector) -> ndarray: ...
    @overload
    def predict(self, x: RDD[Vector]) -> RDD[ndarray]: ...
    def save(self, sc: SparkContext, path: str) -> None: ...
    @classmethod
    def load(cls, sc: SparkContext, path: str) -> IsotonicRegressionModel: ...

class IsotonicRegression:
    @classmethod
    def train(
        cls, data: RDD[VectorLike], isotonic: bool = ...
    ) -> IsotonicRegressionModel: ...

class StreamingLinearAlgorithm:
    def __init__(self, model: LinearModel) -> None: ...
    def latestModel(self) -> LinearModel: ...
    def predictOn(self, dstream: DStream[VectorLike]) -> DStream[float]: ...
    def predictOnValues(
        self, dstream: DStream[Tuple[K, VectorLike]]
    ) -> DStream[Tuple[K, float]]: ...

class StreamingLinearRegressionWithSGD(StreamingLinearAlgorithm):
    stepSize: float
    numIterations: int
    miniBatchFraction: float
    convergenceTol: float
    def __init__(
        self,
        stepSize: float = ...,
        numIterations: int = ...,
        miniBatchFraction: float = ...,
        convergenceTol: float = ...,
    ) -> None: ...
    def setInitialWeights(
        self, initialWeights: VectorLike
    ) -> StreamingLinearRegressionWithSGD: ...
    def trainOn(self, dstream: DStream[LabeledPoint]) -> None: ...
