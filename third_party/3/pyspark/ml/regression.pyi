# Stubs for pyspark.ml.regression (Python 3)

from typing import Any, List, Optional, Sequence
from pyspark.ml._typing import P

from pyspark.ml.param.shared import *
from pyspark.ml.linalg import Vector
from pyspark.ml.util import *
from pyspark.ml.wrapper import JavaEstimator, JavaModel, JavaWrapper
from pyspark.sql.dataframe import DataFrame

class LinearRegression(
    JavaEstimator[LinearRegressionModel],
    HasFeaturesCol,
    HasLabelCol,
    HasPredictionCol,
    HasMaxIter,
    HasRegParam,
    HasTol,
    HasElasticNetParam,
    HasFitIntercept,
    HasStandardization,
    HasSolver,
    HasWeightCol,
    HasAggregationDepth,
    JavaMLWritable,
    JavaMLReadable[LinearRegression],
):
    solver: Param[str]
    loss: Param[str]
    epsilon: Param[float]
    def __init__(
        self,
        *,
        featuresCol: str = ...,
        labelCol: str = ...,
        predictionCol: str = ...,
        maxIter: int = ...,
        regParam: float = ...,
        elasticNetParam: float = ...,
        tol: float = ...,
        fitIntercept: bool = ...,
        standardization: bool = ...,
        solver: str = ...,
        weightCol: Optional[str] = ...,
        aggregationDepth: int = ...,
        epsilon: float = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        featuresCol: str = ...,
        labelCol: str = ...,
        predictionCol: str = ...,
        maxIter: int = ...,
        regParam: float = ...,
        elasticNetParam: float = ...,
        tol: float = ...,
        fitIntercept: bool = ...,
        standardization: bool = ...,
        solver: str = ...,
        weightCol: Optional[str] = ...,
        aggregationDepth: int = ...,
        epsilon: float = ...
    ) -> LinearRegression: ...
    def setEpsilon(self, value: float) -> LinearRegression: ...
    def getEpsilon(self) -> float: ...

class LinearRegressionModel(
    JavaModel,
    JavaPredictionModel,
    GeneralJavaMLWritable,
    JavaMLReadable[LinearRegressionModel],
):
    @property
    def coefficients(self) -> Vector: ...
    @property
    def intercept(self) -> float: ...
    @property
    def summary(self) -> LinearRegressionTrainingSummary: ...
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

class IsotonicRegression(
    JavaEstimator[IsotonicRegressionModel],
    HasFeaturesCol,
    HasLabelCol,
    HasPredictionCol,
    HasWeightCol,
    JavaMLWritable,
    JavaMLReadable[IsotonicRegression],
):
    isotonic: Param[bool]
    featureIndex: Param[int]
    def __init__(
        self,
        *,
        featuresCol: str = ...,
        labelCol: str = ...,
        predictionCol: str = ...,
        weightCol: Optional[str] = ...,
        isotonic: bool = ...,
        featureIndex: int = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        featuresCol: str = ...,
        labelCol: str = ...,
        predictionCol: str = ...,
        weightCol: Optional[str] = ...,
        isotonic: bool = ...,
        featureIndex: int = ...
    ) -> IsotonicRegression: ...
    def setIsotonic(self, value: bool) -> IsotonicRegression: ...
    def getIsotonic(self) -> bool: ...
    def setFeatureIndex(self, value: int) -> IsotonicRegression: ...
    def getFeatureIndex(self) -> int: ...

class IsotonicRegressionModel(
    JavaModel, JavaMLWritable, JavaMLReadable[IsotonicRegressionModel]
):
    @property
    def boundaries(self) -> Vector: ...
    @property
    def predictions(self) -> Vector: ...

class TreeEnsembleParams(DecisionTreeParams):
    supportedFeatureSubsetStrategies: List[str]
    subsamplingRate: Param[float]
    featureSubsetStrategy: Param[str]
    def __init__(self) -> None: ...
    def setSubsamplingRate(self: P, value: float) -> P: ...
    def getSubsamplingRate(self) -> float: ...
    def setFeatureSubsetStrategy(self: P, value: str) -> P: ...
    def getFeatureSubsetStrategy(self) -> str: ...

class TreeRegressorParams(Params):
    supportedImpurities: List[str]
    impurity: Param[str]
    def __init__(self) -> None: ...
    def setImpurity(self: P, value: str) -> P: ...
    def getImpurity(self) -> str: ...

class RandomForestParams(TreeEnsembleParams):
    numTrees: Param[int]
    def __init__(self) -> None: ...
    def setNumTrees(self: P, value: int) -> P: ...
    def getNumTrees(self) -> int: ...

class GBTParams(TreeEnsembleParams):
    supportedLossTypes: List[str]

