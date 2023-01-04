from st_aggrid import AgGrid
import streamlit as st
import pandas as pd 
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport

st.set_page_config(layout='wide', page_title="Pandas Profiling", page_icon= "./pandas.jpg") 

spacer1,col,space2 = st.columns((0.3,1,0.1))
with col:
    st.title(" Data Profiling using streamlit and pandas!")
    st.caption(" Developer - Vivek Kovvuru")
    st.markdown('''[![Streamlit App](https://badgen.net/pypi/v/streamlit)](https://pypi.org/project/streamlit/)
                 [![Github Link](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/vivkv07/streamlit-pandas-profiling)
                [![BymeaCoffee](https://badgen.net/badge/icon/buymeacoffee?icon=buymeacoffee&label)](https://www.buymeacoffee.com/vivekkovvuru)''')
    st.write("")
    st.write("")
    st.write("")


col1,col2,col3 = st.columns((0.5,0.1,1.2))
with col1: 
    upload_option = st.selectbox('Data Source', ('Upload File', 'Web Link', 'Auto Generate'), help= "Supported Filetypes - csv, json, parquet")
    if upload_option == 'Web Link':
        uploaded_file = st.text_input('URL')
        st.warning("Please note that reading Data from web will take a while!")
    if upload_option == 'Upload File': 
        uploaded_file = st.file_uploader("Upload your file:", type=['csv', 'json', 'parquet'])
    elif upload_option == 'Auto Generate':
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
        a,b,c,d = st.columns(4)
        with col1:
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
        with col1:
            option2 = st.radio(
            'Mode',
            ('Minimal', 'Complete'), horizontal=True, help= "Complete mode may cause the app to run overtime or fail for large datasets due to computational limit")

            if option2=='Complete':
                mode='complete'
            elif option2=='Minimal':
                mode='minimal'

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
        with col1: button = st.button('Generate Report')
        a, b, c = st.columns((0.5,2,0.5))
        if button:
            with a:
                
                if mode=='complete':
                    profile=ProfileReport(df,
                        title="User uploaded table",
                        progress_bar=True,
                        dataset={
                            "description": 'This profiling report was generated using streamlit app developed by Vivek Kv',
                            "copyright_holder": 'Vivek Kv',
                            "url": 'https://indian-elections.streamlit.app',
                            "copyright_year": '2023'
                        }) 
                    
                elif mode=='minimal':
                    profile=ProfileReport(df1,
                        minimal=True,
                        title="User uploaded table",
                        progress_bar=True,
                        dataset={
                            "description": 'This profiling report was generated using streamlit app developed by Vivek Kv',
                            "copyright_holder": 'Vivek Kv',
                            "url": 'https://indian-elections.streamlit.app',
                            "copyright_year": '2023'
                        }) 
                        
            with b:
                st_profile_report(profile)
                export=profile.to_html()
                st.download_button(label="Download Full Report", data=export, file_name='data-profile-report.html')

            with c:
                export=profile.to_html()
                st.download_button(label="Download Report", data=export, file_name='data-profile-report.html')
