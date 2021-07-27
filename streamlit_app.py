import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import plotly.graph_objs as go
from data.getData import getMedal, getGender

st.title('Olympic History Data Analysis')

st.write('A Web App by [Yueyuan He](https://github.com/heyueyuan)')
data = pd.read_csv("data/athlete_events.csv")

# Graphing Function #####
fig_medal = getMedal(data)

st.plotly_chart(fig_medal)

# Get_Gender
fig_gender = getGender(data)
st.plotly_chart(fig_gender)