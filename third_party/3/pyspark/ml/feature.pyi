# Stubs for pyspark.ml.feature (Python 3.5)
#

from typing import overload
from typing import Any, Dict, List, Optional, Tuple
from pyspark.ml.param.shared import *
from pyspark.ml.util import JavaMLReadable, JavaMLWritable
from pyspark.ml.wrapper import JavaEstimator, JavaModel, JavaTransformer
from pyspark.ml.linalg import Vector, DenseVector, DenseMatrix
from pyspark.sql.dataframe import DataFrame

class Binarizer(
    JavaTransformer, HasInputCol, HasOutputCol, JavaMLReadable, JavaMLWritable
):
    threshold = ...  # type: Param
    def __init__(
        self,
        *,
        threshold: float = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        threshold: float = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...
    ) -> Binarizer: ...
    def setThreshold(self, value: float) -> Binarizer: ...
    def getThreshold(self) -> float: ...

class LSHParams(Params):
    numHashTables = ...  # type: Param
    def __init__(self) -> None: ...
    def setNumHashTables(self, value: int) -> LSHParams: ...
    def getNumHashTables(self) -> int: ...

class LSHModel(JavaModel):
    def approxNearestNeighbors(
        self,
        dataset: DataFrame,
        key: Vector,
        numNearestNeighbors: int,
        distCol: str = ...,
    ) -> DataFrame: ...
    def approxSimilarityJoin(
        self,
        datasetA: DataFrame,
        datasetB: DataFrame,
        threshold: float,
        distCol: str = ...,
    ) -> DataFrame: ...

class BucketedRandomProjectionLSH(
    JavaEstimator,
    LSHParams,
    HasInputCol,
    HasOutputCol,
    HasSeed,
    JavaMLReadable,
    JavaMLWritable,
):
    bucketLength = ...  # type: Param
    def __init__(
        self,
        *,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        seed: Optional[int] = ...,
        numHashTables: int = ...,
        bucketLength: Optional[float] = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        seed: Optional[int] = ...,
        numHashTables: int = ...,
        bucketLength: Optional[float] = ...
    ) -> BucketedRandomProjectionLSH: ...
    def setBucketLength(self, value: float) -> BucketedRandomProjectionLSH: ...
    def getBucketLength(self) -> float: ...

class BucketedRandomProjectionLSHModel(LSHModel, JavaMLReadable, JavaMLWritable): ...

class Bucketizer(
    JavaTransformer,
    HasInputCol,
    HasOutputCol,
    HasHandleInvalid,
    JavaMLReadable,
    JavaMLWritable,
):
    splits = ...  # type: Param
    handleInvalid = ...  # type: Param
    def __init__(
        self,
        *,
        splits: Optional[List[float]] = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        handleInvalid: str = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        splits: Optional[List[float]] = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        handleInvalid: str = ...
    ) -> Bucketizer: ...
    def setSplits(self, value: List[float]) -> Bucketizer: ...
    def getSplits(self) -> List[float]: ...

class CountVectorizer(
    JavaEstimator, HasInputCol, HasOutputCol, JavaMLReadable, JavaMLWritable
):
    minTF = ...  # type: Param
    minDF = ...  # type: Param
    vocabSize = ...  # type: Param
    binary = ...  # type: Param
    def __init__(
        self,
        *,
        minTF: float = ...,
        minDF: float = ...,
        vocabSize: int = ...,
        binary: bool = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        minTF: float = ...,
        minDF: float = ...,
        vocabSize: int = ...,
        binary: bool = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...
    ) -> CountVectorizer: ...
    def setMinTF(self, value: float) -> CountVectorizer: ...
    def getMinTF(self) -> float: ...
    def setMinDF(self, value: float) -> CountVectorizer: ...
    def getMinDF(self) -> float: ...
    def setVocabSize(self, value: int) -> CountVectorizer: ...
    def getVocabSize(self) -> int: ...
    def setBinary(self, value: bool) -> CountVectorizer: ...
    def getBinary(self) -> bool: ...

class CountVectorizerModel(JavaModel, JavaMLReadable, JavaMLWritable):
    @property
    def vocabulary(self) -> List[str]: ...

class DCT(JavaTransformer, HasInputCol, HasOutputCol, JavaMLReadable, JavaMLWritable):
    inverse = ...  # type: Param
    def __init__(
        self,
        *,
        inverse: bool = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        inverse: bool = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...
    ) -> DCT: ...
    def setInverse(self, value: bool) -> DCT: ...
    def getInverse(self) -> bool: ...