class DecisionTreeRegressor(
    JavaEstimator[DecisionTreeRegressionModel],
    HasFeaturesCol,
    HasLabelCol,
    HasPredictionCol,
    DecisionTreeParams,
    TreeRegressorParams,
    HasCheckpointInterval,
    HasSeed,
    JavaMLWritable,
    JavaMLReadable[DecisionTreeRegressor],
    HasVarianceCol,
):
    def __init__(
        self,
        *,
        featuresCol: str = ...,
        labelCol: str = ...,
        predictionCol: str = ...,
        maxDepth: int = ...,
        maxBins: int = ...,
        minInstancesPerNode: int = ...,
        minInfoGain: float = ...,
        maxMemoryInMB: int = ...,
        cacheNodeIds: bool = ...,
        checkpointInterval: int = ...,
        impurity: str = ...,
        seed: Optional[int] = ...,
        varianceCol: Optional[str] = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        featuresCol: str = ...,
        labelCol: str = ...,
        predictionCol: str = ...,
        maxDepth: int = ...,
        maxBins: int = ...,
        minInstancesPerNode: int = ...,
        minInfoGain: float = ...,
        maxMemoryInMB: int = ...,
        cacheNodeIds: bool = ...,
        checkpointInterval: int = ...,
        impurity: str = ...,
        seed: Optional[int] = ...,
        varianceCol: Optional[str] = ...
    ) -> DecisionTreeRegressor: ...

class DecisionTreeModel(JavaModel, JavaPredictionModel):
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

class DecisionTreeRegressionModel(
    DecisionTreeModel, JavaMLWritable, JavaMLReadable[DecisionTreeRegressionModel]
):
    @property
    def featureImportances(self) -> Vector: ...

class RandomForestRegressor(
    JavaEstimator[RandomForestRegressionModel],
    HasFeaturesCol,
    HasLabelCol,
    HasPredictionCol,
    HasSeed,
    RandomForestParams,
    TreeRegressorParams,
    HasCheckpointInterval,
    JavaMLWritable,
    JavaMLReadable[RandomForestRegressor],
):
    def __init__(
        self,
        *,
        featuresCol: str = ...,
        labelCol: str = ...,
        predictionCol: str = ...,
        maxDepth: int = ...,
        maxBins: int = ...,
        minInstancesPerNode: int = ...,
        minInfoGain: float = ...,
        maxMemoryInMB: int = ...,
        cacheNodeIds: bool = ...,
        checkpointInterval: int = ...,
        impurity: str = ...,
        subsamplingRate: float = ...,
        seed: Optional[int] = ...,
        numTrees: int = ...,
        featureSubsetStrategy: str = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        featuresCol: str = ...,
        labelCol: str = ...,
        predictionCol: str = ...,
        maxDepth: int = ...,
        maxBins: int = ...,
        minInstancesPerNode: int = ...,
        minInfoGain: float = ...,
        maxMemoryInMB: int = ...,
        cacheNodeIds: bool = ...,
        checkpointInterval: int = ...,
        impurity: str = ...,
        subsamplingRate: float = ...,
        seed: Optional[int] = ...,
        numTrees: int = ...,
        featureSubsetStrategy: str = ...
    ) -> RandomForestRegressor: ...
    def setFeatureSubsetStrategy(self, value: str) -> RandomForestRegressor: ...

class RandomForestRegressionModel(
    TreeEnsembleModel,
    JavaPredictionModel,
    JavaMLWritable,
    JavaMLReadable[RandomForestRegressionModel],
):
    @property
    def trees(self) -> Sequence[DecisionTreeRegressionModel]: ...
    @property
    def featureImportances(self) -> Vector: ...

class GBTRegressor(
    JavaEstimator[GBTRegressionModel],
    HasFeaturesCol,
    HasLabelCol,
    HasPredictionCol,
    HasMaxIter,
    GBTParams,
    HasCheckpointInterval,
    HasStepSize,
    HasSeed,
    JavaMLWritable,
    JavaMLReadable[GBTRegressor],
    TreeRegressorParams,
):
    lossType: Param
    def __init__(
        self,
        *,
        featuresCol: str = ...,
        labelCol: str = ...,
        predictionCol: str = ...,
        maxDepth: int = ...,
        maxBins: int = ...,
        minInstancesPerNode: int = ...,
        minInfoGain: float = ...,
        maxMemoryInMB: int = ...,
        cacheNodeIds: bool = ...,
        subsamplingRate: float = ...,
        checkpointInterval: int = ...,
        lossType: str = ...,
        maxIter: int = ...,
        stepSize: float = ...,
        seed: Optional[int] = ...,
        impurity: str = ...,
        featureSubsetStrategy: str = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        featuresCol: str = ...,
        labelCol: str = ...,
        predictionCol: str = ...,
        maxDepth: int = ...,
        maxBins: int = ...,
        minInstancesPerNode: int = ...,
        minInfoGain: float = ...,
        maxMemoryInMB: int = ...,
        cacheNodeIds: bool = ...,
        subsamplingRate: float = ...,
        checkpointInterval: int = ...,
        lossType: str = ...,
        maxIter: int = ...,
        stepSize: float = ...,
        seed: Optional[int] = ...,
        impuriy: str = ...,
        featureSubsetStrategy: str = ...
    ) -> GBTRegressor: ...
    def setLossType(self, value: str) -> GBTRegressor: ...
    def getLossType(self) -> str: ...
    def setFeatureSubsetStrategy(self, value: str) -> GBTRegressor: ...

