import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')
df['date'] = pd.to_datetime(df['date'])

# Preparing data
# These next 4 lines of code creating 3 traces, or categories, to map on the scatter plot.
# It always filters by the date for the x-axis, and filters the data for the different categories
# of max, min, and mean temp for the y-axis. Each trace is put into "line mode" and assigned a name.
# Traces are then sent to 'data' variable as an array to be plotted in the figure.
trace1 = go.Scatter(x=df['date'], y=df['actual_max_temp'], mode='lines', name='Max Temp')
trace2 = go.Scatter(x=df['date'], y=df['actual_min_temp'], mode='lines', name='Min Temp')
trace3 = go.Scatter(x=df['date'], y=df['actual_mean_temp'], mode='lines', name='Mean Temp')
data = [trace1, trace2, trace3]

# Preparing layout
layout = go.Layout(title='Max, Min, and Mean Temps from 2014-15', xaxis_title="Date",
                   yaxis_title="Degrees Fahrenheit")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='multilinechart.html')
