from my_plotly_script import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

die_1 = Die()
die_2 = Die()

# Make some rolls and store the result in a list
results = []

for num_roll in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyzing the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# visualizing the results
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of result'}
my_layout = Layout(title='Results of rolling two D6 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout':my_layout}, filename='d6.html')



# print(results)
print(frequencies)