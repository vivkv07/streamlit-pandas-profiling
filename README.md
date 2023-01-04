# streamlit-pandas-profiling
<br>
[![Streamlit](https://badgen.net/pypi/v/streamlit)](https://pypi.org/project/streamlit/)
[![Pandas](https://badgen.net/pypi/v/pandas)](https://pypi.org/project/pandas/) <br>
[![pandas-profiling](https://badgen.net/pypi/v/pandas-profiling)](https://pypi.org/project/pandas-profiling/)
* The code is using the Streamlit and Pandas libraries to create a web application that allows a user to either upload a file, provide a link to a file, or generate a default file. 
* The file can be in CSV, JSON, or Parquet format. 
* The user can then choose to profile either all of the variables in the file or a selected subset of them, and can also choose between a "minimal" and "complete" mode for the profiling.
* The code then creates an editable grid using the AgGrid library to display the data. 
* The user can then pin, edit, and profile columns in the grid. 
* Finally, the code creates a profile report using the pandas_profiling library and displays it using the st_profile_report function from the streamlit_pandas_profiling library.


```python
from st_aggrid import AgGrid
import streamlit as st
import pandas as pd 
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport
```
