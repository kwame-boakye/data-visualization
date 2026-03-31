"""
Plotly is a python package that allows you to create interactive visualizations

"""
# I am going to use the rolling die to explore the visualizatoins that plotly has to offer
from random import randint
class Die:

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)