import numpy as np

cupcakes = np.array([2, .75, 2, 1, .5])

recipes = np.genfromtxt('recipes.csv', delimiter=',')
print(recipes)