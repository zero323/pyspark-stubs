# Stubs for pyspark.ml.classification (Python 3)

import abc
from typing import Any, Dict, List, Optional, TypeVar
from pyspark.ml._typing import JM, M, P, T, ParamMap

from pyspark.ml.base import Estimator, Model, Transformer
from pyspark.ml.linalg import Matrix, Vector
from pyspark.ml.param.shared import *
from pyspark.ml.tree import _DecisionTreeModel, _DecisionTreeParams, _TreeEnsembleModel, _RandomForestParams, _GBTParams, _HasVarianceImpurity, _TreeClassifierParams, _TreeEnsembleParams
from pyspark.ml.regression import DecisionTreeRegressionModel
from pyspark.ml.util import *
from pyspark.ml.wrapper import JavaPredictionModel, JavaPredictor, JavaPredictorParams, JavaWrapper, JavaTransformer
from pyspark.sql.dataframe import DataFrame

class JavaClassifierParams(HasRawPredictionCol, JavaPredictorParams): ...

class JavaClassifier(JavaPredictor[JM], JavaClassifierParams, metaclass=abc.ABCMeta):
    def setRawPredictionCol(self: P, value: str) -> P: ...

class JavaClassificationModel(JavaPredictionModel[T], JavaClassifierParams):
    def setRawPredictionCol(self: P, value: str) -> P: ...
    @property
    def numClasses(self) -> int: ...

class JavaProbabilisticClassifierParams(HasProbabilityCol, HasThresholds, JavaClassifierParams): ...

class JavaProbabilisticClassifier(JavaClassifier[JM], JavaProbabilisticClassifierParams, metaclass=abc.ABCMeta):
    def setProbabilityCol(self: P, value: str) -> P: ...
    def setThresholds(self: P, value: List[float]) -> P: ...

class JavaProbabilisticClassificationModel(JavaClassificationModel[T], JavaProbabilisticClassifierParams):
    def setProbabilityCol(self: P, value: str) -> P: ...
    def setThresholds(self, value: List[float]) -> P: ...

class LinearSVC(JavaClassifier[LinearSVCModel], HasMaxIter, HasRegParam, HasTol, HasFitIntercept, HasStandardization, HasWeightCol, HasAggregationDepth, HasThreshold, JavaMLWritable, JavaMLReadable[LinearSVC]):
    def __init__(self, *, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., maxIter: int = ..., regParam: float = ..., tol: float = ..., rawPredictionCol: str = ..., fitIntercept: bool = ..., standardization: bool = ..., threshold: float = ..., weightCol: Optional[str] = ..., aggregationDepth: int = ...) -> None: ...
    def setParams(self, *, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., maxIter: int = ..., regParam: float = ..., tol: float = ..., rawPredictionCol: str = ..., fitIntercept: bool = ..., standardization: bool = ..., threshold: float = ..., weightCol: Optional[str] = ..., aggregationDepth: int = ...) -> LinearSVC: ...

class LinearSVCModel(JavaClassificationModel[Vector], JavaMLWritable, JavaMLReadable[LinearSVCModel]):
    @property
    def coefficients(self) -> Vector: ...
    @property
    def intercept(self) -> float: ...

