# Stubs for pyspark.ml.regression (Python 3)

from typing import Any, List, Optional, Sequence
from pyspark.ml._typing import P, T

from pyspark.ml.param.shared import *
from pyspark.ml.linalg import Vector
from pyspark.ml.util import *
from pyspark.ml.wrapper import JavaEstimator, JavaModel, JavaPredictionModel, JavaPredictor, JavaWrapper
from pyspark.sql.dataframe import DataFrame

class LinearRegression(JavaPredictor[LinearRegressionModel], HasMaxIter, HasRegParam, HasTol, HasElasticNetParam, HasFitIntercept, HasStandardization, HasSolver, HasWeightCol, HasAggregationDepth, HasLoss, JavaMLWritable, JavaMLReadable[LinearRegression]):
    def __init__(self, *, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., maxIter: int = ..., regParam: float = ..., elasticNetParam: float = ..., tol: float = ..., fitIntercept: bool = ..., standardization: bool = ..., solver: str = ..., weightCol: Optional[str] = ..., aggregationDepth: int = ...) -> None: ...
    def setParams(self, *, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., maxIter: int = ..., regParam: float = ..., elasticNetParam: float = ..., tol: float = ..., fitIntercept: bool = ..., standardization: bool = ..., solver: str = ..., weightCol: Optional[str] = ..., aggregationDepth: int = ...) -> LinearRegression: ...

class LinearRegressionModel(JavaPredictionModel[Vector], GeneralJavaMLWritable, JavaMLReadable[LinearRegressionModel], HasTrainingSummary[LinearRegressionSummary]):
    @property
    def coefficients(self) -> Vector: ...
    @property
    def intercept(self) -> float: ...
    @property
    def summary(self) -> LinearRegressionSummary: ...
    @property
    def hasSummary(self) -> bool: ...
    def evaluate(self, dataset: DataFrame) -> LinearRegressionSummary: ...

class LinearRegressionSummary(JavaWrapper):
    @property
    def predictions(self) -> DataFrame: ...
    @property
    def predictionCol(self) -> str: ...
    @property
    def labelCol(self) -> str: ...
    @property
    def featuresCol(self) -> str: ...
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
    @property
    def r2adj(self) -> float: ...
    @property
    def residuals(self) -> DataFrame: ...
    @property
    def numInstances(self) -> int: ...
    @property
    def devianceResiduals(self) -> List[float]: ...
    @property
    def coefficientStandardErrors(self) -> List[float]: ...
    @property
    def tValues(self) -> List[float]: ...
    @property
    def pValues(self) -> List[float]: ...

class LinearRegressionTrainingSummary(LinearRegressionSummary):
    @property
    def objectiveHistory(self) -> List[float]: ...
    @property
    def totalIterations(self) -> int: ...

class _IsotonicRegressionBase(HasFeaturesCol, HasLabelCol, HasPredictionCol, HasWeightCol):
    isotonic: Param[bool]
    featureIndex: Param[int]
    def getIsotonic(self) -> bool: ...
    def getFeatureIndex(self) -> int: ...

class IsotonicRegression(JavaEstimator[IsotonicRegressionModel], _IsotonicRegressionBase, HasWeightCol, JavaMLWritable, JavaMLReadable[IsotonicRegression]):
    def __init__(self, *, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., weightCol: Optional[str] = ..., isotonic: bool = ..., featureIndex: int = ...) -> None: ...
    def setParams(self, *, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., weightCol: Optional[str] = ..., isotonic: bool = ..., featureIndex: int = ...) -> IsotonicRegression: ...
    def setIsotonic(self, value: bool) -> IsotonicRegression: ...
    def setFeatureIndex(self, value: int) -> IsotonicRegression: ...

class IsotonicRegressionModel(JavaModel, _IsotonicRegressionBase, JavaMLWritable, JavaMLReadable[IsotonicRegressionModel]):
    @property
    def boundaries(self) -> Vector: ...
    @property
    def predictions(self) -> Vector: ...

class DecisionTreeParams(Params):
    leafCol: Param[str]
    maxDepth: Param[int]
    maxBins: Param[int]
    minInstancesPerNode: Param[int]
    minInfoGain: Param[float]
    maxMemoryInMB: Param[int]
    cacheNodeIds: Param[bool]
    def __init__(self) -> None: ...
    def setLeafCol(self: P, value: str) -> P: ...
    def getLeafCol(self) -> str: ...
    def setMaxDepth(self: P, value: int) -> P: ...
    def getMaxDepth(self) -> int: ...
    def setMaxBins(self: P, value: int) -> P: ...
    def getMaxBins(self) -> int: ...
    def setMinInstancesPerNode(self: P, value: int) -> P: ...
    def getMinInstancesPerNode(self) -> int: ...
    def setMinInfoGain(self: P, value: float) -> P: ...
    def getMinInfoGain(self) -> float: ...
    def setMaxMemoryInMB(self: P, value: int) -> P: ...
    def getMaxMemoryInMB(self) -> int: ...
    def setCacheNodeIds(self: P, value: bool) -> P: ...
    def getCacheNodeIds(self) -> bool: ...

