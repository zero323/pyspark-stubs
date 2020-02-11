from typing import (
    Any,
    Callable,
    Iterable,
    List,
    NewType,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Union,
)
from typing_extensions import Protocol, Literal
from types import FunctionType

from pyspark.sql._typing import LiteralType
from pyspark.sql.pandas._typing.protocols.frame import DataFrameLike as DataFrameLike
from pyspark.sql.pandas._typing.protocols.series import SeriesLike as SeriesLike

import pandas.core.frame  # type: ignore[import]
import pandas.core.series  # type: ignore[import]

# POC compatibility annotations
PandasDataFrame: Type[DataFrameLike] = pandas.core.frame.DataFrame
PandasSeries: Type[SeriesLike] = pandas.core.series.Series

DataFrameOrSeriesLike = Union[DataFrameLike, SeriesLike]

# UDF annotations
PandasScalarUDFType = Literal[200]
PandasScalarIterUDFType = Literal[204]
PandasGroupedMapUDFType = Literal[201]
PandasCogroupedMapUDFType = Literal[206]
PandasGroupedAggUDFType = Literal[202]
PandasMapIterUDFType = Literal[205]

class PandasVariadicScalarToScalarFunction(Protocol):
    def __call__(self, *_: DataFrameOrSeriesLike) -> SeriesLike: ...

PandasScalarToScalarFunction = Union[
    PandasVariadicScalarToScalarFunction,
    Callable[[DataFrameOrSeriesLike], SeriesLike],
    Callable[[DataFrameOrSeriesLike, DataFrameOrSeriesLike], SeriesLike],
    Callable[
        [DataFrameOrSeriesLike, DataFrameOrSeriesLike, DataFrameOrSeriesLike],
        SeriesLike,
    ],
    Callable[
        [
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
        ],
        SeriesLike,
    ],
    Callable[
        [
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
        ],
        SeriesLike,
    ],
    Callable[
        [
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
        ],
        SeriesLike,
    ],
    Callable[
        [
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
        ],
        SeriesLike,
    ],
    Callable[
        [
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
        ],
        SeriesLike,
    ],
    Callable[
        [
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
        ],
        SeriesLike,
    ],
    Callable[
        [
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
        ],
        SeriesLike,
    ],
]

class PandasVariadicScalarToStructFunction(Protocol):
    def __call__(self, *_: DataFrameOrSeriesLike) -> DataFrameLike: ...

PandasScalarToStructFunction = Union[
    PandasVariadicScalarToStructFunction,
    Callable[[DataFrameOrSeriesLike], DataFrameLike],
    Callable[[DataFrameOrSeriesLike, DataFrameOrSeriesLike], DataFrameLike],
    Callable[
        [DataFrameOrSeriesLike, DataFrameOrSeriesLike, DataFrameOrSeriesLike],
        DataFrameLike,
    ],
    Callable[
        [
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
        ],
        DataFrameLike,
    ],
    Callable[
        [
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
        ],
        DataFrameLike,
    ],
    Callable[
        [
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
        ],
        DataFrameLike,
    ],
    Callable[
        [
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
        ],
        DataFrameLike,
    ],
    Callable[
        [
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
        ],
        DataFrameLike,
    ],
    Callable[
        [
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
        ],
        DataFrameLike,
    ],
    Callable[
        [
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
            DataFrameOrSeriesLike,
        ],
        DataFrameLike,
    ],
]

PandasScalarIterFunction = Callable[
    [Iterable[Union[DataFrameOrSeriesLike, Tuple[DataFrameOrSeriesLike, ...]]]],
    Iterable[SeriesLike],
]

PandasGroupedMapFunction = Union[
    Callable[[DataFrameLike], DataFrameLike],
    Callable[[Any, DataFrameLike], DataFrameLike],
]

class PandasVariadicGroupedAggFunction(Protocol):
    def __call__(self, *_: SeriesLike) -> LiteralType: ...

PandasGroupedAggFunction = Union[
    Callable[[SeriesLike], LiteralType],
    Callable[[SeriesLike, SeriesLike], LiteralType],
    Callable[[SeriesLike, SeriesLike, SeriesLike], LiteralType],
    Callable[[SeriesLike, SeriesLike, SeriesLike, SeriesLike], LiteralType],
    Callable[[SeriesLike, SeriesLike, SeriesLike, SeriesLike, SeriesLike], LiteralType],
    Callable[
        [SeriesLike, SeriesLike, SeriesLike, SeriesLike, SeriesLike, SeriesLike],
        LiteralType,
    ],
    Callable[
        [
            SeriesLike,
            SeriesLike,
            SeriesLike,
            SeriesLike,
            SeriesLike,
            SeriesLike,
            SeriesLike,
        ],
        LiteralType,
    ],
    Callable[
        [
            SeriesLike,
            SeriesLike,
            SeriesLike,
            SeriesLike,
            SeriesLike,
            SeriesLike,
            SeriesLike,
            SeriesLike,
        ],
        LiteralType,
    ],
    Callable[
        [
            SeriesLike,
            SeriesLike,
            SeriesLike,
            SeriesLike,
            SeriesLike,
            SeriesLike,
            SeriesLike,
            SeriesLike,
            SeriesLike,
        ],
        LiteralType,
    ],
    Callable[
        [
            SeriesLike,
            SeriesLike,
            SeriesLike,
            SeriesLike,
            SeriesLike,
            SeriesLike,
            SeriesLike,
            SeriesLike,
            SeriesLike,
            SeriesLike,
        ],
        LiteralType,
    ],
    PandasVariadicGroupedAggFunction,
]

PandasMapIterFunction = Callable[[Iterable[DataFrameLike]], Iterable[DataFrameLike]]

PandasCogroupedMapFunction = Callable[[DataFrameLike, DataFrameLike], DataFrameLike]

MapIterPandasUserDefinedFunction = NewType(
    "MapIterPandasUserDefinedFunction", FunctionType
)
GroupedMapPandasUserDefinedFunction = NewType(
    "GroupedMapPandasUserDefinedFunction", FunctionType
)
CogroupedMapPandasUserDefinedFunction = NewType(
    "CogroupedMapPandasUserDefinedFunction", FunctionType
)