class LogisticRegression(JavaProbabilisticClassifier[LogisticRegressionModel], HasMaxIter, HasRegParam, HasTol, HasElasticNetParam, HasFitIntercept, HasStandardization, HasThresholds, HasWeightCol, HasAggregationDepth, JavaMLWritable, JavaMLReadable[LogisticRegression]):
    threshold: Param[float]
    family: Param[str]
    lowerBoundsOnCoefficients: Param[Matrix]
    upperBoundsOnCoefficients: Param[Matrix]
    lowerBoundsOnIntercepts: Param[Vector]
    upperBoundsOnIntercepts: Param[Vector]
    def __init__(self, *, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., maxIter: int = ..., regParam: float = ..., elasticNetParam: float = ..., tol: float = ..., fitIntercept: bool = ..., threshold: float = ..., thresholds: Optional[List[float]] = ..., probabilityCol: str = ..., rawPredictionCol: str = ..., standardization: bool = ..., weightCol: Optional[str] = ..., aggregationDepth: int = ..., family: str = ..., lowerBoundsOnCoefficients: Optional[Matrix] = ..., upperBoundsOnCoefficients: Optional[Matrix] = ..., lowerBoundsOnIntercepts: Optional[Vector] = ..., upperBoundsOnIntercepts: Optional[Vector] = ...) -> None: ...
    def setParams(self, *, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., maxIter: int = ..., regParam: float = ..., elasticNetParam: float = ..., tol: float = ..., fitIntercept: bool = ..., threshold: float = ..., thresholds: Optional[List[float]] = ..., probabilityCol: str = ..., rawPredictionCol: str = ..., standardization: bool = ..., weightCol: Optional[str] = ..., aggregationDepth: int = ..., family: str = ..., lowerBoundsOnCoefficients: Optional[Matrix] = ..., upperBoundsOnCoefficients: Optional[Matrix] = ..., lowerBoundsOnIntercepts: Optional[Vector] = ..., upperBoundsOnIntercepts: Optional[Vector] = ...) -> LogisticRegression: ...
    def setThreshold(self, value: float) -> LogisticRegression: ...
    def getThreshold(self) -> float: ...
    def setThresholds(self, value: List[float]) -> LogisticRegression: ...
    def getThresholds(self) -> List[float]: ...
    def setFamily(self, value: str) -> LogisticRegression: ...
    def getFamily(self) -> str: ...
    def setLowerBoundsOnCoefficients(self, value: Matrix) -> LogisticRegression: ...
    def getLowerBoundsOnCoefficients(self) -> Matrix : ...
    def setUpperBoundsOnCoefficients(self, value: Matrix) -> LogisticRegression: ...
    def getUpperBoundsOnCoefficients(self) -> Matrix: ...
    def setLowerBoundsOnIntercepts(self, value: Vector) -> LogisticRegression: ...
    def getLowerBoundsOnIntercepts(self) -> Vector: ...
    def setUpperBoundsOnIntercepts(self, value: Vector) -> LogisticRegression: ...
    def getUpperBoundsOnIntercepts(self) -> Vector: ...

class LogisticRegressionModel(JavaProbabilisticClassificationModel[Vector], JavaMLWritable, JavaMLReadable[LogisticRegressionModel], HasTrainingSummary[LogisticRegressionTrainingSummary]):
    @property
    def coefficients(self) -> Vector: ...
    @property
    def intercept(self) -> float: ...
    @property
    def coefficientMatrix(self) -> Matrix: ...
    @property
    def interceptVector(self) -> Vector: ...
    @property
    def summary(self) -> LogisticRegressionTrainingSummary: ...
    @property
    def hasSummary(self) -> bool: ...
    def evaluate(self, dataset: DataFrame) -> LogisticRegressionSummary: ...

class LogisticRegressionSummary(JavaWrapper):
    @property
    def predictions(self) -> DataFrame: ...
    @property
    def probabilityCol(self) -> str: ...
    @property
    def predictionCol(self) -> str: ...
    @property
    def labelCol(self) -> str: ...
    @property
    def featuresCol(self) -> str: ...
    @property
    def labels(self) -> List[float]: ...
    @property
    def truePositiveRateByLabel(self) -> List[float]: ...
    @property
    def falsePositiveRateByLabel(self) -> List[float]: ...
    @property
    def precisionByLabel(self) -> List[float]: ...
    @property
    def recallByLabel(self) -> List[float]: ...
    def fMeasureByLabel(self, beta: float = ...) -> List[float]: ...
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
    def weightedFMeasure(self, beta: float = ...) -> float: ...

class LogisticRegressionTrainingSummary(LogisticRegressionSummary):
    @property
    def objectiveHistory(self) -> List[float]: ...
    @property
    def totalIterations(self) -> int: ...

class BinaryLogisticRegressionSummary(LogisticRegressionSummary):
    @property
    def roc(self) -> DataFrame: ...
    @property
    def areaUnderROC(self) -> float: ...
    @property
    def pr(self) -> DataFrame: ...
    @property
    def fMeasureByThreshold(self) -> DataFrame: ...
    @property
    def precisionByThreshold(self) -> DataFrame: ...
    @property
    def recallByThreshold(self) -> DataFrame: ...

