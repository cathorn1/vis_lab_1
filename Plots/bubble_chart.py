import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Datasets/Weather2014-15.csv')
# Removing empty spaces from State column to avoid errors
# df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Creating unrecovered column
# df['Unrecovered'] = df['Confirmed'] - df['Deaths'] - df['Recovered']

# Removing China and Others from data frame
# df = df[(df['Country'] != 'China') & (df['Country'] != 'Others')]

# Creating sum of number of cases group by Country Column
# new_df = df.groupby(['Country']).agg(
#    {'Confirmed': 'sum', 'Recovered': 'sum', 'Unrecovered': 'sum'}).reset_index()

new_df = df.groupby(['date']).agg(
    {'average_min_temp': 'sum', 'average_max_temp': 'sum'}).reset_index()

# Preparing data
# This block of code maps the average_max_temp and average_min_temp categories to the x- and y-axis
# on the Scatter plot respectively. It puts the graph object into 'markers' mode, assigns the date category from the
# data file to the hover text, and also sets the size and color scales of the markers.
data = [
    go.Scatter(x=new_df['average_max_temp'],
               y=new_df['average_min_temp'],
               text=new_df['date'],
               mode='markers',
               marker=dict(size=new_df['average_max_temp']/5, color=new_df['average_max_temp'], showscale=True))
]

# Preparing layout
layout = go.Layout(title='Average Max and Min Temps from 2014-15', xaxis_title="Average Max Temp",
                   yaxis_title='Average Min Temp', hovermode='closest')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubblechart.html')