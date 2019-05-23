# Stubs for pyspark.sql.dataframe (Python 3.5)
#

from typing import Any, Callable, Dict, Iterator, List, Optional, Tuple, TypeVar, Union
from typing import overload

import pandas.core.frame # type: ignore
from py4j.java_gateway import JavaObject  # type: ignore

from pyspark.sql._typing import ColumnOrName, LiteralType
from pyspark.sql.types import *
from pyspark.sql.context import SQLContext
from pyspark.sql.group import GroupedData
from pyspark.sql.readwriter import DataFrameWriter
from pyspark.sql.streaming import DataStreamWriter
from pyspark.sql.column import Column
from pyspark.rdd import RDD
from pyspark.storagelevel import StorageLevel

class DataFrame:
    sql_ctx = ...  # type: SQLContext
    is_cached = ...  # type: bool
    def __init__(self, jdf: JavaObject, sql_ctx: SQLContext) -> None: ...
    @property
    def rdd(self) -> RDD[Row]: ...
    @property
    def na(self) -> DataFrameNaFunctions: ...
    @property
    def stat(self) -> DataFrameStatFunctions: ...
    def toJSON(self, use_unicode: bool = ...) -> RDD[str]: ...
    def registerTempTable(self, name: str) -> None: ...
    def createTempView(self, name: str) -> None: ...
    def createOrReplaceTempView(self, name: str) -> None: ...
    def createGlobalTempView(self, name: str) -> None: ...
    @property
    def write(self) -> DataFrameWriter: ...
    @property
    def writeStream(self) -> DataStreamWriter: ...
    @property
    def schema(self) -> StructType: ...
    def printSchema(self) -> None: ...
    def explain(self, extended: bool = ...) -> None: ...
    def exceptAll(self, other: DataFrame) -> DataFrame: ...
    def isLocal(self) -> bool: ...
    @property
    def isStreaming(self) -> bool: ...
    def show(self, n: int = ..., truncate: bool = ..., vertical: bool = ...) -> None: ...
    def checkpoint(self, eager: bool = ...) -> DataFrame: ...
    def localCheckpoint(self, eager: bool = ...) -> DataFrame: ...
    def withWatermark(self, eventTime: ColumnOrName, delayThreshold: str) -> DataFrame: ...
    def hint(self, name: str, *parameters: Any) -> DataFrame: ...
    def count(self) -> int: ...
    def collect(self) -> List[Row]: ...
    def toLocalIterator(self) -> Iterator[Row]: ...
    def limit(self, num: int) -> DataFrame: ...
    def take(self, num: int) -> List[Row]: ...
    def foreach(self, f: Callable[[Row], None]) -> None: ...
    def foreachPartition(self, f: Callable[[Iterator[Row]], None]) -> None: ...
    def cache(self) -> DataFrame: ...
    def persist(self, storageLevel: StorageLevel = ...) -> DataFrame: ...
    @property
    def storageLevel(self) -> StorageLevel: ...
    def unpersist(self, blocking: bool = ...) -> DataFrame: ...
    def coalesce(self, numPartitions: int) -> DataFrame: ...
    def repartition(self, numPartitions: Union[int, ColumnOrName], *cols: ColumnOrName) -> DataFrame: ...
    def repartitionByRange(self, numPartitions: Union[int, ColumnOrName], *cols: ColumnOrName) -> DataFrame: ...
    def sample(self, withReplacement: Optional[bool], fraction: float, seed: Optional[int] = ...) -> DataFrame: ...
    def sampleBy(self, col: str, fractions: float, seed: Optional[int] = ...) -> DataFrame: ...
    def randomSplit(self, weights: List[float], seed: Optional[int] = ...) -> List[DataFrame]: ...
    @property
    def dtypes(self) -> List[Tuple[str, str]]: ...
    @property
    def columns(self) -> List[str]: ...
    def colRegex(self, colName: str) -> Column: ...
    def alias(self, alias: str) -> DataFrame: ...
    def crossJoin(self, other: DataFrame) -> DataFrame: ...
    def join(self, other: DataFrame, on: Optional[Union[str, List[str], Column, List[Column]]] = ..., how: Optional[str] = ...) -> DataFrame: ...
    def sortWithinPartitions(self, *cols: Union[str, Column, List[Union[str, Column]]], ascending: Union[bool, List[bool]] = ...) -> DataFrame: ...
    def sort(self, *cols: Union[str, Column, List[Union[str, Column]]], ascending: Union[bool, List[bool]] = ...) -> DataFrame: ...
    def orderBy(self, *cols: Union[str, Column, List[Union[str, Column]]], ascending: Union[bool, List[bool]] = ...) -> DataFrame: ...
    def describe(self, *cols: Union[str, List[str]]) -> DataFrame: ...
    def summary(self, *statistics: str) -> DataFrame: ...
    @overload
    def head(self) -> Row: ...
    @overload
    def head(self, n: int) -> List[Row]: ...
    def first(self) -> Row: ...
    def __getitem__(self, item: Union[int, str]) -> Column: ...
    def __getattr__(self, name: str) -> Column: ...
    @overload
    def select(self, *cols: ColumnOrName) -> DataFrame: ...
    @overload
    def select(self, __cols: List[ColumnOrName]) -> DataFrame: ...
    @overload
    def selectExpr(self, *expr: str) -> DataFrame: ...
    @overload
    def selectExpr(self, *expr: List[str]) -> DataFrame: ...
    def filter(self, condition: ColumnOrName) -> DataFrame: ...
    @overload
    def groupBy(self, *cols: ColumnOrName) -> GroupedData: ...
    @overload
    def groupBy(self, __cols: List[ColumnOrName]) -> GroupedData: ...
    @overload
    def rollup(self, *cols: ColumnOrName) ->  GroupedData: ...
    @overload
    def rollup(self, __cols: List[ColumnOrName]) ->  GroupedData: ...
    @overload
    def cube(self, *cols: ColumnOrName) -> GroupedData: ...
    @overload
    def cube(self, __cols: List[ColumnOrName]) ->  GroupedData: ...
    def agg(self, *exprs: Union[Column, Dict[str, str]]) -> DataFrame: ...
    def union(self, other: DataFrame) -> DataFrame: ...
    def unionAll(self, other: DataFrame) -> DataFrame: ...
    def unionByName(self, other: DataFrame) -> DataFrame: ...
    def intersect(self, other: DataFrame) -> DataFrame: ...
    def intersectAll(self, other: DataFrame) -> DataFrame: ...
    def subtract(self, other: DataFrame) -> DataFrame: ...
    def dropDuplicates(self, subset: Optional[List[str]] = ...) -> DataFrame: ...
    def dropna(self, how: str = ..., thresh: Optional[int] = ..., subset: Optional[List[str]] = ...) -> DataFrame: ...
    @overload
    def fillna(self, value: LiteralType, subset: Optional[List[str]] = ...) -> DataFrame: ...
    @overload
    def fillna(self, value: Dict[str, LiteralType]) -> DataFrame: ...
    @overload
    def replace(self, to_replace: LiteralType, value: LiteralType, subset: Optional[List[str]] = ...) -> DataFrame: ...
    @overload
    def replace(self, to_replace: List[LiteralType], value: List[LiteralType], subset: Optional[List[str]] = ...) -> DataFrame: ...
    @overload
    def replace(self, to_replace: Dict[LiteralType, LiteralType], subset: Optional[List[str]] = ...) -> DataFrame: ...
    @overload
    def replace(self, to_replace: List[LiteralType], value: LiteralType, subset: Optional[List[str]] = ...) -> DataFrame: ...
    def approxQuantile(self, col: str, probabilities: List[float], relativeError: float) -> List[float]: ...
    def corr(self, col1: str, col2: str, method: Optional[str] = ...) -> float: ...
    def cov(self, col1: str, col2: str) -> float: ...
    def crosstab(self, col1: str, col2: str) -> DataFrame: ...
    def freqItems(self, cols: List[str], support: Optional[float] = ...) -> DataFrame: ...
    def withColumn(self, colName: str, col: Column) -> DataFrame: ...
    def withColumnRenamed(self, existing: str, new: str) -> DataFrame: ...
    def drop(self, *cols: ColumnOrName) -> DataFrame: ...
    def toDF(self, *cols: ColumnOrName) -> DataFrame: ...
    def toPandas(self) -> pandas.core.frame.DataFrame: ...
    @overload
    def groupby(self, *cols: ColumnOrName) -> DataFrame: ...
    @overload
    def groupby(self, __cols: List[ColumnOrName]) -> DataFrame: ...
    def drop_duplicates(self, subset: Optional[List[str]] = ...) -> DataFrame: ...
    def where(self, condition: ColumnOrName) -> DataFrame: ...

