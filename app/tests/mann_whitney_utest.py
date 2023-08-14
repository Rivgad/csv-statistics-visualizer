from helpers import is_categorical
from tests.result import IsAplicableResult, Result
from tests.statistical_test import StatisticalTest


import pandas as pd
from scipy import stats


from typing import List


class MannWhitneyUTest(StatisticalTest):
    def _is_applicable(
        self, dataframe: pd.DataFrame, columns: List[str]
    ) -> IsAplicableResult:
        if not is_categorical(dataframe[columns[0]], dataframe[columns[1]]):
            return (True, None)
        else:
            return (
                False,
                "Mann–Whitney U test requires two numerical variables. Please select other variables or a test.",
            )

    def _compute(self, dataframe: pd.DataFrame, columns: List[str]) -> Result:
        df = dataframe.dropna(subset=columns)

        stat, pvalue = stats.mannwhitneyu(df[columns[0]], df[columns[1]])
        return Result(statistic=stat, pvalue=pvalue)
