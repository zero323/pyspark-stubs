from mypy.test.data import DataDrivenTestCase, DataSuite
from mypy.test.testcheck import TypeCheckSuite


TypeCheckSuite.files = [
    "core-context.test",
    "core-resultiterable.test",
    "core-rdd.test",
    "ml-evaluation.test",
    "ml-param.test",
    "ml-readable.test",
    "sql-column.test",
    "sql-dataframe.test",
    "sql-pandas-typing-compatibility.test",
    "sql-readwriter.test",
    "sql-udf.test",
]
