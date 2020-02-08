# Stubs for pyspark.accumulators (Python 3.7)
#

from typing import Callable, Generic, Tuple, Type, TypeVar

import socketserver.BaseRequestHandler  # type: ignore

from pyspark._typing import SupportsIAdd

T = TypeVar("T")
U = TypeVar("U", bound=SupportsIAdd)

import socketserver as SocketServer
from typing import Any

class Accumulator(Generic[T]):
    aid: int
    accum_param: AccumulatorParam[T]
    def __init__(
        self, aid: int, value: T, accum_param: AccumulatorParam[T]
    ) -> None: ...
    def __reduce__(
        self,
    ) -> Tuple[
        Callable[[int, int, AccumulatorParam[T]], Accumulator[T]],
        Tuple[int, int, AccumulatorParam[T]],
    ]: ...
    @property
    def value(self) -> T: ...
    @value.setter
    def value(self, value: T) -> None: ...
    def add(self, term: T) -> None: ...
    def __iadd__(self, term: T) -> Accumulator[T]: ...

class AccumulatorParam(Generic[T]):
    def zero(self, value: T) -> T: ...
    def addInPlace(self, value1: T, value2: T) -> T: ...

class AddingAccumulatorParam(AccumulatorParam[U]):
    zero_value: U
    def __init__(self, zero_value: U) -> None: ...
    def zero(self, value: U) -> U: ...
    def addInPlace(self, value1: U, value2: U) -> U: ...

class _UpdateRequestHandler(SocketServer.StreamRequestHandler):
    def handle(self) -> None: ...

class AccumulatorServer(SocketServer.TCPServer):
    auth_token: str
    def __init__(
        self,
        server_address: Tuple[str, int],
        RequestHandlerClass: Type[socketserver.BaseRequestHandler],
        auth_token: str,
    ) -> None: ...
    server_shutdown: bool
    def shutdown(self) -> None: ...
