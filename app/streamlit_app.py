import pandas as pd
import streamlit as st
from pandas.errors import ParserError
import plotly.express as px
from scipy import stats


def main():
    with st.echo(code_location="below"):
        uploaded_file = st.file_uploader(
            "Load dataset (*.csv)", ["csv"], accept_multiple_files=False
        )

        if uploaded_file is not None:
            dataframe = pd.read_csv(uploaded_file)
            st.write(dataframe[:5])
        else:
            return

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

        if st.button("Show distplots"):
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

        testing_algorithm_option = st.selectbox(
            "Choose algorithms",
            options=[
                "Welch's t-test",
                "Mann–Whitney U test",
                "chi-square",
            ],
            placeholder="Choose algorithm",
        )

        if len(testing_algorithms_options) < 2:
            st.warning("You have to choose at least 2 algorithms")
            return


if __name__ == "__main__":
    try:
        main()
    except ParserError as ex:
        st.error(
            "An error occurred while trying to parse the dataframe. Check the file and try again."
        )
    except Exception as ex:
        st.exception(ex)
