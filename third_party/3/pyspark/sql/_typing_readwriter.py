from mypy_extensions import TypedDict
from typing_extensions import Literal
from typing import Optional

# _CSVReaderOptions = {
#     "sep": Optional[str],
#     "encoding": Optional[str],
#     "quote": Optional[str],
#     "escape": Optional[str],
#     "charToEscapeQuoteEscaping": Optional[str],
#     "comment": Optional[str],
#     "header": Optional[Literal["true", "false", True, False]],
#     "enforceSchema": Optional[Literal["true", "false", True, False]],
#     "inferSchema": Optional[Literal["true", "false", True, False]],
#     "samplingRatio": Optional[float],
#     "ignoreLeadingWhiteSpace": Optional[Literal["true", "false", True, False]],
#     "ignoreTrailingWhiteSpace": Optional[Literal["true", "false", True, False]],
#     "nullValue": Optional[str],
#     "emptyValue": Optional[str],
#     "nanValue": Optional[str],
#     "positiveInf": Optional[str],
#     "negativeInf": Optional[str],
#     "dateFormat": Optional[str],
#     "timestampFormat": Optional[str],
#     "maxColumns": Optional[int],
#     "maxCharsPerColumn": Optional[int],
#     "mode": Optional[Literal["PERMISSIVE", "DROPMALFORMED", "FAILFAST"]],
#     "columnNameOfCorruptRecord": Optional[str],
#     "multiLine": Optional[Literal["true", "false", True, False]],
# }
#
# CSVReaderOptions = TypedDict("CSVReaderOptions", _CSVReaderOptions)
#
#
# for k, v in _CSVReaderOptions.items():
#     print(f"""@overload\ndef option(self, key: Literal["{k}"], value: {v}) -> _CSVDataFrameReader: ...""".replace("NoneType", "None"))
