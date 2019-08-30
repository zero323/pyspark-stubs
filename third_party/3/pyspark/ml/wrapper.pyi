# Stubs for pyspark.ml.wrapper (Python 3.7)
#

from pyspark.ml import Estimator, Model, Transformer
from pyspark.ml.param import Params
from typing import Any, Optional, TypeVar

JM = TypeVar("JM", bound=JavaTransformer)

xrange = range

class JavaWrapper:
    def __init__(self, java_obj: Optional[Any] = ...) -> None: ...
    def __del__(self) -> None: ...

class JavaParams(JavaWrapper, Params):
    __metaclass__: Any = ...
    def copy(self, extra: Optional[Any] = ...): ...

class JavaEstimator(JavaParams, Estimator[JM]):
    __metaclass__: Any = ...

class JavaTransformer(JavaParams, Transformer):
    __metaclass__: Any = ...

class JavaModel(JavaTransformer, Model):
    __metaclass__: Any = ...
    def __init__(self, java_model: Optional[Any] = ...) -> None: ...
