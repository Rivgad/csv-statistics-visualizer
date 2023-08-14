import numpy as np
from typing import NamedTuple, Optional, Tuple, TypeAlias


class Result(NamedTuple):
    statistic: float | np.ndarray
    pvalue: float | np.ndarray


class TestExecutionError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


IsAplicableResult: TypeAlias = Tuple[bool, Optional[str]]
