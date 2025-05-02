#use the scatter() method to draw plot diagram
import matplotlib.pyplot as plt

x=[5,7,8,7,2,17,2,9,4,11,12,9,6]
y=[99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x,y)
plt.show()

# Our data illustrate 100 customer in a shop and their shoping habits 
# the traing set should be a random selection of 88% of the original data
# the tesing set should be the reaming 28%

import numpy 
numpy.random.seed(2)

x=numpy.random.normal(loc=3,scale=1,size=100)
y=numpy.random.normal(loc=150,scale=40,size=100)/x


# the traing set should be a random selection of 88% of the original data 
# the tesing set should be the raming 

train_x=x[:80]
train_y=y[:80]

test_x=x[:80]
test_y=y[80:]


mymodel=numpy.poly1d(numpy.polyfit(train_x,train_y,deg=4))
myline=numpy.linspace(start=0,stop=6,num=100)

plt.scatter(train_x,train_y)
plt.plot(myline,mymodel(myline))
plt.show()

