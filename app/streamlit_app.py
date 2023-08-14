import pandas as pd
import streamlit as st
from pandas.errors import ParserError
import plotly.express as px
from scipy import stats


if "show_distplots" not in st.session_state:
    st.session_state.show_distplots = False


def click_button_show_distplots():
    st.session_state.show_distplots = not st.session_state.show_distplots


def main():
    st.markdown("# 📊 Data visualization and testing")
    with st.echo(code_location="below"):
        st.markdown("### Load dataset")
        use_example_dataset = st.checkbox("Use example dataset")

        if use_example_dataset:
            uploaded_file = ".\\datasets\\students.csv"
        else:
            uploaded_file = st.file_uploader(
                "Load dataset (*.csv)", ["csv"], accept_multiple_files=False
            )

        if uploaded_file is not None:
            dataframe = pd.read_csv(uploaded_file)
        else:
            return

        st.markdown("### Data preview")
        st.write(dataframe[:5])

        columns = dataframe.columns.tolist()
        columns_options = st.multiselect(
            "Choose columns",
            options=columns,
            max_selections=2,
            placeholder="Choose two columns",
        )

        if len(columns_options) != 2:
            st.warning("You have to select 2 columns")
            return

        st.markdown("### Distpots view")
        st.button("Show", on_click=click_button_show_distplots)
        if st.session_state.show_distplots:
            for column_option in columns_options:
                if dataframe[column_option].dtype in ["object", "bool"]:
                    counts = dataframe[column_option].value_counts()

                    fig = px.pie(
                        names=counts.index,
                        values=counts,
                    )
                else:
                    fig = px.histogram(
                        data_frame=dataframe,
                        x=column_option,
                        marginal="box",
                        histnorm="density",
                    )

                st.plotly_chart(fig, use_container_width=True)

        st.markdown("### Testing")
        test_name = st.selectbox(
            "Choose algorithms",
            options=[
                "Welch's t-test",
                "Mann–Whitney U test",
                "Chi-square",
            ],
            placeholder="Choose algorithm",
        )

        if st.button("Calculate"):
            if test_name == "Welch's t-test":
                if (dataframe[columns_options[0]].dtype not in ["object", "bool"]) and (
                    dataframe[columns_options[1]].dtype not in ["object", "bool"]
                ):
                    df = dataframe.dropna(subset=columns_options)

                    stat, pvalue = stats.ttest_ind(
                        df[columns_options[0]], df[columns_options[1]], equal_var=False
                    )
                    st.write("Student's t-test result:")
                    st.write(f"Statistic = {stat}")
                    st.write(f"p-value = {pvalue}")
                    if pvalue < 0.05:
                        st.write(
                            "The difference is statistically significant (p < 0.05)"
                        )
                    else:
                        st.write(
                            "The difference is not statistically significant (p >= 0.05)"
                        )
                else:
                    st.write(
                        "The t-test requires two numerical variables. Please select other variables or a test."
                    )
            elif test_name == "Mann–Whitney U test":
                if (dataframe[columns_options[0]].dtype != "object") & (
                    dataframe[columns_options[1]].dtype != "object"
                ):
                    df = dataframe.dropna(subset=columns_options)

                    stat, pvalue = stats.mannwhitneyu(
                        df[columns_options[0]], df[columns_options[1]]
                    )

                    st.write("Mann–Whitney U test result:")
                    st.write(f"Statistic = {stat}")
                    st.write(f"p-value = {pvalue}")
                    if pvalue < 0.05:
                        st.write(
                            "The difference is statistically significant (p < 0.05)"
                        )
                    else:
                        st.write(
                            "The difference is not statistically significant (p >= 0.05)"
                        )
                else:
                    st.write(
                        "Mann–Whitney U test requires two numerical variables. Please select other variables or a test."
                    )
            elif test_name == "Chi-square":
                cross_tab = pd.crosstab(
                    dataframe[columns_options[0]],
                    dataframe[columns_options[1]],
                    margins=True,
                )
                st.write("Contingency table:")
                st.write(cross_tab)

                cross_tab = cross_tab.drop("All", axis=1).drop("All", axis=0)
                stat, pvalue, _, _ = stats.chi2_contingency(cross_tab)

                st.write("Chi-Square test result:")
                st.write(f"Statistic = {stat}")
                st.write("p-value: ", pvalue)
                if pvalue < 0.05:
                    st.write("The difference is statistically significant (p < 0.05)")
                else:
                    st.write(
                        "The difference is not statistically significant (p >= 0.05)"
                    )


if __name__ == "__main__":
    try:
        main()
    except ParserError as ex:
        st.error(
            "An error occurred while trying to parse the dataframe. Check the file and try again."
        )
    except Exception as ex:
        st.exception(ex)
