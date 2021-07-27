import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import plotly.graph_objs as go

# data
def getMedal(data):
    medal = data.dropna(subset=['Medal'])
    totalGoldMedals = medal.Team.value_counts().reset_index(name='Medal').head(10)
    x = totalGoldMedals['index']
    y = totalGoldMedals.Medal
    fig = go.FigureWidget(data=[go.Bar(x=[x],
                                       y=[y],
                                       name=x,
                                       marker={'color': y,
                                               'colorscale': 'Viridis'})
                                for x, y in zip(x, y)])
    fig.update_layout(
        title="Medals per Country",
        xaxis_title="Top 5 countries",
        yaxis_title="Number of Medals",
        font_family="Courier New",
        font_color="white",
        title_font_family="Times New Roman",
        title_font_color="white",
        legend_title_font_color="green"
    )
    fig.update_xaxes(title_font_family="Arial")
    return fig


def getGender(data):
    Summer = data[data['Season'] == 'Summer']
    gender = Summer.groupby(['Year', 'Sex']).count()
    Men = gender.xs('M', level=1)
    Women = gender.xs('F', level=1)
    # Create traces
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=Men.index, y=Men.ID,
                             mode='lines',
                             name='男性参与人数'))
    fig.add_trace(go.Scatter(x=Women.index, y=Women.ID,
                             mode='lines+markers',
                             name='女性参与人数'))

    return fig