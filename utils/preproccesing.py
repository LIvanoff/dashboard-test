import pandas as pd
import streamlit as st
from io import StringIO


def file_preprocces(df: pd.core.frame.DataFrame):
    names = df.columns.str.split(',')
    df = df.iloc[:, 0].str.split(',', expand=True)
    df.columns = names[0]
    df = df.rename(columns={'"Возраст"': 'age', '"Пол"': 'sex', 'Количество больничных дней': 'work_days'})
    df['age'] = df['age'].astype(str).astype(int)
    df['work_days'] = df['work_days'].astype(str).astype(int)

    for i in range(len(df['sex'])):
        if df.loc[i, 'sex'] == '"Ж"':
            df.loc[i, 'sex'] = 0
        else:
            df.loc[i, 'sex'] = 1

    return df

@st.cache_data
def load_data(uploaded_file):
    dataframe = pd.read_csv(uploaded_file)
    dataframe = file_preprocces(dataframe)
    return dataframe