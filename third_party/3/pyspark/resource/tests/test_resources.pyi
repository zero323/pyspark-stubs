import unittest
from pyspark.resource import (
    ExecutorResourceRequests as ExecutorResourceRequests,
    ResourceProfileBuilder as ResourceProfileBuilder,
    TaskResourceRequests as TaskResourceRequests,
)

class ResourceProfileTests(unittest.TestCase):
    def test_profile_before_sc(self) -> None: ...