class BinaryLogisticRegressionTrainingSummary(BinaryLogisticRegressionSummary, LogisticRegressionTrainingSummary): ...

class _DecisionTreeClassifierParams(_DecisionTreeParams, _TreeClassifierParams): ...

class DecisionTreeClassifier(JavaProbabilisticClassifier[DecisionTreeClassificationModel], _DecisionTreeClassifierParams, JavaMLWritable, JavaMLReadable[DecisionTreeClassifier]):
    def __init__(self, *, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., probabilityCol: str = ..., rawPredictionCol: str = ..., maxDepth: int = ..., maxBins: int = ..., minInstancesPerNode: int = ..., minInfoGain: float = ..., maxMemoryInMB: int = ..., cacheNodeIds: bool = ..., checkpointInterval: int = ..., impurity: str = ..., seed: Optional[int] = ..., weightCol: Optional[str] = ..., leafCol: str = ..., minWeightFractionPerNode: float = ...) -> None: ...
    def setParams(self, *, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., probabilityCol: str = ..., rawPredictionCol: str = ..., maxDepth: int = ..., maxBins: int = ..., minInstancesPerNode: int = ..., minInfoGain: float = ..., maxMemoryInMB: int = ..., cacheNodeIds: bool = ..., checkpointInterval: int = ..., impurity: str = ..., seed: Optional[int] = ..., weightCol: Optional[str] = ..., leafCol: str = ..., minWeightFractionPerNode: float = ...) -> DecisionTreeClassifier: ...
    def setMaxDepth(self, value: int) -> DecisionTreeClassifier: ...
    def setMaxBins(self, value: int) -> DecisionTreeClassifier: ...
    def setMinInstancesPerNode(self, value: int) -> DecisionTreeClassifier: ...
    def setMinWeightFractionPerNode(self, value: float) -> DecisionTreeClassifier: ...
    def setMinInfoGain(self, value: float) -> DecisionTreeClassifier: ...
    def setMaxMemoryInMB(self, value: int) -> DecisionTreeClassifier: ...
    def setCacheNodeIds(self, value: bool) -> DecisionTreeClassifier: ...
    def setImpurity(self, value: str) -> DecisionTreeClassifier: ...

class DecisionTreeClassificationModel(_DecisionTreeModel, JavaProbabilisticClassificationModel[Vector], _DecisionTreeClassifierParams, JavaMLWritable, JavaMLReadable[DecisionTreeClassificationModel]):
    @property
    def featureImportances(self) -> Vector: ...

class _RandomForestClassifierParams(_RandomForestParams, _TreeClassifierParams): ...

class RandomForestClassifier(JavaProbabilisticClassifier[RandomForestClassificationModel], _RandomForestClassifierParams, JavaMLWritable, JavaMLReadable[RandomForestClassifier]):
    def __init__(self, *, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., probabilityCol: str = ..., rawPredictionCol: str = ..., maxDepth: int = ..., maxBins: int = ..., minInstancesPerNode: int = ..., minInfoGain: float = ..., maxMemoryInMB: int = ..., cacheNodeIds: bool = ..., checkpointInterval: int = ..., impurity: str = ..., numTrees: int = ..., featureSubsetStrategy: str = ..., seed: Optional[int] = ..., subsamplingRate: float = ..., leafCol: str = ..., minWeightFractionPerNode: float = ...) -> None: ...
    def setParams(self, *, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., probabilityCol: str = ..., rawPredictionCol: str = ..., maxDepth: int = ..., maxBins: int = ..., minInstancesPerNode: int = ..., minInfoGain: float = ..., maxMemoryInMB: int = ..., cacheNodeIds: bool = ..., checkpointInterval: int = ..., seed: Optional[int] = ..., impurity: str = ..., numTrees: int = ..., featureSubsetStrategy: str = ..., subsamplingRate: float = ..., leafCol: str = ..., minWeightFractionPerNode: float = ...) -> RandomForestClassifier: ...
    def setMaxDepth(self, value: int) -> RandomForestClassifier: ...
    def setMaxBins(self, value: int) -> RandomForestClassifier: ...
    def setMinInstancesPerNode(self, value: int) -> RandomForestClassifier: ...
    def setMinInfoGain(self, value: float) -> RandomForestClassifier: ...
    def setMaxMemoryInMB(self, value: int) -> RandomForestClassifier: ...
    def setCacheNodeIds(self, value: bool) -> RandomForestClassifier: ...
    def setImpurity(self, value: str) -> RandomForestClassifier: ...
    def setNumTrees(self, value: int) -> RandomForestClassifier: ...
    def setSubsamplingRate(self, value: float) -> RandomForestClassifier: ...
    def setFeatureSubsetStrategy(self, value: str) -> RandomForestClassifier: ...

