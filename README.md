# Data Profiling using Streamlit and Pandas <br>
[![Streamlit](https://badgen.net/pypi/v/streamlit)](https://pypi.org/project/streamlit/)
[![Pandas](https://badgen.net/pypi/v/pandas)](https://pypi.org/project/pandas/) 
[![pandas-profiling](https://badgen.net/pypi/v/pandas-profiling)](https://pypi.org/project/pandas-profiling/)
[![streamlit-pandas-profiling](https://badgen.net/pypi/v/streamlit-pandas-profiling)](https://pypi.org/project/streamlit-pandas-profiling/)
[![streamlit-aggrid](https://badgen.net/pypi/v/streamlit-aggrid)](https://pypi.org/project/streamlit-aggrid/)

:wave: This is going to be my one of many streamlit apps that I will be sharing in this year.

## About the App

* The code is using the Streamlit and Pandas libraries to create a web application that allows a user to either upload a file, provide a link to a file, or generate a default file. 
* The file can be in CSV, JSON, or Parquet format. 
* The user can then choose to profile either all of the variables in the file or a selected subset of them, and can also choose between a "minimal" and "complete" mode for the profiling.
* The code then creates an editable grid using the AgGrid library to display the data. 
* The user can then pin, edit, and profile columns in the grid. 
* Finally, the code creates a profile report using the pandas_profiling library and displays it using the st_profile_report function from the streamlit_pandas_profiling library.

## What is streamlit 

Streamlit lets you turn data scripts into shareable web apps in minutes, not weeks. It’s all Python, open-source, and free! And once you’ve created an app you can use our [Community Cloud platform](https://streamlit.io/cloud) to deploy, manage, and share your app!

![Example of live coding an app in Streamlit|635x380](https://raw.githubusercontent.com/streamlit/docs/main/public/images/Streamlit_overview.gif)

## Installation

```bash
pip install streamlit
streamlit hello
```

Streamlit can also be installed in a virtual environment on [Windows](https://github.com/streamlit/streamlit/wiki/Installing-in-a-virtual-environment#on-windows), [Mac](https://github.com/streamlit/streamlit/wiki/Installing-in-a-virtual-environment#on-mac--linux), and [Linux](https://github.com/streamlit/streamlit/wiki/Installing-in-a-virtual-environment#on-mac--linux).

## Getting started with the Code 

```python
from st_aggrid import AgGrid
import streamlit as st
import pandas as pd 
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport
```
