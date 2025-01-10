import numpy
from sklearn.metrics import r2_score


numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

model = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

r2 = r2_score(train_y, model(train_x))
# 0.809 shows that the model fits the training set
print(r2) 

r2 = r2_score(test_y, model(test_x))
# 0.809 shows that the model fits the testing set as well
print(r2)