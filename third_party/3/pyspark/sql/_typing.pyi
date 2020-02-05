from typing import Any, List, Optional, Tuple, TypeVar, Union
import datetime
import decimal
import pyspark.sql.column
import pyspark.sql.types

ColumnOrName = Union[pyspark.sql.column.Column, str]
Literal = Union[bool, int, float, str]
DecimalLiteral = decimal.Decimal
DateTimeLiteral = Union[datetime.datetime, datetime.date]
LiteralType = TypeVar("LiteralType", bool, int, float, str)
DataTypeOrString = Union[pyspark.sql.types.DataType, str]

RowLike = TypeVar("RowLike", List[Any], Tuple[Any, ...], pyspark.sql.types.Row)
