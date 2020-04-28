from typing import Any, Iterable, List, Optional, Tuple, TypeVar, Union
from pyspark.mllib.linalg import Vector
from numpy import ndarray  # type: ignore[import]

VectorLike = Union[Vector, List[float], Tuple[float, ...]]
