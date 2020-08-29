# Stubs for pyspark.storagelevel (Python 3.5)
#
from typing import Any, ClassVar

class StorageLevel:
    DISK_ONLY: ClassVar["StorageLevel"]
    DISK_ONLY_2: ClassVar["StorageLevel"]
    MEMORY_ONLY: ClassVar["StorageLevel"]
    MEMORY_ONLY_2: ClassVar["StorageLevel"]
    MEMORY_AND_DISK: ClassVar["StorageLevel"]
    MEMORY_AND_DISK_2: ClassVar["StorageLevel"]
    OFF_HEAP: ClassVar["StorageLevel"]

    useDisk: bool
    useMemory: bool
    useOffHeap: bool
    deserialized: bool
    replication: int
    def __init__(
        self,
        useDisk: bool,
        useMemory: bool,
        useOffHeap: bool,
        deserialized: bool,
        replication: int = ...,
    ) -> None: ...
