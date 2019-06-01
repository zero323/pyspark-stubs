from typing import Any, List, Optional, TypeVar, Union, SupportsFloat
import datetime
import decimal
import pyspark.sql.column

ColumnOrName = Union[pyspark.sql.column.Column, str]
ColumnNameOrFloat = Union[ColumnOrName, SupportsFloat]
Literal = Union[bool, int, float, str]
DecimalLiteral = decimal.Decimal
DateTimeLiteral = Union[datetime.datetime, datetime.date]
LiteralType = TypeVar('LiteralType', bool, int, float, str)
