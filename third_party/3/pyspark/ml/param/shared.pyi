# Stubs for pyspark.ml.param.shared (Python 3.5)
#

from typing import Any, List
from pyspark.ml.param import *

class HasMaxIter(Params):
    maxIter = ...  # type: Param
    def __init__(self) -> None: ...
    def setMaxIter(self, value: int) -> HasMaxIter: ...
    def getMaxIter(self) -> int: ...

class HasRegParam(Params):
    regParam = ...  # type: Param
    def __init__(self) -> None: ...
    def setRegParam(self, value: float) -> HasRegParam: ...
    def getRegParam(self) -> float: ...

class HasFeaturesCol(Params):
    featuresCol = ...  # type: Param
    def __init__(self) -> None: ...
    def setFeaturesCol(self, value: str) -> HasFeaturesCol: ...
    def getFeaturesCol(self) -> str: ...

class HasLabelCol(Params):
    labelCol = ...  # type: Param
    def __init__(self) -> None: ...
    def setLabelCol(self, value: str) -> HasLabelCol: ...
    def getLabelCol(self) -> str: ...

class HasPredictionCol(Params):
    predictionCol = ...  # type: Param
    def __init__(self) -> None: ...
    def setPredictionCol(self, value: str) -> HasPredictionCol: ...
    def getPredictionCol(self) -> str: ...

class HasProbabilityCol(Params):
    probabilityCol = ...  # type: Param
    def __init__(self) -> None: ...
    def setProbabilityCol(self, value: str) -> HasProbabilityCol: ...
    def getProbabilityCol(self) -> str: ...

class HasRawPredictionCol(Params):
    rawPredictionCol = ...  # type: Param
    def __init__(self) -> None: ...
    def setRawPredictionCol(self, value: str) -> HasRawPredictionCol: ...
    def getRawPredictionCol(self) -> str: ...

class HasInputCol(Params):
    inputCol = ...  # type: Param
    def __init__(self) -> None: ...
    def setInputCol(self, value: str) -> HasInputCol: ...
    def getInputCol(self) -> str: ...

class HasInputCols(Params):
    inputCols = ...  # type: Param
    def __init__(self) -> None: ...
    def setInputCols(self, value: List[str]) -> HasInputCols: ...
    def getInputCols(self) -> List[str]: ...

class HasOutputCol(Params):
    outputCol = ...  # type: Param
    def __init__(self) -> None: ...
    def setOutputCol(self, value: str) -> HasOutputCol: ...
    def getOutputCol(self) -> str: ...

class HasOutputCols(Params):
    outputCols = ...  # type: Param
    def __init__(self) -> None: ...
    def setOutputCols(self, value: List[str]): ...
    def getOutputCols(self) -> List[str]: ...

class HasNumFeatures(Params):
    numFeatures = ...  # type: Param
    def __init__(self) -> None: ...
    def setNumFeatures(self, value: int) -> HasNumFeatures: ...
    def getNumFeatures(self) -> int: ...

class HasCheckpointInterval(Params):
    checkpointInterval = ...  # type: Param
    def __init__(self) -> None: ...
    def setCheckpointInterval(self, value: int) -> HasCheckpointInterval: ...
    def getCheckpointInterval(self) -> int: ...

class HasSeed(Params):
    seed = ...  # type: Param
    def __init__(self) -> None: ...
    def setSeed(self, value: int) -> HasSeed: ...
    def getSeed(self) -> int: ...

class HasTol(Params):
    tol = ...  # type: Param
    def __init__(self) -> None: ...
    def setTol(self, value: float) -> HasTol: ...
    def getTol(self) -> float: ...

class HasStepSize(Params):
    stepSize = ...  # type: Param
    def __init__(self) -> None: ...
    def setStepSize(self, value: float) -> HasStepSize: ...
    def getStepSize(self) -> float: ...

class HasHandleInvalid(Params):
    handleInvalid = ...  # type: Param
    def __init__(self) -> None: ...
    def setHandleInvalid(self, value: str) -> HasHandleInvalid: ...
    def getHandleInvalid(self) -> str: ...

