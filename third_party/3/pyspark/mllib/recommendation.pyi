# Stubs for pyspark.mllib.recommendation (Python 3.5)
#

from typing import Any, List, Optional, Tuple, Union

import array
from collections import namedtuple

from pyspark.context import SparkContext
from pyspark.rdd import RDD
from pyspark.mllib.common import JavaModelWrapper
from pyspark.mllib.util import JavaLoader, JavaSaveable

class Rating(namedtuple("Rating", ["user", "product", "rating"])):
    def __reduce__(self): ...

class MatrixFactorizationModel(
    JavaModelWrapper, JavaSaveable, JavaLoader[MatrixFactorizationModel]
):
    def predict(self, user: int, product: int) -> float: ...
    def predictAll(self, user_product: RDD[Tuple[int, int]]) -> RDD[Rating]: ...
    def userFeatures(self) -> RDD[Tuple[int, array.array]]: ...
    def productFeatures(self) -> RDD[Tuple[int, array.array]]: ...
    def recommendUsers(self, product: int, num: int) -> List[Rating]: ...
    def recommendProducts(self, user: int, num: int) -> List[Rating]: ...
    def recommendProductsForUsers(
        self, num: int
    ) -> RDD[Tuple[int, Tuple[Rating, ...]]]: ...
    def recommendUsersForProducts(
        self, num: int
    ) -> RDD[Tuple[int, Tuple[Rating, ...]]]: ...
    @property
    def rank(self) -> int: ...
    @classmethod
    def load(cls, sc: SparkContext, path: str) -> MatrixFactorizationModel: ...

class ALS:
    @classmethod
    def train(
        cls,
        ratings: Union[RDD[Rating], RDD[Tuple[int, int, float]]],
        rank: int,
        iterations: int = ...,
        lambda_: float = ...,
        blocks: int = ...,
        nonnegative: bool = ...,
        seed: Optional[int] = ...,
    ) -> MatrixFactorizationModel: ...
    @classmethod
    def trainImplicit(
        cls,
        ratings: Union[RDD[Rating], RDD[Tuple[int, int, float]]],
        rank: int,
        iterations: int = ...,
        lambda_: float = ...,
        blocks: int = ...,
        alpha: float = ...,
        nonnegative: bool = ...,
        seed: Optional[int] = ...,
    ) -> MatrixFactorizationModel: ...
