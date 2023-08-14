import numpy as np
from typing import NamedTuple, Optional, Tuple, TypeAlias


class Result(NamedTuple):
    statistic: float | np.ndarray
    pvalue: float | np.ndarray


class TestResult(NamedTuple):
    result: Optional[Result]
    error: Optional[str]


IsAplicableResult: TypeAlias = Tuple[bool, Optional[str]]
