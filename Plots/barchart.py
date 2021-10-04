import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Olympic2016Rio.csv')

# Filtering US Cases
# filtered_df = df[df['Country'] == 'US']
# filtered_df = df['NOC']

# Removing empty spaces from State column to avoid errors
# filtered_df = filtered_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
new_df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Creating sum of number of cases group by State Column
# new_df = filtered_df.groupby(['State'])['Confirmed'].sum().reset_index()
new_df = df.groupby(['NOC'])['Total'].sum().reset_index()

# Sorting values and select first 20 states
# new_df = new_df.sort_values(by=['Confirmed'], ascending=[False]).head(20)
new_df = df.sort_values(by=['Total'], ascending=[False]).head(20)

# Preparing data
# This line of code is defining the graph object to a bar chart and mapping the names of the country
# to the x-axis by filtering new_df by "NOC" and then mapping the total number of medals to the y-axis
# by filtering the df by 'Total'
data = [go.Bar(x=new_df['NOC'], y=new_df['Total'])]

# Preparing layout
layout = go.Layout(title='Olympic Medals Won By Country', xaxis_title="Name of Country",
                   yaxis_title="Total Medals")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='barchart.html')
