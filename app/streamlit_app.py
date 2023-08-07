import pandas as pd
import streamlit as st


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

        testing_algorithms_options = st.multiselect(
            "Choose algorithms",
            options=[
                "A/B test",
                "t-test",
                "p-value",
                "u-test",
                "bootstraping",
                "chi-square",
            ],
            placeholder="Choose at least 2 algorithms",
        )

        if len(testing_algorithms_options) < 2:
            st.warning("You have to choose at least 2 algorithms")
            return


if __name__ == "__main__":
    main()
