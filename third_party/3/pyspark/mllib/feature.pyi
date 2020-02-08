# Stubs for pyspark.mllib.feature (Python 3.5)
#

from typing import overload
from typing import Any, Iterable, Hashable, List, Tuple
from pyspark.mllib._typing import VectorLike
from pyspark.context import SparkContext
from pyspark.rdd import RDD
from pyspark.mllib.common import JavaModelWrapper
from pyspark.mllib.linalg import Vector
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.util import JavaLoader, JavaSaveable
from py4j.java_collections import JavaMap  # type: ignore

class VectorTransformer:
    @overload
    def transform(self, vector: VectorLike) -> Vector: ...
    @overload
    def transform(self, vector: RDD[VectorLike]) -> RDD[Vector]: ...

class Normalizer(VectorTransformer):
    p: float
    def __init__(self, p: float = ...) -> None: ...
    @overload
    def transform(self, vector: VectorLike) -> Vector: ...
    @overload
    def transform(self, vector: RDD[VectorLike]) -> RDD[Vector]: ...

class JavaVectorTransformer(JavaModelWrapper, VectorTransformer):
    @overload
    def transform(self, vector: VectorLike) -> Vector: ...
    @overload
    def transform(self, vector: RDD[VectorLike]) -> RDD[Vector]: ...

class StandardScalerModel(JavaVectorTransformer):
    @overload
    def transform(self, vector: VectorLike) -> Vector: ...
    @overload
    def transform(self, vector: RDD[VectorLike]) -> RDD[Vector]: ...
    def setWithMean(self, withMean: bool) -> StandardScalerModel: ...
    def setWithStd(self, withStd: bool) -> StandardScalerModel: ...
    @property
    def withStd(self) -> bool: ...
    @property
    def withMean(self) -> bool: ...
    @property
    def std(self) -> Vector: ...
    @property
    def mean(self) -> Vector: ...

class StandardScaler:
    withMean: bool
    withStd: bool
    def __init__(self, withMean: bool = ..., withStd: bool = ...) -> None: ...
    def fit(self, dataset: RDD[VectorLike]) -> StandardScalerModel: ...

class ChiSqSelectorModel(JavaVectorTransformer):
    @overload
    def transform(self, vector: VectorLike) -> Vector: ...
    @overload
    def transform(self, vector: RDD[VectorLike]) -> RDD[Vector]: ...

class ChiSqSelector:
    numTopFeatures: int
    selectorType: str
    percentile: float
    fpr: float
    fdr: float
    fwe: float
    def __init__(self, numTopFeatures: int = ..., selectorType: str = ..., percentile: float = ..., fpr: float = ..., fdr: float = ..., fwe: float = ...) -> None: ...
    def setNumTopFeatures(self, numTopFeatures: int) -> ChiSqSelector: ...
    def setPercentile(self, percentile: float) -> ChiSqSelector: ...
    def setFpr(self, fpr: float) -> ChiSqSelector: ...
    def setFdr(self, fdr: float) -> ChiSqSelector: ...
    def setFwe(self, fwe: float) -> ChiSqSelector: ...
    def setSelectorType(self, selectorType: str) -> ChiSqSelector: ...
    def fit(self, data: RDD[LabeledPoint]) -> ChiSqSelectorModel: ...

class PCAModel(JavaVectorTransformer): ...

class PCA:
    k: int
    def __init__(self, k: int) -> None: ...
    def fit(self, data: RDD[VectorLike]) -> PCAModel: ...

class HashingTF:
    numFeatures: int
    binary: bool
    def __init__(self, numFeatures: int = ...) -> None: ...
    def setBinary(self, value: bool) -> HashingTF: ...
    def indexOf(self, term: Hashable) -> int: ...
    @overload
    def transform(self, document: Iterable[Hashable]) -> Vector: ...
    @overload
    def transform(self, document: RDD[Iterable[Hashable]]) -> RDD[Vector]: ...

class IDFModel(JavaVectorTransformer):
    @overload
    def transform(self, x: VectorLike) -> Vector: ...
    @overload
    def transform(self, x: RDD[VectorLike]) -> RDD[Vector]: ...
    def idf(self) -> Vector: ...
    def docFreq(self) -> List[int]: ...
    def numDocs(self) -> int: ...

class IDF:
    minDocFreq: int
    def __init__(self, minDocFreq: int = ...) -> None: ...
    def fit(self, dataset: RDD[VectorLike]) -> IDFModel: ...

class Word2VecModel(JavaVectorTransformer, JavaSaveable, JavaLoader[Word2VecModel]):
    def transform(self, word: str) -> Vector: ...  # type: ignore
    def findSynonyms(self, word: str, num: int) -> Iterable[Tuple[str, float]]: ...
    def getVectors(self) -> JavaMap: ...
    @classmethod
    def load(cls, sc: SparkContext, path: str) -> Word2VecModel: ...

class Word2Vec:
    vectorSize: int
    learningRate: float
    numPartitions: int
    numIterations: int
    seed: int
    minCount: int
    windowSize: int
    def __init__(self) -> None: ...
    def setVectorSize(self, vectorSize: int) -> Word2Vec: ...
    def setLearningRate(self, learningRate: float) -> Word2Vec: ...
    def setNumPartitions(self, numPartitions: int) -> Word2Vec: ...
    def setNumIterations(self, numIterations: int) -> Word2Vec: ...
    def setSeed(self, seed: int) -> Word2Vec: ...
    def setMinCount(self, minCount: int) -> Word2Vec: ...
    def setWindowSize(self, windowSize: int) -> Word2Vec: ...
    def fit(self, data: RDD[List[str]]) -> Word2VecModel: ...

class ElementwiseProduct(VectorTransformer):
    scalingVector: Vector
    def __init__(self, scalingVector: Vector) -> None: ...
    @overload
    def transform(self, vector: VectorLike) -> Vector: ...
    @overload
    def transform(self, vector: RDD[VectorLike]) -> RDD[Vector]: ...
