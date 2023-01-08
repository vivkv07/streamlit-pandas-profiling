# Data Profiling using Streamlit and Pandas <br>
[![Streamlit](https://badgen.net/pypi/v/streamlit)](https://pypi.org/project/streamlit/)
[![Pandas](https://badgen.net/pypi/v/pandas)](https://pypi.org/project/pandas/) 
[![pandas-profiling](https://badgen.net/pypi/v/pandas-profiling)](https://pypi.org/project/pandas-profiling/)
[![streamlit-pandas-profiling](https://badgen.net/pypi/v/streamlit-pandas-profiling)](https://pypi.org/project/streamlit-pandas-profiling/)
[![streamlit-aggrid](https://badgen.net/pypi/v/streamlit-aggrid)](https://pypi.org/project/streamlit-aggrid/)

## About the App
![Example of live coding an app in Streamlit|635x380](https://github.com/vivkv07/streamlit-pandas-profiling/blob/main/images/demo.gif?raw=true)

* The code is using the Streamlit and Pandas libraries to create a web application that allows a user to either upload a file, provide a link to a file, or generate a default file. 
* The file can be in CSV, JSON, or Parquet format. 
* The user can then choose to profile either all of the variables in the file or a selected subset of them, and can also choose between a "minimal" and "complete" mode for the profiling.
* The code then creates an editable grid using the AgGrid library to display the data. 
* The user can then pin, edit, and profile columns in the grid. 
* Finally, the code creates a profile report using the pandas_profiling library and displays it using the st_profile_report function from the streamlit_pandas_profiling library.

### What is streamlit 

Streamlit lets you turn data scripts into shareable web apps in minutes, not weeks. It’s all Python, open-source, and free! And once you’ve created an app you can use our [Community Cloud platform](https://streamlit.io/cloud) to deploy, manage, and share your app!

### Installation

```bash
pip install streamlit
streamlit hello
```

Streamlit can also be installed in a virtual environment on [Windows](https://github.com/streamlit/streamlit/wiki/Installing-in-a-virtual-environment#on-windows), [Mac](https://github.com/streamlit/streamlit/wiki/Installing-in-a-virtual-environment#on-mac--linux), and [Linux](https://github.com/streamlit/streamlit/wiki/Installing-in-a-virtual-environment#on-mac--linux).

### Use streamlit run
Once you've cloned the repo, the easiest way to run it is with streamlit run:
```bash
streamlit run streamlit_app.py 
```

As soon as you run the script as shown above, a local Streamlit server will spin up and your app will open in a new tab in your default web browser.

### Pass a URL to streamlit run
You can also pass a URL to streamlit run! This is great when your script is hosted remotely, such as a GitHub Gist.
```bash
streamlit run https://raw.githubusercontent.com/vivkv07/streamlit-pandas-profiling/main/streamlit-app.py
```

### Run App Using Streamlit as a Python module
Another way of running Streamlit is to run it as a Python module. This is useful when configuring an IDE like PyCharm to work with Streamlit:

```bash
# Windows:
python -m streamlit run streamlit_app.py
```


```bash
# Linux/MacOS:
streamlit run your_script.py
```

## Run the app using DockerFile
### Build a Docker image
The docker build command builds an image from a Dockerfile . Run the following command from the app/ directory on your server to build the image:

```bash
docker build -t streamlit .
```

The -t flag is used to tag the image. Here, we have tagged the image streamlit. If you run:

```bash
docker images
```
You should see a streamlit image under the REPOSITORY column. For example:
```bash
REPOSITORY   TAG       IMAGE ID       CREATED              SIZE
streamlit    latest    70b0759a094d   About a minute ago   1.02GB
```

### Run the Docker container
Now that you have built the image, you can run the container by executing:
```bash
docker run -p 8501:8501 streamlit
```
The -p flag publishes the container’s port 8501 to your server’s 8501 port.

If all went well, you should see an output similar to the following:
```bash
$ docker run -p 8501:8501 streamlit
  
  You can now view your Streamlit app in your browser.

  URL: http://0.0.0.0:8501
```
To view your app, you can browse to http://0.0.0.0:8501 or http://localhost:8501