class TreeEnsembleParams(DecisionTreeParams):
    supportedFeatureSubsetStrategies: List[str]
    subsamplingRate: Param[float]
    featureSubsetStrategy: Param[str]
    def __init__(self) -> None: ...
    def getSubsamplingRate(self) -> float: ...
    def getFeatureSubsetStrategy(self) -> str: ...

class HasVarianceImpurity(Params):
    supportedImpurities: List[str]
    impurity: Param[str]
    def __init__(self) -> None: ...
    def getImpurity(self) -> str: ...

class TreeRegressorParams(HasVarianceImpurity): ...

class RandomForestParams(TreeEnsembleParams):
    numTrees: Param[int]
    def __init__(self) -> None: ...
    def getNumTrees(self) -> int: ...

class GBTParams(TreeEnsembleParams, HasMaxIter, HasStepSize, HasValidationIndicatorCol):
    stepSize: Param[float]
    validationTol: Param[float]
    def getValidationTol(self) -> float: ...

class GBTRegressorParams(GBTParams, TreeRegressorParams):
    supportedLossTypes: List[str]
    lossType: Param[str]
    def getLossType(self) -> str: ...

class DecisionTreeRegressor(JavaPredictor[DecisionTreeRegressionModel], HasWeightCol, DecisionTreeParams, TreeRegressorParams, HasCheckpointInterval, HasSeed, JavaMLWritable, JavaMLReadable[DecisionTreeRegressor], HasVarianceCol):
    def __init__(self, *, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., maxDepth: int = ..., maxBins: int = ..., minInstancesPerNode: int = ..., minInfoGain: float = ..., maxMemoryInMB: int = ..., cacheNodeIds: bool = ..., checkpointInterval: int = ..., impurity: str = ..., seed: Optional[int] = ..., varianceCol: Optional[str] = ..., weightCol: Optional[str] = ..., leafCol: str = ...) -> None: ...
    def setParams(self, *, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., maxDepth: int = ..., maxBins: int = ..., minInstancesPerNode: int = ..., minInfoGain: float = ..., maxMemoryInMB: int = ..., cacheNodeIds: bool = ..., checkpointInterval: int = ..., impurity: str = ..., seed: Optional[int] = ..., varianceCol: Optional[str] = ..., weightCol: Optional[str] = ..., leafCol: str = ...) -> DecisionTreeRegressor: ...
    def setMaxDepth(self, value: int) -> DecisionTreeRegressor: ...
    def setMaxBins(self, value: int) -> DecisionTreeRegressor: ...
    def setMinInstancesPerNode(self, value: int) -> DecisionTreeRegressor: ...
    def setMinInfoGain(self, value: float) -> DecisionTreeRegressor: ...
    def setMaxMemoryInMB(self, value: int) -> DecisionTreeRegressor: ...
    def setCacheNodeIds(self, value: bool) -> DecisionTreeRegressor: ...
    def setImpurity(self, value: str) -> DecisionTreeRegressor: ...

class DecisionTreeModel(JavaPredictionModel[T]):
    @property
    def numNodes(self) -> int: ...
    @property
    def depth(self) -> int: ...
    @property
    def toDebugString(self) -> str: ...

class TreeEnsembleModel(JavaModel):
    @property
    def trees(self) -> Sequence[DecisionTreeModel]: ...
    @property
    def getNumTrees(self) -> int: ...
    @property
    def treeWeights(self) -> List[float]: ...
    @property
    def totalNumNodes(self) -> int: ...
    @property
    def toDebugString(self) -> str: ...

class DecisionTreeRegressionModel(DecisionTreeModel[T], JavaMLWritable, JavaMLReadable[DecisionTreeRegressionModel]):
    @property
    def featureImportances(self) -> Vector: ...

