# Stubs for pyspark.streaming.kafka (Python 3.5)
#

from typing import overload
from typing import Any, Dict, Callable, Generic, List, Optional, Tuple, TypeVar
from pyspark.rdd import RDD
from pyspark.context import SparkContext
from pyspark.serializers import Serializer
from pyspark.storagelevel import StorageLevel
from pyspark.streaming.context import StreamingContext
from pyspark.streaming.dstream import DStream, TransformedDStream
from py4j.java_gateway import JavaObject  # type: ignore
import datetime

R = TypeVar("R")
T = TypeVar("T")
U = TypeVar("U")

def utf8_decoder(s: Optional[bytes]) -> Optional[str]: ...

class KafkaUtils:
    @staticmethod
    def createStream(
        ssc: StreamingContext,
        zkQuorum: str,
        groupId: str,
        topics: Dict[str, int],
        kafkaParams: Optional[Dict[str, str]] = ...,
        storageLevel: StorageLevel = ...,
        keyDecoder: Callable[[bytes], T] = ...,
        valueDecoder: Callable[[bytes], U] = ...,
    ) -> DStream[Tuple[T, U]]: ...
    @overload
    @staticmethod
    def createDirectStream(
        ssc: StreamingContext,
        topics: List[str],
        kafkaParams: Dict[str, str],
        fromOffsets: Dict[TopicAndPartition, int],
        keyDecoder: Callable[[bytes], T],
        valueDecoder: Callable[[bytes], U],
        messageHandler: Callable[[KafkaMessageAndMetadata], R],
    ) -> DStream[R]: ...
    @overload
    @staticmethod
    def createDirectStream(
        ssc: StreamingContext,
        topics: List[str],
        kafkaParams: Dict[str, str],
        keyDecoder: Callable[[bytes], T],
        valueDecoder: Callable[[bytes], U],
        messageHandler: Callable[[KafkaMessageAndMetadata], R],
    ) -> DStream[R]: ...
    @overload
    @staticmethod
    def createDirectStream(
        ssc: StreamingContext,
        topics: List[str],
        kafkaParams: Dict[str, str],
        fromOffsets: Dict[TopicAndPartition, int],
        valueDecoder: Callable[[bytes], U],
        messageHandler: Callable[[KafkaMessageAndMetadata], R],
    ) -> DStream[R]: ...
    @overload
    @staticmethod
    def createDirectStream(
        ssc: StreamingContext,
        topics: List[str],
        kafkaParams: Dict[str, str],
        fromOffsets: Dict[TopicAndPartition, int],
        keyDecoder: Callable[[bytes], T],
        messageHandler: Callable[[KafkaMessageAndMetadata], R],
    ) -> DStream[R]: ...
    @overload
    @staticmethod
    def createDirectStream(
        ssc: StreamingContext,
        topics: List[str],
        kafkaParams: Dict[str, str],
        valueDecoder: Callable[[bytes], U],
        messageHandler: Callable[[KafkaMessageAndMetadata], R],
    ) -> DStream[R]: ...
    @overload
    @staticmethod
    def createDirectStream(
        ssc: StreamingContext,
        topics: List[str],
        kafkaParams: Dict[str, str],
        keyDecoder: Callable[[bytes], T],
        messageHandler: Callable[[KafkaMessageAndMetadata], R],
    ) -> DStream[R]: ...
    @overload
    @staticmethod
    def createDirectStream(
        ssc: StreamingContext,
        topics: List[str],
        kafkaParams: Dict[str, str],
        fromOffsets: Dict[TopicAndPartition, int],
        messageHandler: Callable[[KafkaMessageAndMetadata], R],
    ) -> DStream[R]: ...
    @overload
    @staticmethod
    def createDirectStream(
        ssc: StreamingContext,
        topics: List[str],
        kafkaParams: Dict[str, str],
        messageHandler: Callable[[KafkaMessageAndMetadata], R],
    ) -> DStream[R]: ...
    @overload
    @staticmethod
    def createDirectStream(
        ssc: StreamingContext,
        topics: List[str],
        kafkaParams: Dict[str, str],
        fromOffsets: Optional[Dict[TopicAndPartition, int]] = ...,
        keyDecoder: Callable[[bytes], T] = ...,
        valueDecoder: Callable[[bytes], U] = ...,
    ) -> DStream[Tuple[T, U]]: ...
    @overload
    @staticmethod
    def createRDD(
        sc: SparkContext,
        kafkaParams: Dict[str, str],
        offsetRanges: List[int],
        keyDecoder: Callable[[bytes], T],
        valueDecoder: Callable[[bytes], U],
        messageHandler: Callable[[KafkaMessageAndMetadata], R],
    ) -> RDD[R]: ...
    @overload
    @staticmethod
    def createRDD(
        sc: SparkContext,
        kafkaParams: Dict[str, str],
        offsetRanges: List[int],
        leaders: Dict[TopicAndPartition, Broker],
        valueDecoder: Callable[[bytes], U],
        messageHandler: Callable[[KafkaMessageAndMetadata], R],
    ) -> RDD[R]: ...
    @overload
    @staticmethod
    def createRDD(
        sc: SparkContext,
        kafkaParams: Dict[str, str],
        offsetRanges: List[int],
        leaders: Dict[TopicAndPartition, Broker],
        keyDecoder: Callable[[bytes], T],
        messageHandler: Callable[[KafkaMessageAndMetadata], R],
    ) -> RDD[R]: ...
    @overload
    @staticmethod
    def createRDD(
        sc: SparkContext,
        kafkaParams: Dict[str, str],
        offsetRanges: List[int],
        leaders: Dict[TopicAndPartition, Broker],
        messageHandler: Callable[[KafkaMessageAndMetadata], R],
    ) -> RDD[R]: ...
    @overload
    @staticmethod
    def createRDD(
        sc: SparkContext,
        kafkaParams: Dict[str, str],
        offsetRanges: List[int],
        keyDecoder: Callable[[bytes], T],
        messageHandler: Callable[[KafkaMessageAndMetadata], R],
    ) -> RDD[R]: ...
    @overload
    @staticmethod
    def createRDD(
        sc: SparkContext,
        kafkaParams: Dict[str, str],
        offsetRanges: List[int],
        valueDecoder: Callable[[bytes], U],
        messageHandler: Callable[[KafkaMessageAndMetadata], R],
    ) -> RDD[R]: ...
    @overload
    @staticmethod
    def createRDD(
        sc: SparkContext,
        kafkaParams: Dict[str, str],
        offsetRanges: List[int],
        messageHandler: Callable[[KafkaMessageAndMetadata], R],
    ) -> RDD[R]: ...
    @overload
    @staticmethod
    def createRDD(
        sc: SparkContext,
        kafkaParams: Dict[str, str],
        offsetRanges: List[int],
        leaders: Optional[Dict[TopicAndPartition, Broker]] = ...,
        keyDecoder: Callable[[bytes], T] = ...,
        valueDecoder: Callable[[bytes], U] = ...,
    ) -> RDD[Tuple[T, U]]: ...

