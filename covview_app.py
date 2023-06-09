

import streamlit as st
import pandas as pd

st.set_page_config(
     page_title="Visualize COVID-19 cases and deaths App",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
 )


# @st.cache
cov=pd.read_csv('WHOcov_cleaned.csv',index_col=0)
# cov = st.cache(pd.read_csv)("WHOcov_cleaned.csv",index_col=0)

cov['Datetime']=pd.to_datetime(cov['Date'])
cov['Date']=cov['Datetime'].apply(lambda x: x.strftime('%y-%m-%d'))

# set index for linechart
cov.set_index('Datetime',inplace=True)

col=['Date', 'Country', 'WHO_region', 'Cumulative_cases', 'New_cases',
        'Cumulative_deaths', 'New_deaths']

cov_disp=cov[col]

sorted_country = sorted(cov_disp['Country'].unique())

# Sidebar - title & filters
st.sidebar.header('Data Filters')
selected_countries = st.sidebar.selectbox('Country', sorted_country)

cov_disp = cov_disp[cov_disp['Country'].isin([selected_countries])]

st.title('daily number of new reported COVID-19 cases and deaths worldwide')

col1, col2 = st.columns([1.68, 1])

col1.subheader("New Cases")
col1.line_chart(cov_disp.New_cases)

col2.subheader("Cumulative Cases")
col2.line_chart(cov_disp.Cumulative_cases)

col3, col4 = st.columns([1.68, 1])

col3.subheader("New Deaths")
col3.line_chart(cov_disp.New_deaths)

col4.subheader("Cumulative Deaths")
col4.line_chart(cov_disp.Cumulative_deaths)

