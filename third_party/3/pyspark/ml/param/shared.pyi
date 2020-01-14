# Stubs for pyspark.ml.param.shared (Python 3)

from typing import Any, Generic, List
from pyspark.ml._typing import T

from pyspark.ml.param import *

class HasMaxIter(Params):
    maxIter: Param[int]
    def __init__(self) -> None: ...
    def getMaxIter(self) -> int: ...

class HasRegParam(Params):
    regParam: Param[float]
    def __init__(self) -> None: ...
    def getRegParam(self) -> float: ...

class HasFeaturesCol(Params):
    featuresCol: Param[str]
    def __init__(self) -> None: ...
    def getFeaturesCol(self) -> str: ...

class HasLabelCol(Params):
    labelCol: Param[str]
    def __init__(self) -> None: ...
    def getLabelCol(self) -> str: ...

class HasPredictionCol(Params):
    predictionCol: Param[str]
    def __init__(self) -> None: ...
    def getPredictionCol(self) -> str: ...

class HasProbabilityCol(Params):
    probabilityCol: Param[str]
    def __init__(self) -> None: ...
    def getProbabilityCol(self) -> str: ...

class HasRawPredictionCol(Params):
    rawPredictionCol: Param[str]
    def __init__(self) -> None: ...
    def getRawPredictionCol(self) -> str: ...

class HasInputCol(Params):
    inputCol: Param[str]
    def __init__(self) -> None: ...
    def getInputCol(self) -> str: ...

class HasInputCols(Params):
    inputCols: Param[List[str]]
    def __init__(self) -> None: ...
    def getInputCols(self) -> List[str]: ...

class HasOutputCol(Params):
    outputCol: Param[str]
    def __init__(self) -> None: ...
    def getOutputCol(self) -> str: ...

class HasOutputCols(Params):
    outputCols: Param[List[str]]
    def __init__(self) -> None: ...
    def getOutputCols(self) -> List[str]: ...

class HasNumFeatures(Params):
    numFeatures: Param[int]
    def __init__(self) -> None: ...
    def getNumFeatures(self) -> int: ...

class HasCheckpointInterval(Params):
    checkpointInterval: Param[int]
    def __init__(self) -> None: ...
    def getCheckpointInterval(self) -> int: ...

class HasSeed(Params):
    seed: Param[int]
    def __init__(self) -> None: ...
    def getSeed(self) -> int: ...

class HasTol(Params):
    tol: Param[float]
    def __init__(self) -> None: ...
    def getTol(self) -> float: ...

class HasRelativeError(Params):
    relativeError: Param[float]
    def __init__(self) -> None: ...
    def getRelativeError(self) -> float: ...

class HasStepSize(Params):
    stepSize: Param[float]
    def __init__(self) -> None: ...
    def getStepSize(self) -> float: ...

class HasHandleInvalid(Params):
    handleInvalid: Param[str]
    def __init__(self) -> None: ...
    def getHandleInvalid(self) -> str: ...

class HasElasticNetParam(Params):
    elasticNetParam: Param[float]
    def __init__(self) -> None: ...
    def getElasticNetParam(self) -> float: ...

class HasFitIntercept(Params):
    fitIntercept: Param[bool]
    def __init__(self) -> None: ...
    def getFitIntercept(self) -> bool: ...

class HasStandardization(Params):
    standardization: Param[bool]
    def __init__(self) -> None: ...
    def getStandardization(self) -> bool: ...

class HasThresholds(Params):
    thresholds: Param[List[float]]
    def __init__(self) -> None: ...
    def getThresholds(self) -> List[float]: ...

class HasThreshold(Params):
    threshold: Param[float]
    def __init__(self) -> None: ...
    def getThreshold(self) -> float: ...

class HasWeightCol(Params):
    weightCol: Param[str]
    def __init__(self) -> None: ...
    def getWeightCol(self) -> str: ...

class HasSolver(Params):
    solver: Param[str]
    def __init__(self) -> None: ...
    def getSolver(self) -> str: ...

class HasVarianceCol(Params):
    varianceCol: Param[str]
    def __init__(self) -> None: ...
    def getVarianceCol(self) -> str: ...

class HasAggregationDepth(Params):
    aggregationDepth: Param[int]
    def __init__(self) -> None: ...
    def getAggregationDepth(self) -> int: ...

class HasParallelism(Params):
    parallelism: Param[int]
    def __init__(self) -> None: ...
    def getParallelism(self) -> int: ...

class HasCollectSubModels(Params):
    collectSubModels: Param[bool]
    def __init__(self) -> None: ...
    def getCollectSubModels(self) -> bool: ...

class HasLoss(Params):
    loss: Param[str]
    def __init__(self) -> None: ...
    def getLoss(self) -> str: ...

class HasValidationIndicatorCol(Params):
    validationIndicatorCol: Param[str]
    def __init__(self) -> None: ...
    def getValidationIndicatorCol(self) -> str: ...

class HasDistanceMeasure(Params):
    distanceMeasure: Param[str]
    def __init__(self) -> None: ...
    def getDistanceMeasure(self) -> str: ...