class DataFrameNaFunctions:
    df = ...  # type: DataFrame
    def __init__(self, df: DataFrame) -> None: ...
    def drop(self, how: str = ..., thresh: Optional[int] = ..., subset: Optional[List[str]] = ...) -> DataFrame: ...
    @overload
    def fill(self, value: LiteralType, subset: Optional[List[str]] = ...) -> DataFrame: ...
    @overload
    def fill(self, value: Dict[str, LiteralType]) -> DataFrame: ...
    @overload
    def replace(self, to_replace: LiteralType, value: LiteralType, subset: Optional[List[str]] = ...) -> DataFrame: ...
    @overload
    def replace(self, to_replace: List[LiteralType], value: List[LiteralType], subset: Optional[List[str]] = ...) -> DataFrame: ...
    @overload
    def replace(self, to_replace: Dict[LiteralType, LiteralType], subset: Optional[List[str]] = ...) -> DataFrame: ...
    @overload
    def replace(self, to_replace: List[LiteralType], value: LiteralType, subset: Optional[List[str]] = ...) -> DataFrame: ...

class DataFrameStatFunctions:
    df = ...  # type: DataFrame
    def __init__(self, df: DataFrame) -> None: ...
    def approxQuantile(self, col: str, probabilities: List[float], relativeError: float) -> List[float]: ...
    def corr(self, col1: str, col2: str, method: Optional[str] = ...) -> float: ...
    def cov(self, col1: str, col2: str) -> float: ...
    def crosstab(self, col1: str, col2: str) -> DataFrame: ...
    def freqItems(self, cols: List[str], support: Optional[float] = ...) -> DataFrame: ...
    def sampleBy(self, col: str, fractions: float, seed: Optional[int] = ...) -> DataFrame: ...
