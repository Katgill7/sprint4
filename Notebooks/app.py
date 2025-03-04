import streamlit as st
import plotly.figure_factory as ff
import numpy as np
import plotly.io as pio
import matplotlib.pyplot as plt
df_degrees = pd.read_csv('degrees-that-pay-back.csv')
st.header = 'Test'
fig2 = ff.create_distplot([df_degrees['Percent change from Starting to Mid-Career Salary']], group_labels=['Test2'])
