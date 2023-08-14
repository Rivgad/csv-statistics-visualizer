from tests.result import IsAplicableResult, Result
from tests.statistical_test import StatisticalTest


import pandas as pd
import streamlit as st
from scipy import stats


from typing import List


class ChiSquareTest(StatisticalTest):
    def _is_applicable(
        self, dataframe: pd.DataFrame, columns: List[str]
    ) -> IsAplicableResult:
        return (True, None)

    def _compute(self, dataframe: pd.DataFrame, columns: List[str]) -> Result:
        cross_tab = pd.crosstab(
            dataframe[columns[0]],
            dataframe[columns[1]],
            margins=True,
        )
        st.write("Contingency table:")
        st.write(cross_tab)

        cross_tab = cross_tab.drop("All", axis=1).drop("All", axis=0)
        stat, pvalue, _, _ = stats.chi2_contingency(cross_tab)

        return Result(statistic=stat, pvalue=pvalue)
