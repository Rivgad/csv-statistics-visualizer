# CSV statisctics visualizer

This is a data visualization web application developed using Streamlit.
The application accepts a CSV file and allows the user to visualize the data distribution and apply statistical hypothesis tests.

## Table of Contents

- [Usage](#usage)
- [Installation](#installation)
  - [Installing and running Locally](#installing-and-running-locally)
  - [Running on Streamlit Community Cloud](#running-on-streamlit-community-cloud)


# Usage

To get started with application, the hosted on streamlit version of app can be used:

https://csv-statistics-visualizer.streamlit.app/

# Installation

<details>
<summary>

### Installing and Running Locally
</summary>

### Pre-requisites

- [Anaconda](https://www.anaconda.com/products/distribution)

### Steps:

1. Clone the repository
    ```
    git clone https://github.com/Rivgad/csv-statistics-visualizer
    cd csv-statistics-visualizer
    ```

2. Create a new Conda environment and activate it
    ```
    conda env create -f conda-env.yml
    conda activate csv-statistics-visualizer-env
    ```

3. Run the Streamlit app
    ```
    streamlit run app/streamlit_app.py
    ```
    or (for Windows)
    ```
    python -m streamlit run app/streamlit_app.py
    ```

</details>

<details>
<summary>

### Running on [Streamlit Community Cloud](https://share.streamlit.io/)
</summary>

1. Fork repository \*[click here](https://github.com/Rivgad/csv-statistics-visualizer/fork)\*

2. To deploy an app, click "New app" from the upper right corner of your workspace. ![Alt text](https://docs.streamlit.io/images/streamlit-community-cloud/deploy-empty-new-app.png)

3. Fill in:
    - Repository: %your_github_username%/csv-statistics-visualizer
    - Branch: main
    - Main file path: app/streamlit_app.py
4. Click 'Advanced settings...' and choose Python version 3.10
5. Click 'Deploy!'

</details>