class OffsetRange:
    topic: str
    partition: int
    fromOffset: int
    untilOffset: int
    def __init__(
        self, topic: str, partition: int, fromOffset: int, untilOffset: int
    ) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...

class TopicAndPartition:
    def __init__(self, topic: str, partition: int) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...

class Broker:
    def __init__(self, host: str, port: int) -> None: ...

class KafkaRDD(RDD):
    def __init__(
        self, jrdd, ctx: SparkContext, jrdd_deserializer: Serializer
    ) -> None: ...
    def offsetRanges(self): ...

class KafkaDStream(DStream[T]):
    def __init__(
        self, jdstream: JavaObject, ssc: StreamingContext, jrdd_deserializer: Serializer
    ) -> None: ...
    @overload
    def foreachRDD(self: "KafkaDStream[T]", func: Callable[[RDD[T]], None]) -> None: ...
    @overload
    def foreachRDD(
        self: "KafkaDStream[T]", func: Callable[[datetime.datetime, RDD[T]], None]
    ) -> None: ...
    @overload
    def transform(
        self: "KafkaDStream[T]", func: Callable[[RDD[T]], RDD[U]]
    ) -> KafkaTransformedDStream[U]: ...
    @overload
    def transform(
        self: "KafkaDStream[T]", func: Callable[[datetime.datetime, RDD[T]], RDD[U]]
    ) -> KafkaTransformedDStream[U]: ...

class KafkaTransformedDStream(TransformedDStream[U]):
    @overload
    def __init__(
        self, prev: KafkaDStream[T], func: Callable[[RDD[T]], RDD[U]]
    ) -> None: ...
    @overload
    def __init__(
        self, prev: KafkaDStream[T], func: Callable[[datetime.datetime, RDD[T]], RDD[U]]
    ) -> None: ...

class KafkaMessageAndMetadata(Generic[T, U]):
    topic: str
    partition: int
    offset: int
    def __init__(self, topic, partition, offset, key, message) -> None: ...
    def __reduce__(self): ...
    @property
    def key(self): ...
    @property
    def message(self): ...
