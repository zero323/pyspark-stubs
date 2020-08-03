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

"""
Setup for PySpark type annotations.

Notes:

- To avoid manual PYTHONPATH modification the package installation will overlay PySpark installation. If this is not acceptable please download source and add it to PYTHONPATH manually.

"""


from setuptools import setup
import os
import sys

# find_packages doesn't seem to handle stub files
# so we'll enumarate manually
src_path = os.path.join("third_party", "3")


def list_packages(src_path=src_path):
    for root, _, _ in os.walk(os.path.join(src_path, "pyspark")):
        yield ".".join(os.path.relpath(root, src_path).split(os.path.sep))


setup(
    name="pyspark-stubs",
    package_dir={"": src_path},
    version="3.1.0.dev0",
    description="A collection of the Apache Spark stub files",
    long_description=(
        open("README.rst").read() if os.path.exists("README.rst") else ""
    ),
    url="https://github.com/zero323/pyspark-stubs",
    packages=list(list_packages()),
    package_data={"": ["*.pyi", "py.typed"]},
    install_requires=["pyspark>=3.1.0.dev0,<3.2.0"],
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Typing :: Typed",
    ],
)