class RandomForestClassificationModel(_TreeEnsembleModel, JavaProbabilisticClassificationModel[Vector],  _RandomForestClassifierParams, JavaMLWritable, JavaMLReadable[RandomForestClassificationModel]):
    @property
    def featureImportances(self) -> Vector: ...
    @property
    def trees(self) -> List[DecisionTreeClassificationModel]: ...

class GBTClassifierParams(_GBTParams, _HasVarianceImpurity):
    supportedLossTypes: List[str]
    lossType: Param[str]
    def getLossType(self) -> str: ...

class GBTClassifier(JavaProbabilisticClassifier[GBTClassificationModel], GBTClassifierParams, JavaMLWritable, JavaMLReadable[GBTClassifier]):
    def __init__(self, *, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., maxDepth: int = ..., maxBins: int = ..., minInstancesPerNode: int = ..., minInfoGain: float = ..., maxMemoryInMB: int = ..., cacheNodeIds: bool = ..., checkpointInterval: int = ..., lossType: str = ..., maxIter: int = ..., stepSize: float = ..., seed: Optional[int] = ..., subsamplingRate: float = ..., featureSubsetStrategy: str = ...,  validationTol: float = ..., validationIndicatorCol: Optional[str] = ..., leafCol: str = ..., minWeightFractionPerNode: float = ...) -> None: ...
    def setParams(self, *, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., maxDepth: int = ..., maxBins: int = ..., minInstancesPerNode: int = ..., minInfoGain: float = ..., maxMemoryInMB: int = ..., cacheNodeIds: bool = ..., checkpointInterval: int = ..., lossType: str = ..., maxIter: int = ..., stepSize: float = ..., seed: Optional[int] = ..., subsamplingRate: float = ..., featureSubsetStrategy: str = ..., validationTol: float = ..., validationIndicatorCol: Optional[str] = ..., leafCol: str = ..., minWeightFractionPerNode: float = ...) -> GBTClassifier: ...
    def setMaxDepth(self, value: int) -> GBTClassifier: ...
    def setMaxBins(self, value: int) -> GBTClassifier: ...
    def setMinInstancesPerNode(self, value: int) -> GBTClassifier: ...
    def setMinInfoGain(self, value: float) -> GBTClassifier: ...
    def setMaxMemoryInMB(self, value: int) -> GBTClassifier: ...
    def setCacheNodeIds(self, value: bool) -> GBTClassifier: ...
    def setImpurity(self, value: str) -> GBTClassifier: ...
    def setLossType(self, value: str) -> GBTClassifier: ...
    def setSubsamplingRate(self, value: float) -> GBTClassifier: ...
    def setFeatureSubsetStrategy(self, value: str) -> GBTClassifier: ...
    def setValidationIndicatorCol(self, value: str) -> GBTClassifier: ...

class GBTClassificationModel(_TreeEnsembleModel, JavaProbabilisticClassificationModel[Vector], GBTClassifierParams, JavaMLWritable, JavaMLReadable[GBTClassificationModel]):
    @property
    def featureImportances(self) -> Vector: ...
    @property
    def trees(self) -> List[DecisionTreeRegressionModel]: ...
    def evaluateEachIteration(self, dataset: DataFrame) -> List[float]: ...

