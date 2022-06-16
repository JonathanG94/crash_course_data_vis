
from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#create two D8 dice
die_1 = Die()
die_2 = Die()
die_3 = Die()

#Count number of dice
num_dice = len([i for i in dir() if isinstance(eval(i), Die)])

#make some rolls and store as a list

results = [die_1.roll() + die_2.roll() + die_3.roll() for roll_num in 
    range(50000)]

#Analyse the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(num_dice, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualise the results
x_values = list(range(num_dice, max_result + 1))
data = [Bar(x = x_values, y = frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title = 'Results of rolling three D6 50000 times', 
    xaxis = x_axis_config, yaxis = y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename = 'd6_d6_d6.html')