import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')

# Preparing data
# This block of code creates a heatmap graph object based of the actual_max_temp category for the day of week
# and month of year from the data folder. It also sets the color scheme.
data = [go.Heatmap(x=df['day'],
                   y=df['month'],
                   z=df['actual_max_temp'].values.tolist(),
                   colorscale='Jet')]

# Preparing layout
layout = go.Layout(title='Actual Max Temps from 2014-15', xaxis_title="Day of Week",
                   yaxis_title="Month of Year")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='heatmap.html')