class ElementwiseProduct(
    JavaTransformer, HasInputCol, HasOutputCol, JavaMLReadable, JavaMLWritable
):
    scalingVec = ...  # type: Param
    def __init__(
        self,
        *,
        scalingVec: Optional[Vector] = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        scalingVec: Optional[Vector] = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...
    ) -> ElementwiseProduct: ...
    def setScalingVec(self, value: Vector) -> ElementwiseProduct: ...
    def getScalingVec(self) -> Vector: ...

class FeatureHasher(
    JavaTransformer,
    HasInputCols,
    HasOutputCol,
    HasNumFeatures,
    JavaMLReadable,
    JavaMLWritable,
):
    categoricalCols = ...  # type: Param
    def __init__(
        self,
        *,
        numFeatures: int = ...,
        inputCols: Optional[List[str]] = ...,
        outputCol: Optional[str] = ...,
        categoricalCols: Optional[List[str]] = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        numFeatures: int = ...,
        inputCols: Optional[List[str]] = ...,
        outputCol: Optional[str] = ...,
        categoricalCols: Optional[List[str]] = ...
    ) -> FeatureHasher: ...
    def setCategoricalCols(self, value: List[str]) -> FeatureHasher: ...
    def getCategoricalCols(self) -> List[str]: ...

class HashingTF(
    JavaTransformer,
    HasInputCol,
    HasOutputCol,
    HasNumFeatures,
    JavaMLReadable,
    JavaMLWritable,
):
    binary = ...  # type: Param
    def __init__(
        self,
        *,
        numFeatures: int = ...,
        binary: bool = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        numFeatures: int = ...,
        binary: bool = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...
    ) -> HashingTF: ...
    def setBinary(self, value: bool) -> HashingTF: ...
    def getBinary(self) -> bool: ...

class IDF(JavaEstimator, HasInputCol, HasOutputCol, JavaMLReadable, JavaMLWritable):
    minDocFreq = ...  # type: Param
    def __init__(
        self,
        *,
        minDocFreq: int = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        minDocFreq: int = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...
    ) -> IDF: ...
    def setMinDocFreq(self, value: int) -> IDF: ...
    def getMinDocFreq(self) -> int: ...

class IDFModel(JavaModel, JavaMLReadable, JavaMLWritable):
    @property
    def idf(self) -> Vector: ...

class Imputer(JavaEstimator, HasInputCols, JavaMLReadable, JavaMLWritable):
    outputCols = ...  # type: Param
    strategy = ...  # type: Param
    missingValue = ...  # type: Param
    def __init__(
        self,
        *,
        strategy: str = ...,
        missingValue: float = ...,
        inputCols: Optional[List[str]] = ...,
        outputCols: Optional[List[str]] = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        strategy: str = ...,
        missingValue: float = ...,
        inputCols: Optional[List[str]] = ...,
        outputCols: Optional[List[str]] = ...
    ) -> Imputer: ...
    def setOutputCols(self, value: List[str]) -> Imputer: ...
    def getOutputCols(self) -> List[str]: ...
    def setStrategy(self, value: str) -> Imputer: ...
    def getStrategy(self) -> str: ...
    def setMissingValue(self, value: float) -> Imputer: ...
    def getMissingValue(self) -> float: ...

class ImputerModel(JavaModel, JavaMLReadable, JavaMLWritable):
    @property
    def surrogateDF(self) -> DataFrame: ...

class MaxAbsScaler(
    JavaEstimator, HasInputCol, HasOutputCol, JavaMLReadable, JavaMLWritable
):
    def __init__(
        self, *, inputCol: Optional[str] = ..., outputCol: Optional[str] = ...
    ) -> None: ...
    def setParams(
        self, *, inputCol: Optional[str] = ..., outputCol: Optional[str] = ...
    ) -> MaxAbsScaler: ...

class MaxAbsScalerModel(JavaModel, JavaMLReadable, JavaMLWritable):
    @property
    def maxAbs(self) -> Vector: ...

class MinHashLSH(
    JavaEstimator,
    LSHParams,
    HasInputCol,
    HasOutputCol,
    HasSeed,
    JavaMLReadable,
    JavaMLWritable,
):
    def __init__(
        self,
        *,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        seed: Optional[int] = ...,
        numHashTables: int = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        seed: Optional[int] = ...,
        numHashTables: int = ...
    ) -> MinHashLSH: ...

