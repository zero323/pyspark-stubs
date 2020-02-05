# Stubs for pyspark.mllib.clustering (Python 3.5)
#

from typing import overload
from typing import Any, List, NamedTuple, Optional, Tuple, TypeVar

import array

from numpy import float64, int64, ndarray  # type: ignore
from py4j.java_gateway import JavaObject  # type: ignore

from pyspark.mllib._typing import VectorLike
from pyspark.context import SparkContext
from pyspark.rdd import RDD
from pyspark.mllib.common import JavaModelWrapper
from pyspark.mllib.stat.distribution import MultivariateGaussian
from pyspark.mllib.util import Saveable, Loader, JavaLoader, JavaSaveable
from pyspark.streaming.dstream import DStream

T = TypeVar("T")

class BisectingKMeansModel(JavaModelWrapper):
    centers: List[ndarray]
    def __init__(self, java_model: JavaObject) -> None: ...
    @property
    def clusterCenters(self) -> List[ndarray]: ...
    @property
    def k(self) -> int: ...
    @overload
    def predict(self, x: VectorLike) -> int: ...
    @overload
    def predict(self, x: RDD[VectorLike]) -> RDD[int]: ...
    @overload
    def computeCost(self, x: VectorLike) -> float: ...
    @overload
    def computeCost(self, x: RDD[VectorLike]) -> float: ...

class BisectingKMeans:
    @classmethod
    def train(
        self,
        rdd: RDD[VectorLike],
        k: int = ...,
        maxIterations: int = ...,
        minDivisibleClusterSize: float = ...,
        seed: int = ...,
    ) -> BisectingKMeansModel: ...

class KMeansModel(Saveable, Loader[KMeansModel]):
    centers: List[ndarray]
    def __init__(self, centers: List[ndarray]) -> None: ...
    @property
    def clusterCenters(self) -> List[ndarray]: ...
    @property
    def k(self) -> int: ...
    @overload
    def predict(self, x: VectorLike) -> int: ...
    @overload
    def predict(self, x: RDD[VectorLike]) -> RDD[int]: ...
    def computeCost(self, rdd: RDD[VectorLike]) -> float: ...
    def save(self, sc: SparkContext, path: str) -> None: ...
    @classmethod
    def load(cls, sc: SparkContext, path: str) -> KMeansModel: ...

class KMeans:
    @classmethod
    def train(
        cls,
        rdd: RDD[VectorLike],
        k: int,
        maxIterations: int = ...,
        initializationMode: str = ...,
        seed: Optional[int] = ...,
        initializationSteps: int = ...,
        epsilon: float = ...,
        initialModel: Optional[KMeansModel] = ...,
    ) -> KMeansModel: ...

class GaussianMixtureModel(
    JavaModelWrapper, JavaSaveable, JavaLoader[GaussianMixtureModel]
):
    @property
    def weights(self) -> ndarray: ...
    @property
    def gaussians(self) -> List[MultivariateGaussian]: ...
    @property
    def k(self) -> int: ...
    @overload
    def predict(self, x: VectorLike) -> int64: ...
    @overload
    def predict(self, x: RDD[VectorLike]) -> RDD[int]: ...
    @overload
    def predictSoft(self, x: VectorLike) -> ndarray: ...
    @overload
    def predictSoft(self, x: RDD[VectorLike]) -> RDD[array.array]: ...
    @classmethod
    def load(cls, sc: SparkContext, path: str) -> GaussianMixtureModel: ...

class GaussianMixture:
    @classmethod
    def train(
        cls,
        rdd: RDD[VectorLike],
        k: int,
        convergenceTol: float = ...,
        maxIterations: int = ...,
        seed: Optional[int] = ...,
        initialModel: Optional[GaussianMixtureModel] = ...,
    ) -> GaussianMixtureModel: ...

class PowerIterationClusteringModel(
    JavaModelWrapper, JavaSaveable, JavaLoader[PowerIterationClusteringModel]
):
    @property
    def k(self) -> int: ...
    def assignments(self) -> RDD[PowerIterationClustering.Assignment]: ...
    @classmethod
    def load(cls, sc: SparkContext, path: str) -> PowerIterationClusteringModel: ...

class PowerIterationClustering:
    @classmethod
    def train(
        cls,
        rdd: RDD[Tuple[int, int, float]],
        k: int,
        maxIterations: int = ...,
        initMode: str = ...,
    ) -> PowerIterationClusteringModel: ...
    class Assignment(NamedTuple("Assignment", [("id", int), ("cluster", int)])): ...

class StreamingKMeansModel(KMeansModel):
    def __init__(self, clusterCenters, clusterWeights) -> None: ...
    @property
    def clusterWeights(self) -> List[float64]: ...
    centers: ndarray
    def update(
        self, data: RDD[VectorLike], decayFactor: float, timeUnit: str
    ) -> StreamingKMeansModel: ...

class StreamingKMeans:
    def __init__(
        self, k: int = ..., decayFactor: float = ..., timeUnit: str = ...
    ) -> None: ...
    def latestModel(self) -> StreamingKMeansModel: ...
    def setK(self, k: int) -> StreamingKMeans: ...
    def setDecayFactor(self, decayFactor: float) -> StreamingKMeans: ...
    def setHalfLife(self, halfLife: float, timeUnit: str) -> StreamingKMeans: ...
    def setInitialCenters(
        self, centers: List[VectorLike], weights: List[float]
    ) -> StreamingKMeans: ...
    def setRandomCenters(
        self, dim: int, weight: float, seed: int
    ) -> StreamingKMeans: ...
    def trainOn(self, dstream: DStream[VectorLike]) -> None: ...
    def predictOn(self, dstream: DStream[VectorLike]) -> DStream[int]: ...
    def predictOnValues(
        self, dstream: DStream[Tuple[T, VectorLike]]
    ) -> DStream[Tuple[T, int]]: ...

class LDAModel(JavaModelWrapper, JavaSaveable, Loader[LDAModel]):
    def topicsMatrix(self) -> ndarray: ...
    def vocabSize(self) -> int: ...
    def describeTopics(
        self, maxTermsPerTopic: Optional[int] = ...
    ) -> List[Tuple[List[int], List[float]]]: ...
    @classmethod
    def load(cls, sc: SparkContext, path: str) -> LDAModel: ...

class LDA:
    @classmethod
    def train(
        cls,
        rdd: RDD[Tuple[int, VectorLike]],
        k: int = ...,
        maxIterations: int = ...,
        docConcentration: float = ...,
        topicConcentration: float = ...,
        seed: Optional[int] = ...,
        checkpointInterval: int = ...,
        optimizer: str = ...,
    ) -> LDAModel: ...