class HasElasticNetParam(Params):
    elasticNetParam = ...  # type: Param
    def __init__(self) -> None: ...
    def setElasticNetParam(self, value: float) -> HasElasticNetParam: ...
    def getElasticNetParam(self) -> float: ...

class HasFitIntercept(Params):
    fitIntercept = ...  # type: Param
    def __init__(self) -> None: ...
    def setFitIntercept(self, value: bool) -> HasFitIntercept: ...
    def getFitIntercept(self) -> bool: ...

class HasStandardization(Params):
    standardization = ...  # type: Param
    def __init__(self) -> None: ...
    def setStandardization(self, value: bool) -> HasStandardization: ...
    def getStandardization(self) -> bool: ...

class HasThresholds(Params):
    thresholds = ...  # type: Param
    def __init__(self) -> None: ...
    def setThresholds(self, value: List[float]) -> HasThresholds: ...
    def getThresholds(self) -> List[float]: ...

class HasThreshold(Params):
    threshold = ...  # type: Param
    def __init__(self) -> None: ...
    def setThreshold(self, value: float) -> HasThreshold: ...
    def getThreshold(self) -> float: ...

class HasWeightCol(Params):
    weightCol = ...  # type: Param
    def __init__(self) -> None: ...
    def setWeightCol(self, value: str) -> HasWeightCol: ...
    def getWeightCol(self) -> str: ...

class HasSolver(Params):
    solver = ...  # type: Param
    def __init__(self) -> None: ...
    def setSolver(self, value: str) -> HasSolver: ...
    def getSolver(self) -> str: ...

class HasVarianceCol(Params):
    varianceCol = ...  # type: Param
    def __init__(self) -> None: ...
    def setVarianceCol(self, value: str) -> HasVarianceCol: ...
    def getVarianceCol(self) -> str: ...

class HasAggregationDepth(Params):
    aggregationDepth = ...  # type: Param
    def __init__(self) -> None: ...
    def setAggregationDepth(self, value: int) -> HasAggregationDepth: ...
    def getAggregationDepth(self) -> int: ...

class HasParallelism(Params):
    parallelism = ...  # type: Param
    def __init__(self) -> None: ...
    def setParallelism(self, value: int) -> HasParallelism: ...
    def getParallelism(self) -> int: ...

class HasCollectSubModels(Params):
    collectSubModels = ... # type: Param
    def __init__(self) -> None: ...
    def setCollectSubModels(self, value: bool) -> HasCollectSubModels: ...
    def getCollectSubModels(self) -> bool: ...

class HasLoss(Params):
    loss = ...  # type: Param
    def __init__(self) -> None: ...
    def setLoss(self, value: str) -> HasLoss: ...
    def getLoss(self) -> str: ...

class DecisionTreeParams(Params):
    maxDepth = ...  # type: Param
    maxBins = ...  # type: Param
    minInstancesPerNode = ...  # type: Param
    minInfoGain = ...  # type: Param
    maxMemoryInMB = ...  # type: Param
    cacheNodeIds = ...  # type: Param
    def __init__(self) -> None: ...
    def setMaxDepth(self, value: int) -> DecisionTreeParams: ...
    def getMaxDepth(self) -> int: ...
    def setMaxBins(self, value: int) -> DecisionTreeParams: ...
    def getMaxBins(self) -> int: ...
    def setMinInstancesPerNode(self, value: int) -> DecisionTreeParams: ...
    def getMinInstancesPerNode(self) -> int: ...
    def setMinInfoGain(self, value: float) -> DecisionTreeParams: ...
    def getMinInfoGain(self) -> float: ...
    def setMaxMemoryInMB(self, value: int) -> DecisionTreeParams: ...
    def getMaxMemoryInMB(self) -> int: ...
    def setCacheNodeIds(self, value: bool) -> DecisionTreeParams: ...
    def getCacheNodeIds(self) -> bool: ...