class MinHashLSHModel(LSHModel, JavaMLReadable, JavaMLWritable): ...

class MinMaxScaler(
    JavaEstimator, HasInputCol, HasOutputCol, JavaMLReadable, JavaMLWritable
):
    min = ...  # type: Param
    max = ...  # type: Param
    def __init__(
        self,
        *,
        min: float = ...,
        max: float = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        min: float = ...,
        max: float = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...
    ) -> MinMaxScaler: ...
    def setMin(self, value: float) -> MinMaxScaler: ...
    def getMin(self) -> float: ...
    def setMax(self, value: float) -> MinMaxScaler: ...
    def getMax(self) -> float: ...

class MinMaxScalerModel(JavaModel, JavaMLReadable, JavaMLWritable):
    @property
    def originalMin(self) -> Vector: ...
    @property
    def originalMax(self) -> Vector: ...

class NGram(JavaTransformer, HasInputCol, HasOutputCol, JavaMLReadable, JavaMLWritable):
    n = ...  # type: Param
    def __init__(
        self,
        *,
        n: int = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        n: int = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...
    ) -> NGram: ...
    def setN(self, value: int) -> NGram: ...
    def getN(self) -> int: ...

class Normalizer(
    JavaTransformer, HasInputCol, HasOutputCol, JavaMLReadable, JavaMLWritable
):
    p = ...  # type: Param
    def __init__(
        self,
        *,
        p: float = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        p: float = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...
    ) -> Normalizer: ...
    def setP(self, value: float) -> Normalizer: ...
    def getP(self) -> float: ...

class OneHotEncoder(
    JavaTransformer, HasInputCol, HasOutputCol, JavaMLReadable, JavaMLWritable
):
    dropLast = ...  # type: Param
    def __init__(
        self,
        *,
        dropLast: bool = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        dropLast: bool = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...
    ) -> OneHotEncoder: ...
    def setDropLast(self, value: bool) -> OneHotEncoder: ...
    def getDropLast(self) -> bool: ...

class OneHotEncoderEstimator(
    JavaEstimator,
    HasInputCols,
    HasOutputCols,
    HasHandleInvalid,
    JavaMLReadable,
    JavaMLWritable,
):
    handleInvalid = ...  # type: Param
    dropLast = ...  # type: Param
    def __init__(
        self,
        *,
        inputCols: Optional[List[str]] = ...,
        outputCols: Optional[List[str]] = ...,
        handleInvalid: str = ...,
        dropLast: bool = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        inputCols: Optional[List[str]] = ...,
        outputCols: Optional[List[str]] = ...,
        handleInvalid: str = ...,
        dropLast: bool = ...
    ) -> OneHotEncoderEstimator: ...
    def setDropLast(self, value: bool) -> OneHotEncoderEstimator: ...
    def getDropLast(self) -> bool: ...

class OneHotEncoderModel(JavaModel, JavaMLReadable, JavaMLWritable):
    @property
    def categorySizes(self) -> List[int]: ...

class PolynomialExpansion(
    JavaTransformer, HasInputCol, HasOutputCol, JavaMLReadable, JavaMLWritable
):
    degree = ...  # type: Param
    def __init__(
        self,
        *,
        degree: int = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        degree: int = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...
    ) -> PolynomialExpansion: ...
    def setDegree(self, value: int) -> PolynomialExpansion: ...
    def getDegree(self) -> int: ...

class QuantileDiscretizer(
    JavaEstimator,
    HasInputCol,
    HasOutputCol,
    HasHandleInvalid,
    JavaMLReadable,
    JavaMLWritable,
):
    numBuckets = ...  # type: Param
    relativeError = ...  # type: Param
    handleInvalid = ...  # type: Param
    def __init__(
        self,
        *,
        numBuckets: int = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        relativeError: float = ...,
        handleInvalid: str = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        numBuckets: int = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        relativeError: float = ...,
        handleInvalid: str = ...
    ) -> QuantileDiscretizer: ...
    def setNumBuckets(self, value: int) -> QuantileDiscretizer: ...
    def getNumBuckets(self) -> int: ...
    def setRelativeError(self, value: float) -> QuantileDiscretizer: ...
    def getRelativeError(self) -> float: ...

