# if data not fit for linear regression (straight line), maybe use polymonial

import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

# NumPy has a method that lets us make a polynomial model
model = numpy.poly1d(numpy.polyfit(x, y, 3))

draw_line = numpy.linspace(1, 22, 100)

plt.scatter(x, y)
plt.plot(draw_line, model(draw_line))
plt.show() 


# r2 quare = how well the relationship between the values of the x- and y-axis is, if there are no relationship the polynomial regression can not be used to predict anything.
r2score = r2_score(y, model(x)) # The r-squared value ranges from 0 to 1, where 0 means no relationship, and 1 means 100% related.
print(r2score)