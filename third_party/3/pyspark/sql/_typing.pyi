from typing import (
    Any,
    Callable,
    Iterable,
    List,
    NewType,
    Optional,
    Tuple,
    TypeVar,
    Union,
)
from typing_extensions import Protocol, Literal
from types import FunctionType

import datetime
import decimal

from pyspark._typing import PrimitiveType
import pyspark.sql.column
import pyspark.sql.types
from pyspark.sql.column import Column

import pandas.core.frame  # type: ignore[import]
import pandas.core.series  # type: ignore[import]

ColumnOrName = Union[pyspark.sql.column.Column, str]
DecimalLiteral = decimal.Decimal
DateTimeLiteral = Union[datetime.datetime, datetime.date]
LiteralType = PrimitiveType
AtomicDataTypeOrString = Union[pyspark.sql.types.AtomicType, str]
DataTypeOrString = Union[pyspark.sql.types.DataType, str]
OptionalPrimitiveType = Optional[PrimitiveType]

RowLike = TypeVar("RowLike", List[Any], Tuple[Any, ...], pyspark.sql.types.Row)

class SupportsOpen(Protocol):
    def open(self, partition_id: int, epoch_id: int) -> bool: ...

class SupportsProcess(Protocol):
    def process(self, row: pyspark.sql.types.Row) -> None: ...

class SupportsClose(Protocol):
    def close(self, error: Exception) -> None: ...

PandasScalarUDFType = Literal[200]
PandasScalarIterUDFType = Literal[204]
PandasGroupedMapUDFType = Literal[201]
PandasGroupedAggUDFType = Literal[202]
PandasMapIterUDFType = Literal[205]

class PandasVariadicScalarFunction(Protocol):
    def __call__(self, *_: pandas.core.series.Series) -> pandas.core.series.Series: ...

PandasScalarFunction = Union[
    Callable[[pandas.core.series.Series], pandas.core.series.Series],
    Callable[
        [pandas.core.series.Series, pandas.core.series.Series],
        pandas.core.series.Series,
    ],
    Callable[
        [
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
        ],
        pandas.core.series.Series,
    ],
    Callable[
        [
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
        ],
        pandas.core.series.Series,
    ],
    Callable[
        [
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
        ],
        pandas.core.series.Series,
    ],
    Callable[
        [
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
        ],
        pandas.core.series.Series,
    ],
    Callable[
        [
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
        ],
        pandas.core.series.Series,
    ],
    Callable[
        [
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
        ],
        pandas.core.series.Series,
    ],
    Callable[
        [
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
        ],
        pandas.core.series.Series,
    ],
    Callable[
        [
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
        ],
        pandas.core.series.Series,
    ],
    PandasVariadicScalarFunction,
]

PandasGroupedMapFunction = Union[
    Callable[[pandas.core.frame.DataFrame], pandas.core.frame.DataFrame],
    Callable[[Any, pandas.core.frame.DataFrame], pandas.core.frame.DataFrame],
]

class PandasVariadicGroupedAggFunction(Protocol):
    def __call__(self, *_: pandas.core.series.Series) -> LiteralType: ...

PandasGroupedAggFunction = Union[
    Callable[[pandas.core.series.Series], LiteralType],
    Callable[[pandas.core.series.Series, pandas.core.series.Series], LiteralType],
    Callable[
        [
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
        ],
        LiteralType,
    ],
    Callable[
        [
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
        ],
        LiteralType,
    ],
    Callable[
        [
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
        ],
        LiteralType,
    ],
    Callable[
        [
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
        ],
        LiteralType,
    ],
    Callable[
        [
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
        ],
        LiteralType,
    ],
    Callable[
        [
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
        ],
        LiteralType,
    ],
    Callable[
        [
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
        ],
        LiteralType,
    ],
    Callable[
        [
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
            pandas.core.series.Series,
        ],
        LiteralType,
    ],
    PandasVariadicGroupedAggFunction,
]

class UserDefinedFunctionLike(Protocol):
    def __call__(self, *_: ColumnOrName) -> Column: ...

GroupedMapPandasUserDefinedFunction = NewType(
    "GroupedMapPandasUserDefinedFunction", FunctionType
)