class RegexTokenizer(
    JavaTransformer, HasInputCol, HasOutputCol, JavaMLReadable, JavaMLWritable
):
    minTokenLength = ...  # type: Param
    gaps = ...  # type: Param
    pattern = ...  # type: Param
    toLowercase = ...  # type: Param
    def __init__(
        self,
        *,
        minTokenLength: int = ...,
        gaps: bool = ...,
        pattern: str = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        toLowercase: bool = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        minTokenLength: int = ...,
        gaps: bool = ...,
        pattern: str = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        toLowercase: bool = ...
    ) -> RegexTokenizer: ...
    def setMinTokenLength(self, value: int) -> RegexTokenizer: ...
    def getMinTokenLength(self) -> int: ...
    def setGaps(self, value: bool) -> RegexTokenizer: ...
    def getGaps(self) -> bool: ...
    def setPattern(self, value: str) -> RegexTokenizer: ...
    def getPattern(self) -> str: ...
    def setToLowercase(self, value: bool) -> RegexTokenizer: ...
    def getToLowercase(self) -> bool: ...

class SQLTransformer(JavaTransformer, JavaMLReadable, JavaMLWritable):
    statement = ...  # type: Param
    def __init__(self, *, statement: Optional[str] = ...) -> None: ...
    def setParams(self, *, statement: Optional[str] = ...) -> SQLTransformer: ...
    def setStatement(self, value: str) -> SQLTransformer: ...
    def getStatement(self) -> str: ...

class StandardScaler(
    JavaEstimator, HasInputCol, HasOutputCol, JavaMLReadable, JavaMLWritable
):
    withMean = ...  # type: Param
    withStd = ...  # type: Param
    def __init__(
        self,
        *,
        withMean: bool = ...,
        withStd: bool = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        withMean: bool = ...,
        withStd: bool = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...
    ) -> StandardScaler: ...
    def setWithMean(self, value: bool) -> StandardScaler: ...
    def getWithMean(self) -> bool: ...
    def setWithStd(self, value: bool) -> StandardScaler: ...
    def getWithStd(self) -> bool: ...

class StandardScalerModel(JavaModel, JavaMLReadable, JavaMLWritable):
    @property
    def std(self) -> Vector: ...
    @property
    def mean(self) -> Vector: ...

class StringIndexer(
    JavaEstimator,
    HasInputCol,
    HasOutputCol,
    HasHandleInvalid,
    JavaMLReadable,
    JavaMLWritable,
):
    stringOrderType = ...  # type: Param
    handleInvalid = ...  # type: Param
    def __init__(
        self,
        *,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        handleInvalid: str = ...,
        stringOrderType: str = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        handleInvalid: str = ...,
        stringOrderType: str = ...
    ) -> StringIndexer: ...
    def setStringOrderType(self, value: str) -> StringIndexer: ...
    def getStringOrderType(self) -> str: ...

class StringIndexerModel(JavaModel, JavaMLReadable, JavaMLWritable):
    @property
    def labels(self) -> List[str]: ...

class IndexToString(
    JavaTransformer, HasInputCol, HasOutputCol, JavaMLReadable, JavaMLWritable
):
    labels = ...  # type: Param
    def __init__(
        self,
        *,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        labels: Optional[List[str]] = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        labels: Optional[List[str]] = ...
    ) -> IndexToString: ...
    def setLabels(self, value: List[str]) -> IndexToString: ...
    def getLabels(self) -> List[str]: ...

class StopWordsRemover(
    JavaTransformer, HasInputCol, HasOutputCol, JavaMLReadable, JavaMLWritable
):
    stopWords = ...  # type: Param
    caseSensitive = ...  # type: Param
    def __init__(
        self,
        *,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        stopWords: Optional[List[str]] = ...,
        caseSensitive: bool = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        stopWords: Optional[List[str]] = ...,
        caseSensitive: bool = ...
    ) -> StopWordsRemover: ...
    def setStopWords(self, value: List[str]) -> StopWordsRemover: ...
    def getStopWords(self) -> List[str]: ...
    def setCaseSensitive(self, value: bool) -> StopWordsRemover: ...
    def getCaseSensitive(self) -> bool: ...
    @staticmethod
    def loadDefaultStopWords(language: str) -> List[str]: ...

