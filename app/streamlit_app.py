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


if __name__ == "__main__":
    main()
