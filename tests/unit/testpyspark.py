#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from mypy.test.data import DataDrivenTestCase, DataSuite
from mypy.test.testcheck import TypeCheckSuite


TypeCheckSuite.files = [
    "core.test",
    "core-context.test",
    "core-resultiterable.test",
    "core-rdd.test",
    "ml-classification.test",
    "ml-evaluation.test",
    "ml-feature.test",
    "ml-param.test",
    "ml-readable.test",
    "ml-regression.test",
    "sql-column.test",
    "sql-dataframe.test",
    "sql-pandas-typing-compatibility.test",
    "sql-readwriter.test",
    "sql-session.test",
    "sql-udf.test",
]