class Tokenizer(
    JavaTransformer, HasInputCol, HasOutputCol, JavaMLReadable, JavaMLWritable
):
    def __init__(
        self, *, inputCol: Optional[str] = ..., outputCol: Optional[str] = ...
    ) -> None: ...
    def setParams(
        self, *, inputCol: Optional[str] = ..., outputCol: Optional[str] = ...
    ) -> Tokenizer: ...

class VectorAssembler(
    JavaTransformer, HasInputCols, HasOutputCol, JavaMLReadable, JavaMLWritable
):
    def __init__(
        self, *, inputCols: Optional[List[str]] = ..., outputCol: Optional[str] = ...
    ) -> None: ...
    def setParams(
        self, *, inputCols: Optional[List[str]] = ..., outputCol: Optional[str] = ...
    ) -> VectorAssembler: ...

class VectorIndexer(
    JavaEstimator,
    HasInputCol,
    HasOutputCol,
    HasHandleInvalid,
    JavaMLReadable,
    JavaMLWritable,
):
    maxCategories = ...  # type: Param
    handleInvalid = ...  # type: Param
    def __init__(
        self,
        *,
        maxCategories: int = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        handleInvalid: str = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        maxCategories: int = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        handleInvalid: str = ...
    ) -> VectorIndexer: ...
    def setMaxCategories(self, value: int) -> VectorIndexer: ...
    def getMaxCategories(self) -> int: ...

class VectorIndexerModel(JavaModel, JavaMLReadable, JavaMLWritable):
    @property
    def numFeatures(self) -> int: ...
    @property
    def categoryMaps(self) -> Dict[int, Tuple[float, int]]: ...

class VectorSlicer(
    JavaTransformer, HasInputCol, HasOutputCol, JavaMLReadable, JavaMLWritable
):
    indices = ...  # type: Param
    names = ...  # type: Param
    def __init__(
        self,
        *,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        indices: Optional[List[int]] = ...,
        names: Optional[List[str]] = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        indices: Optional[List[int]] = ...,
        names: Optional[List[str]] = ...
    ) -> VectorSlicer: ...
    def setIndices(self, value: List[int]) -> VectorSlicer: ...
    def getIndices(self) -> List[int]: ...
    def setNames(self, value: List[str]) -> VectorSlicer: ...
    def getNames(self) -> List[str]: ...

class Word2Vec(
    JavaEstimator,
    HasStepSize,
    HasMaxIter,
    HasSeed,
    HasInputCol,
    HasOutputCol,
    JavaMLReadable,
    JavaMLWritable,
):
    vectorSize = ...  # type: Param
    numPartitions = ...  # type: Param
    minCount = ...  # type: Param
    windowSize = ...  # type: Param
    maxSentenceLength = ...  # type: Param
    def __init__(
        self,
        *,
        vectorSize: int = ...,
        minCount: int = ...,
        numPartitions: int = ...,
        stepSize: float = ...,
        maxIter: int = ...,
        seed: Optional[int] = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        windowSize: int = ...,
        maxSentenceLength: int = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        vectorSize: int = ...,
        minCount: int = ...,
        numPartitions: int = ...,
        stepSize: float = ...,
        maxIter: int = ...,
        seed: Optional[int] = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        windowSize: int = ...,
        maxSentenceLength: int = ...
    ) -> Word2Vec: ...
    def setVectorSize(self, value: int) -> Word2Vec: ...
    def getVectorSize(self) -> int: ...
    def setNumPartitions(self, value: int) -> Word2Vec: ...
    def getNumPartitions(self) -> int: ...
    def setMinCount(self, value: int) -> Word2Vec: ...
    def getMinCount(self) -> int: ...
    def setWindowSize(self, value: int) -> Word2Vec: ...
    def getWindowSize(self) -> int: ...
    def setMaxSentenceLength(self, value: int) -> Word2Vec: ...
    def getMaxSentenceLength(self) -> int: ...

class Word2VecModel(JavaModel, JavaMLReadable, JavaMLWritable):
    def getVectors(self) -> DataFrame: ...
    @overload
    def findSynonyms(self, word: str, num: int) -> DataFrame: ...
    @overload
    def findSynonyms(self, word: Vector, num: int) -> DataFrame: ...
    @overload
    def findSynonymsArray(self, word: str, num: int) -> List[Tuple[str, float]]: ...
    @overload
    def findSynonymsArray(self, word: Vector, num: int) -> List[Tuple[str, float]]: ...

