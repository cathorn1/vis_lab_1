import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')
df['date'] = pd.to_datetime(df['date'])

# Preparing data
# This line of code is prepping the data for the graph object, and telling it to
# log the dates on the x-axis by filtering the df by 'date', and then mapping the max temps to the y-axis
# by filtering the data by 'actual_max_temp'. It's also formatting the graph object to use a line to illustrate data
data = [go.Scatter(x=df['date'], y=df['actual_max_temp'], mode='lines', name='Max Temp')]

# Preparing layout
layout = go.Layout(title='Actual Max Temps from 2014-15', xaxis_title="Date",
                   yaxis_title="Max Temperature")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='linechart.html')