class GBTRegressionModel(
    TreeEnsembleModel,
    JavaPredictionModel,
    JavaMLWritable,
    JavaMLReadable[GBTRegressionModel],
):
    @property
    def featureImportances(self) -> Vector: ...
    @property
    def trees(self) -> Sequence[DecisionTreeRegressionModel]: ...
    def evaluateEachIteration(self, dataset: DataFrame, loss: str) -> List[float]: ...

class AFTSurvivalRegression(
    JavaEstimator[AFTSurvivalRegressionModel],
    HasFeaturesCol,
    HasLabelCol,
    HasPredictionCol,
    HasFitIntercept,
    HasMaxIter,
    HasTol,
    HasAggregationDepth,
    JavaMLWritable,
    JavaMLReadable[AFTSurvivalRegression],
):
    censorCol: Param[str]
    quantileProbabilities: Param[List[float]]
    quantilesCol: Param[str]
    def __init__(
        self,
        *,
        featuresCol: str = ...,
        labelCol: str = ...,
        predictionCol: str = ...,
        fitIntercept: bool = ...,
        maxIter: int = ...,
        tol: float = ...,
        censorCol: str = ...,
        quantileProbabilities: List[float] = ...,
        quantilesCol: Optional[str] = ...,
        aggregationDepth: int = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        featuresCol: str = ...,
        labelCol: str = ...,
        predictionCol: str = ...,
        fitIntercept: bool = ...,
        maxIter: int = ...,
        tol: float = ...,
        censorCol: str = ...,
        quantileProbabilities: List[float] = ...,
        quantilesCol: Optional[str] = ...,
        aggregationDepth: int = ...
    ) -> AFTSurvivalRegression: ...
    def setCensorCol(self, value: str) -> AFTSurvivalRegression: ...
    def getCensorCol(self) -> str: ...
    def setQuantileProbabilities(self, value: List[float]) -> AFTSurvivalRegression: ...
    def getQuantileProbabilities(self) -> List[float]: ...
    def setQuantilesCol(self, value: str) -> AFTSurvivalRegression: ...
    def getQuantilesCol(self) -> str: ...

class AFTSurvivalRegressionModel(
    JavaModel, JavaMLWritable, JavaMLReadable[AFTSurvivalRegressionModel]
):
    @property
    def coefficients(self) -> Vector: ...
    @property
    def intercept(self) -> float: ...
    @property
    def scale(self) -> float: ...
    def predictQuantiles(self, features: Vector) -> Vector: ...
    def predict(self, features: Vector) -> float: ...

class GeneralizedLinearRegression(
    JavaEstimator[GeneralizedLinearRegressionModel],
    HasLabelCol,
    HasFeaturesCol,
    HasPredictionCol,
    HasFitIntercept,
    HasMaxIter,
    HasTol,
    HasRegParam,
    HasWeightCol,
    HasSolver,
    JavaMLWritable,
    JavaMLReadable[GeneralizedLinearRegression],
):
    family: Param[str]
    link: Param[str]
    linkPredictionCol: Param[str]
    variancePower: Param[float]
    linkPower: Param[float]
    solver: Param[str]
    offsetCol: Param[str]
    def __init__(
        self,
        *,
        labelCol: str = ...,
        featuresCol: str = ...,
        predictionCol: str = ...,
        family: str = ...,
        link: Optional[str] = ...,
        fitIntercept: bool = ...,
        maxIter: int = ...,
        tol: float = ...,
        regParam: float = ...,
        weightCol: Optional[str] = ...,
        solver: str = ...,
        linkPredictionCol: Optional[str] = ...,
        variancePower: float = ...,
        linkPower: Optional[float] = ...,
        offsetCol: Optional[str] = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        labelCol: str = ...,
        featuresCol: str = ...,
        predictionCol: str = ...,
        family: str = ...,
        link: Optional[str] = ...,
        fitIntercept: bool = ...,
        maxIter: int = ...,
        tol: float = ...,
        regParam: float = ...,
        weightCol: Optional[str] = ...,
        solver: str = ...,
        linkPredictionCol: Optional[str] = ...,
        variancePower: float = ...,
        linkPower: Optional[float] = ...,
        offsetCol: Optional[str] = ...
    ) -> GeneralizedLinearRegression: ...
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

class GeneralizedLinearRegressionModel(
    JavaModel,
    JavaPredictionModel,
    JavaMLWritable,
    JavaMLReadable[GeneralizedLinearRegressionModel],
):
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
