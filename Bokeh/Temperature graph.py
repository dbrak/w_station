import pandas as pd
from bokeh.plotting import figure
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.io import show, output_file
from Query import query


f = 'Temperature'


# Making Figure and Querying
p = figure(x_axis_type='datetime', x_axis_label='Datetime', y_axis_label='Temperature(ºC)',
           title="Graph to Show Temperuture over Time",
           toolbar_location=None)
q = query('Joe\'s Study', 'Humidity', '>', 40, f)

# Putting Data in Pandas Dataframee
data = pd.DataFrame.from_dict(q, orient='index', columns=[f, 'Time'])
data['Time'] = pd.to_datetime(data['Time'], unit='s')
data = data.sort_values('Time')

# Formatting Pandas
data['12h'] = data['Time'].apply(lambda x: x.strftime('%d-%m-%y %p'))
data['Average'] = data.groupby(['12h']).transform('mean')
data = data.drop_duplicates('12h')
data = data.drop([f, 'Time'], axis=1)
data['12h'] = pd.to_datetime(data['12h'], format = "%d-%m-%y %p")

print(data)

# Converting into Column Data sourse
mySource = ColumnDataSource(data)

# Drawing Graph And Putting Cirles on points
p.line(x='12h', y='Average', line_width=4, color='steelblue', source=mySource)
p.circle(x='12h', y='Average', fill_color='white', line_color='orangered', size=10, line_width=3, source=mySource)

# Adding Hovertool
p.add_tools(HoverTool(
    tooltips=[
        ('Datetime', '@12h'),
        (f, '@Average' + 'ºC'),
    ],

    formatters={
        'Time': 'datetime',
    },

))

# Outputting File And Showing it
output_file('Temp.html')
show(p)
