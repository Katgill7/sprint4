import streamlit as st 
import pandas as pd 
import plotly.express as plt
df_degrees = pd.read_csv('degrees-that-pay-back.csv')
df_degrees.columns = df_degrees.columns.str.replace(' ', '_')
df_degrees.columns = df_degrees.columns.str.lower()
df_degrees['starting_median_salary'] = df_degrees['starting_median_salary'].replace('[\$,]', '', regex=True).astype(float).astype(float)
st.header('Is College Worth It?')
df_degrees.plot(
    y='starting_median_salary',
    x='undergraduate_major',
    ylabel='Starting Median Salary in Dollars',
    xlabel='Undergrad Major',
    title='Starting Salaries for Undergraduate Degree',
    kind='bar'
)