from plotly import Die

die = Die()

# Make some rolls and store the result in a list
results = []

for num_roll in range(100):
    result = die.roll()
    results.append(result)

print(results)