class PCA(JavaEstimator, HasInputCol, HasOutputCol, JavaMLReadable, JavaMLWritable):
    k = ...  # type: Param
    def __init__(
        self,
        *,
        k: Optional[int] = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        k: Optional[int] = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...
    ) -> PCA: ...
    def setK(self, value: int) -> PCA: ...
    def getK(self) -> int: ...

class PCAModel(JavaModel, JavaMLReadable, JavaMLWritable):
    @property
    def pc(self) -> DenseMatrix: ...
    @property
    def explainedVariance(self) -> DenseVector: ...

class RFormula(
    JavaEstimator,
    HasFeaturesCol,
    HasLabelCol,
    HasHandleInvalid,
    JavaMLReadable,
    JavaMLWritable,
):
    formula = ...  # type: Param
    forceIndexLabel = ...  # type: Param
    stringIndexerOrderType = ...  # type: Param
    handleInvalid = ...  # type: Param
    def __init__(
        self,
        *,
        formula: Optional[str] = ...,
        featuresCol: str = ...,
        labelCol: str = ...,
        forceIndexLabel: bool = ...,
        stringIndexerOrderType: str = ...,
        handleInvalid: str = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        formula: Optional[str] = ...,
        featuresCol: str = ...,
        labelCol: str = ...,
        forceIndexLabel: bool = ...,
        stringIndexerOrderType: str = ...,
        handleInvalid: str = ...
    ) -> RFormula: ...
    def setFormula(self, value: str) -> RFormula: ...
    def getFormula(self) -> str: ...
    def setForceIndexLabel(self, value: bool) -> RFormula: ...
    def getForceIndexLabel(self) -> bool: ...
    def setStringIndexerOrderType(self, value: str) -> RFormula: ...
    def getStringIndexerOrderType(self) -> str: ...

class RFormulaModel(JavaModel, JavaMLReadable, JavaMLWritable): ...

class ChiSqSelector(
    JavaEstimator,
    HasFeaturesCol,
    HasOutputCol,
    HasLabelCol,
    JavaMLReadable,
    JavaMLWritable,
):
    selectorType = ...  # type: Param
    numTopFeatures = ...  # type: Param
    percentile = ...  # type: Param
    fpr = ...  # type: Param
    fdr = ...  # type: Param
    fwe = ...  # type: Param
    def __init__(
        self,
        *,
        numTopFeatures: int = ...,
        featuresCol: str = ...,
        outputCol: Optional[str] = ...,
        labelCol: str = ...,
        selectorType: str = ...,
        percentile: float = ...,
        fpr: float = ...,
        fdr: float = ...,
        fwe: float = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        numTopFeatures: int = ...,
        featuresCol: str = ...,
        outputCol: Optional[str] = ...,
        labelCol: str = ...,
        selectorType: str = ...,
        percentile: float = ...,
        fpr: float = ...,
        fdr: float = ...,
        fwe: float = ...
    ): ...
    def setSelectorType(self, value: str) -> ChiSqSelector: ...
    def getSelectorType(self) -> str: ...
    def setNumTopFeatures(self, value: int) -> ChiSqSelector: ...
    def getNumTopFeatures(self) -> int: ...
    def setPercentile(self, value: float) -> ChiSqSelector: ...
    def getPercentile(self) -> float: ...
    def setFpr(self, value: float) -> ChiSqSelector: ...
    def getFpr(self) -> float: ...
    def setFdr(self, value: float) -> ChiSqSelector: ...
    def getFdr(self) -> float: ...
    def setFwe(self, value: float) -> ChiSqSelector: ...
    def getFwe(self) -> float: ...

class ChiSqSelectorModel(JavaModel, JavaMLReadable, JavaMLWritable):
    @property
    def selectedFeatures(self) -> List[int]: ...

class VectorSizeHint(
    JavaTransformer, HasInputCol, HasHandleInvalid, JavaMLReadable, JavaMLWritable
):
    size = ...  # type: Param
    handleInvalid = ...  # type: Param
    def __init__(
        self,
        *,
        inputCol: Optional[str] = ...,
        size: Optional[int] = ...,
        handleInvalid: str = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        inputCol: Optional[str] = ...,
        size: Optional[int] = ...,
        handleInvalid: str = ...
    ) -> VectorSizeHint: ...
    def setSize(self, value: int) -> VectorSizeHint: ...
    def getSize(self) -> int: ...
