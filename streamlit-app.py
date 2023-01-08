from st_aggrid import AgGrid
import streamlit as st
import pandas as pd 
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport
from pathlib import Path


st.set_page_config(layout='wide', page_title="Pandas Profiling", page_icon= "./images/pandas.jpg") 

spacer1,col,space2 = st.columns((0.5,1,0.5))

with col:
    st.title(" Data Profiling using streamlit and pandas!")
    st.caption(" Developer - Vivek Kovvuru")
    st.markdown('''[![Streamlit App](https://badgen.net/pypi/v/streamlit)](https://pypi.org/project/streamlit/)
                 [![Github Link](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/vivkv07/streamlit-pandas-profiling)
                [![BymeaCoffee](https://badgen.net/badge/icon/buymeacoffee?icon=buymeacoffee&label)](https://www.buymeacoffee.com/vivekkovvuru)''')
    st.write("")
    st.write("")
    st.write("")
    st.write("")

col1,col2,col3,col4 = st.columns((0.35,0.4,1.2,0.35))
with col2: 
    upload_option = st.selectbox('Data Source', ('Upload File', 'Web Link', 'Use Demo Data'), help= "Supported Filetypes - csv, json, parquet")
    if upload_option == 'Web Link':
        uploaded_file = st.text_input('URL')
        st.warning("Please note that reading Data from web will take a while!")
    if upload_option == 'Upload File': 
        uploaded_file = st.file_uploader("Upload your file:", type=['csv', 'json', 'parquet'])
    elif upload_option == 'Use Demo Data':
        uploaded_file = 'https://storage.googleapis.com/tf-datasets/titanic/train.csv'


if uploaded_file is not None:
    if upload_option == 'Web Link' and uploaded_file == "":
        st.empty()
    else:
        if "csv" in str(uploaded_file): df=pd.read_csv(uploaded_file)
        elif "json" in str(uploaded_file): df=pd.read_json(uploaded_file)
        elif "parquet" in str(uploaded_file): df=pd.read_parquet(uploaded_file)
        else: 
            st.error("Unsupportable file format uploaded!")
            st.stop()

        with col2:
            st.write("")
            st.write("")
            st.write("")


            option1=st.radio(
            'Variables',
            ('Default', 'Selected'), horizontal= True, help= "By Default it considers all Variables to be Profiled")
            
            if option1=='Default':
                df=df
            
            elif option1=='Selected':
                var_list=list(df.columns)
                option3=st.multiselect(
                    'Select Variables to be included in profile',
                    var_list)
                df=df[option3]

            option2 = st.radio(
            'Mode',
            ('Minimal', 'Complete'), horizontal=True, help= "Complete mode may cause the app to run overtime or fail for large datasets due to computational limit")

            if option2=='Complete':
                mode='complete'
            elif option2=='Minimal':
                mode='minimal'
            button = st.button('Generate Report')


        with col3:
            st.caption("Columns can be pinned, edited, and profiled.")
            grid_response = AgGrid(
                    df,
                    editable=True, 
                    height=350, 
                    width='100%',
                    )

            updated = grid_response['data']
            df1 = pd.DataFrame(updated) 
        a, b, c = st.columns((0.5,2,0.5))
        if button:
            with a:
                
                if mode=='complete':
                    profile=ProfileReport(df,
                        title="Profile Report - " + str(uploaded_file),
                        progress_bar=True,
                        dataset={
                            "description": 'This profiling report was generated using streamlit app developed by Vivek Kv',
                            "copyright_holder": 'Vivek Kv',
                            "url": 'https://pandas-profiling.streamlit.app',
                            "copyright_year": '2023'
                        }) 
                    
                elif mode=='minimal':
                    profile=ProfileReport(df1,
                        minimal=True,
                        title="Profile Report - " + str(uploaded_file),
                        progress_bar=True,
                        dataset={
                            "description": 'This profiling report was generated using streamlit app developed by Vivek Kv',
                            "copyright_holder": 'Vivek Kv',
                            "url": 'https://pandas-profiling.streamlit.app',
                            "copyright_year": '2023'
                        }) 
                        
            with b:
                st.header(" Review and Download the HTML report!")
                export=profile.to_html()
                st.download_button(label="Download Full report", data=export, file_name='data-profile-report.html')
                st_profile_report(profile)

                st.info("End of the Report. Scroll up to Download!")

with col3:               
    with st.expander("Getting Started"):

        st.write((Path(__file__).parent/"README.md").read_text())   