class RandomForestRegressor(JavaPredictor[RandomForestRegressionModel], HasSeed, RandomForestParams, TreeRegressorParams, HasCheckpointInterval, JavaMLWritable, JavaMLReadable[RandomForestRegressor]):
    def __init__(self, *, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., maxDepth: int = ..., maxBins: int = ..., minInstancesPerNode: int = ..., minInfoGain: float = ..., maxMemoryInMB: int = ..., cacheNodeIds: bool = ..., checkpointInterval: int = ..., impurity: str = ..., subsamplingRate: float = ..., seed: Optional[int] = ..., numTrees: int = ..., featureSubsetStrategy: str = ...) -> None: ...
    def setParams(self, *, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., maxDepth: int = ..., maxBins: int = ..., minInstancesPerNode: int = ..., minInfoGain: float = ..., maxMemoryInMB: int = ..., cacheNodeIds: bool = ..., checkpointInterval: int = ..., impurity: str = ..., subsamplingRate: float = ..., seed: Optional[int] = ..., numTrees: int = ..., featureSubsetStrategy: str = ...) -> RandomForestRegressor: ...
    def setFeatureSubsetStrategy(self, value: str) -> RandomForestRegressor: ...

class RandomForestRegressionModel(TreeEnsembleModel, JavaPredictionModel[Vector], JavaMLWritable, JavaMLReadable[RandomForestRegressionModel]):
    @property
    def trees(self) -> Sequence[DecisionTreeRegressionModel]: ...
    @property
    def featureImportances(self) -> Vector: ...

class GBTRegressor(JavaPredictor[GBTRegressionModel], GBTRegressorParams, HasCheckpointInterval, HasSeed, JavaMLWritable, JavaMLReadable[GBTRegressor]):
    def __init__(self, *, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., maxDepth: int = ..., maxBins: int = ..., minInstancesPerNode: int = ..., minInfoGain: float = ..., maxMemoryInMB: int = ..., cacheNodeIds: bool = ..., subsamplingRate: float = ..., checkpointInterval: int = ..., lossType: str = ..., maxIter: int = ..., stepSize: float = ..., seed: Optional[int] = ..., impurity: str = ..., featureSubsetStrategy: str = ..., validationTol: float = ..., validationIndicatorCol: Optional[str] = ..., leafCol: str = ...) -> None: ...
    def setParams(self, *, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., maxDepth: int = ..., maxBins: int = ..., minInstancesPerNode: int = ..., minInfoGain: float = ..., maxMemoryInMB: int = ..., cacheNodeIds: bool = ..., subsamplingRate: float = ..., checkpointInterval: int = ..., lossType: str = ..., maxIter: int = ..., stepSize: float = ..., seed: Optional[int] = ..., impuriy: str = ..., featureSubsetStrategy: str = ..., validationTol: float = ..., validationIndicatorCol: Optional[str] = ..., leafCol: str = ...) -> GBTRegressor: ...
    def setMaxDepth(self, value: int) -> GBTRegressor: ...
    def setMaxBins(self, value: int) -> GBTRegressor: ...
    def setMinInstancesPerNode(self, value: int) -> GBTRegressor: ...
    def setMinInfoGain(self, value: float) -> GBTRegressor: ...
    def setMaxMemoryInMB(self, value: int) -> GBTRegressor: ...
    def setCacheNodeIds(self, value: bool) -> GBTRegressor: ...
    def setImpurity(self, value: str) -> GBTRegressor: ...
    def setLossType(self, value: str) -> GBTRegressor: ...
    def setSubsamplingRate(self, value: float) -> GBTRegressor: ...
    def setFeatureSubsetStrategy(self, value: str) -> GBTRegressor: ...
    def setValidationIndicatorCol(self, value: str) -> GBTRegressor: ...

class GBTRegressionModel(TreeEnsembleModel, JavaPredictionModel[Vector], JavaMLWritable, JavaMLReadable[GBTRegressionModel]):
    @property
    def featureImportances(self) -> Vector: ...
    @property
    def trees(self) -> Sequence[DecisionTreeRegressionModel]: ...
    def evaluateEachIteration(self, dataset: DataFrame, loss: str) -> List[float]: ...

class AFTSurvivalRegression(JavaPredictor[AFTSurvivalRegressionModel], HasFitIntercept, HasMaxIter, HasTol, HasAggregationDepth, JavaMLWritable, JavaMLReadable[AFTSurvivalRegression]):
    censorCol: Param[str]
    quantileProbabilities: Param[List[float]]
    quantilesCol: Param[str]
    def __init__(self, *, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., fitIntercept: bool = ..., maxIter: int = ..., tol: float = ..., censorCol: str = ..., quantileProbabilities: List[float] = ..., quantilesCol: Optional[str] = ..., aggregationDepth: int = ...) -> None: ...
    def setParams(self, *, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., fitIntercept: bool = ..., maxIter: int = ..., tol: float = ..., censorCol: str = ..., quantileProbabilities: List[float] = ..., quantilesCol: Optional[str] = ..., aggregationDepth: int = ...) -> AFTSurvivalRegression: ...
    def setCensorCol(self, value: str) -> AFTSurvivalRegression: ...
    def getCensorCol(self) -> str: ...
    def setQuantileProbabilities(self, value: List[float]) -> AFTSurvivalRegression: ...
    def getQuantileProbabilities(self) -> List[float]: ...
    def setQuantilesCol(self, value: str) -> AFTSurvivalRegression: ...
    def getQuantilesCol(self) -> str: ...

