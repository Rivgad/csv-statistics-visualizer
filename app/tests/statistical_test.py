from abc import ABC, abstractmethod
from typing import List
import pandas as pd
from app.tests.result import TestResult, Result, IsAplicableResult


class StatisticalTest(ABC):
    @abstractmethod
    def _is_applicable(
        self, dataframe: pd.DataFrame, columns: List[str]
    ) -> IsAplicableResult:
        pass

    @abstractmethod
    def _compute(self, dataframe: pd.DataFrame, columns: List[str]) -> Result:
        pass

    def execute(self, dataframe: pd.DataFrame, columns: List[str]) -> TestResult:
        (is_applicable, error) = self._is_applicable(dataframe, columns)

        if is_applicable:
            return TestResult(self._compute(dataframe, columns), None)
        else:
            return TestResult(None, error)
