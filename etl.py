import streamlit as st
import pandas as pd

data = {
        'Task' : ['Extract', 'Transform','Load'],
        'Status' : ['completed', 'INprogress', 'Pending']
}

df = pd.DataFrame(data)
st.write('ETL Pipeline execution Status', df)