class AFTSurvivalRegressionModel(JavaPredictionModel, JavaMLWritable, JavaMLReadable[AFTSurvivalRegressionModel]):
    @property
    def coefficients(self) -> Vector: ...
    @property
    def intercept(self) -> float: ...
    @property
    def scale(self) -> float: ...
    def predictQuantiles(self, features: Vector) -> Vector: ...
    def predict(self, features: Vector) -> float: ...

class GeneralizedLinearRegression(JavaPredictor[GeneralizedLinearRegressionModel], HasFitIntercept, HasMaxIter, HasTol, HasRegParam, HasWeightCol, HasSolver, JavaMLWritable, JavaMLReadable[GeneralizedLinearRegression]):
    family: Param[str]
    link: Param[str]
    linkPredictionCol: Param[str]
    variancePower: Param[float]
    linkPower: Param[float]
    solver: Param[str]
    offsetCol: Param[str]
    def __init__(self, *, labelCol: str = ..., featuresCol: str = ..., predictionCol: str = ..., family: str = ..., link: Optional[str] = ..., fitIntercept: bool = ..., maxIter: int = ..., tol: float = ..., regParam: float = ..., weightCol: Optional[str] = ..., solver: str = ..., linkPredictionCol: Optional[str] = ...,  variancePower: float = ..., linkPower: Optional[float] = ..., offsetCol: Optional[str] = ...) -> None: ...
    def setParams(self, *, labelCol: str = ..., featuresCol: str = ..., predictionCol: str = ..., family: str = ..., link: Optional[str] = ..., fitIntercept: bool = ..., maxIter: int = ..., tol: float = ..., regParam: float = ..., weightCol: Optional[str] = ..., solver: str = ..., linkPredictionCol: Optional[str] = ..., variancePower: float = ..., linkPower: Optional[float] = ..., offsetCol: Optional[str] = ...) -> GeneralizedLinearRegression: ...
    def setFamily(self, value: str) -> GeneralizedLinearRegression: ...
    def getFamily(self) -> str: ...
    def setLinkPredictionCol(self, value: str) -> GeneralizedLinearRegression: ...
    def getLinkPredictionCol(self) -> str: ...
    def setLink(self, value: str) -> GeneralizedLinearRegression: ...
    def getLink(self) -> str: ...
    def setVariancePower(self, value: float) -> GeneralizedLinearRegression: ...
    def getVariancePower(self) -> float: ...
    def setLinkPower(self, value: float) -> GeneralizedLinearRegression: ...
    def getLinkPower(self) -> float: ...
    def setOffsetCol(self, value: str) -> GeneralizedLinearRegression: ...
    def getOffsetCol(self) -> str: ...

class GeneralizedLinearRegressionModel(JavaPredictionModel[Vector], JavaMLWritable, JavaMLReadable[GeneralizedLinearRegressionModel], HasTrainingSummary[GeneralizedLinearRegressionTrainingSummary]):
    @property
    def coefficients(self) -> Vector: ...
    @property
    def intercept(self) -> float: ...
    @property
    def summary(self) -> GeneralizedLinearRegressionTrainingSummary: ...
    @property
    def hasSummary(self) -> bool: ...
    def evaluate(self, dataset: DataFrame) -> GeneralizedLinearRegressionSummary: ...

class GeneralizedLinearRegressionSummary(JavaWrapper):
    @property
    def predictions(self) -> DataFrame: ...
    @property
    def predictionCol(self) -> str: ...
    @property
    def rank(self) -> int: ...
    @property
    def degreesOfFreedom(self) -> int: ...
    @property
    def residualDegreeOfFreedom(self) -> int: ...
    @property
    def residualDegreeOfFreedomNull(self) -> int: ...
    def residuals(self, residualsType: str = ...) -> DataFrame: ...
    @property
    def nullDeviance(self) -> float: ...
    @property
    def deviance(self) -> float: ...
    @property
    def dispersion(self) -> float: ...
    @property
    def aic(self) -> float: ...

class GeneralizedLinearRegressionTrainingSummary(GeneralizedLinearRegressionSummary):
    @property
    def numIterations(self) -> int: ...
    @property
    def solver(self) -> str: ...
    @property
    def coefficientStandardErrors(self) -> List[float]: ...
    @property
    def tValues(self) -> List[float]: ...
    @property
    def pValues(self) -> List[float]: ...
