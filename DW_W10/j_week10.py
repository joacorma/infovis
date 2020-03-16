import pandas as pd
import statistics
import plotly.express as px
import plotly.graph_objects as go

def get_color(med):
    if med > 20:
        return 'indianred'
    else:
        return 'lightseagreen'

dataUrl = 'https://query.data.world/s/tpokqgljmatzv4wflmoakhnio352ma'
title = '2020/W10: #Viz5 - Violence Against Women & Girls'

df = pd.read_csv(dataUrl)


questions = df['Question'].unique()

fig = go.Figure()

for i in range(0,6):
    question = questions[i]
    query = "Question == '" + question + "'"
    values = df.query(query)['Value']
    color = get_color(values.median())
    fig.add_trace(go.Box(x=values, name=question,
                        boxpoints='all',
                        pointpos=0,
                        marker_color = color))

fig.update_layout(title=title)

fig.show()

