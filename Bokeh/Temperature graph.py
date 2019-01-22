import pandas as pd
from bokeh.plotting import figure
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.io import output_notebook, show, output_file
from Query import query



#Making Figure and Querying
p = figure(x_axis_type='datetime',x_axis_label='Datetime', y_axis_label='Temperature(ºC)', title="Graph to Show Temperuture over Time",
           toolbar_location=None)
q = query('Joe\'s Study', 'Humidity', '>',40, 'Temperature')


#Putting Data in Pandus Dataframee
data = pd.DataFrame(q, columns=['Time', 'Temperature'])
data['Time'] = pd.to_datetime(data['Time'], unit='s')
data = data.sort_values('Time')

#Converting into Column Data sours
mySource = ColumnDataSource(data)

#Drawing Graph And Putting Cirles on points
p.line(x='Time', y='Temperature', line_width=4, color='steelblue', source=mySource)
p.circle(x='Time', y='Temperature', fill_color='white', line_color='orangered', size=10, line_width=3, source=mySource)

#Adding Hovertool
p.add_tools(HoverTool(
    tooltips=[
        ('Time', '@Time'),
        ('Temperature', '@Temperature' + 'ºC'),
    ],

    formatters={
        'Time': 'datetime',
    },

    mode= 'vline'
))

#Outputting File And Showing it
output_file('Temp.html')
show(p)
