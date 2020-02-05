# Stubs for pyspark.mllib.tree (Python 3.5)
#

from typing import overload
from typing import Any, Dict, Optional, Tuple
from pyspark.mllib._typing import VectorLike
from pyspark.rdd import RDD
from pyspark.mllib.common import JavaModelWrapper
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.util import JavaLoader, JavaSaveable

class TreeEnsembleModel(JavaModelWrapper, JavaSaveable):
    @overload
    def predict(self, x: VectorLike) -> float: ...
    @overload
    def predict(self, x: RDD[VectorLike]) -> RDD[VectorLike]: ...
    def numTrees(self) -> int: ...
    def totalNumNodes(self) -> int: ...
    def toDebugString(self) -> str: ...

class DecisionTreeModel(JavaModelWrapper, JavaSaveable, JavaLoader[DecisionTreeModel]):
    @overload
    def predict(self, x: VectorLike) -> float: ...
    @overload
    def predict(self, x: RDD[VectorLike]) -> RDD[VectorLike]: ...
    def numNodes(self) -> int: ...
    def depth(self) -> int: ...
    def toDebugString(self) -> str: ...

class DecisionTree:
    @classmethod
    def trainClassifier(
        cls,
        data: RDD[LabeledPoint],
        numClasses: int,
        categoricalFeaturesInfo: Dict[int, int],
        impurity: str = ...,
        maxDepth: int = ...,
        maxBins: int = ...,
        minInstancesPerNode: int = ...,
        minInfoGain: float = ...,
    ) -> DecisionTreeModel: ...
    @classmethod
    def trainRegressor(
        cls,
        data: RDD[LabeledPoint],
        categoricalFeaturesInfo: Dict[int, int],
        impurity: str = ...,
        maxDepth: int = ...,
        maxBins: int = ...,
        minInstancesPerNode: int = ...,
        minInfoGain: float = ...,
    ) -> DecisionTreeModel: ...

class RandomForestModel(TreeEnsembleModel, JavaLoader[RandomForestModel]): ...

class RandomForest:
    supportedFeatureSubsetStrategies: Tuple[str, ...]
    @classmethod
    def trainClassifier(
        cls,
        data: RDD[LabeledPoint],
        numClasses: int,
        categoricalFeaturesInfo: Dict[int, int],
        numTrees: int,
        featureSubsetStrategy: str = ...,
        impurity: str = ...,
        maxDepth: int = ...,
        maxBins: int = ...,
        seed: Optional[int] = ...,
    ) -> RandomForestModel: ...
    @classmethod
    def trainRegressor(
        cls,
        data: RDD[LabeledPoint],
        categoricalFeaturesInfo: Dict[int, int],
        numTrees: int,
        featureSubsetStrategy: str = ...,
        impurity: str = ...,
        maxDepth: int = ...,
        maxBins: int = ...,
        seed: Optional[int] = ...,
    ) -> RandomForestModel: ...

class GradientBoostedTreesModel(
    TreeEnsembleModel, JavaLoader[GradientBoostedTreesModel]
): ...

class GradientBoostedTrees:
    @classmethod
    def trainClassifier(
        cls,
        data: RDD[LabeledPoint],
        categoricalFeaturesInfo: Dict[int, int],
        loss: str = ...,
        numIterations: int = ...,
        learningRate: float = ...,
        maxDepth: int = ...,
        maxBins: int = ...,
    ) -> GradientBoostedTreesModel: ...
    @classmethod
    def trainRegressor(
        cls,
        data: RDD[LabeledPoint],
        categoricalFeaturesInfo: Dict[int, int],
        loss: str = ...,
        numIterations: int = ...,
        learningRate: float = ...,
        maxDepth: int = ...,
        maxBins: int = ...,
    ) -> GradientBoostedTreesModel: ...
