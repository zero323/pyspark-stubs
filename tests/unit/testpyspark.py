from mypy.test.data import DataDrivenTestCase, DataSuite
from mypy.test.testcheck import TypeCheckSuite


TypeCheckSuite.files = [
    "core-context.test",
    "core-rdd.test",
    "ml-evaluation.test",
    "ml-param.test",
    "ml-readable.test",
    "resultiterable.test",
    "sql-column.test",
    "sql-dataframe.test",
    "sql-pandas-typing-compatibility.test",
    "sql-readwriter.test",
    "core-context.test",    
    "sql-udf.test",
]