class NaiveBayes(JavaProbabilisticClassifier[NaiveBayesModel], HasThresholds, HasWeightCol, JavaMLWritable, JavaMLReadable[NaiveBayes]):
    smoothing: Param[float]
    modelType: Param[str]
    def __init__(self, *, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., probabilityCol: str = ..., rawPredictionCol: str = ..., smoothing: float = ..., modelType: str = ..., thresholds: Optional[List[float]] = ..., weightCol: Optional[str] = ...) -> None: ...
    def setParams(self, *, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., probabilityCol: str = ..., rawPredictionCol: str = ..., smoothing: float = ..., modelType: str = ..., thresholds: Optional[List[float]] = ..., weightCol: Optional[str] = ...) -> NaiveBayes: ...
    def setSmoothing(self, value: float) -> NaiveBayes: ...
    def getSmoothing(self) -> float: ...
    def setModelType(self, value: str) -> NaiveBayes: ...
    def getModelType(self) -> str: ...

class NaiveBayesModel(JavaProbabilisticClassificationModel[Vector], JavaMLWritable, JavaMLReadable[NaiveBayesModel]):
    @property
    def pi(self) -> Vector: ...
    @property
    def theta(self) -> Matrix: ...

class MultilayerPerceptronClassifier(JavaProbabilisticClassifier[MultilayerPerceptronClassificationModel], HasMaxIter, HasTol, HasSeed, HasStepSize, HasSolver, JavaMLWritable, JavaMLReadable[MultilayerPerceptronClassifier]):
    layers: Param[List[int]]
    blockSize: Param[int]
    solver: Param[str]
    initialWeights: Param[Vector]
    def __init__(self, *, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., maxIter: int = ..., tol: float = ..., seed: Optional[int] = ..., layers: Optional[List[int]] = ..., blockSize: int = ..., stepSize: float = ..., solver: str = ..., initialWeights: Optional[Vector] = ..., probabilityCol: str = ..., rawPredictionCol: str = ...) -> None: ...
    def setParams(self, *, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., maxIter: int = ..., tol: float = ..., seed: Optional[int] = ..., layers: Optional[List[int]] = ..., blockSize: int = ..., stepSize: float = ..., solver: str = ..., initialWeights: Optional[Vector] = ..., probabilityCol: str = ..., rawPredictionCol: str = ...) -> MultilayerPerceptronClassifier: ...
    def setLayers(self, value: List[int]) -> MultilayerPerceptronClassifier: ...
    def getLayers(self) -> List[int]: ...
    def setBlockSize(self, value: int) -> MultilayerPerceptronClassifier: ...
    def getBlockSize(self) -> int: ...
    def setStepSize(self, value: float) -> MultilayerPerceptronClassifier: ...
    def getStepSize(self) -> float: ...
    def setInitialWeights(self, value: Vector) -> MultilayerPerceptronClassifier: ...
    def getInitialWeights(self) -> Vector: ...

class MultilayerPerceptronClassificationModel(JavaProbabilisticClassificationModel[Vector], JavaMLWritable, JavaMLReadable[MultilayerPerceptronClassificationModel]):
    @property
    def layers(self) -> List[int]: ...
    @property
    def weights(self) -> Vector: ...

class OneVsRestParams(JavaClassifierParams, HasWeightCol):
    classifier: Param[Estimator]
    def getClassifier(self) -> Estimator[M]: ...

class OneVsRest(Estimator[OneVsRestModel], OneVsRestParams, HasParallelism, JavaMLReadable[OneVsRest], JavaMLWritable):
    def __init__(self, *, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., rawPredictionCol: str = ..., classifier: Optional[Estimator[M]] = ..., weightCol: Optional[str] = ..., parallelism: int = ...) -> None: ...
    def setParams(self, *, featuresCol: Optional[str] = ..., labelCol: Optional[str] = ..., predictionCol: Optional[str] = ..., rawPredictionCol: str = ..., classifier: Optional[Estimator[M]] = ..., weightCol: Optional[str] = ..., parallelism: int = ...) -> OneVsRest: ...
    def setClassifier(self, value: Estimator[M]) -> OneVsRest: ...
    def copy(self, extra: Optional[ParamMap] = ...) -> OneVsRest: ...

class OneVsRestModel(Model, OneVsRestParams, JavaMLReadable[OneVsRestModel], JavaMLWritable):
    models: List[Transformer]
    def __init__(self, models: List[Transformer]) -> None: ...
    def setClassifier(self, value: Estimator[M]) -> OneVsRest: ...
    def copy(self, extra: Optional[ParamMap] = ...) -> OneVsRestModel: ...
