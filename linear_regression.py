import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (20.0, 10.0)

data = pd.read_csv('s.csv')
print(data.shape)
data.head()

#collecting x,y
x = data['temperaturemin'].values
y = data['temperaturemax'].values

#mean of x,y
mean_x = np.mean(x)
mean_y = np.mean(y)

m = len(x)

numerator = 0
denominator = 0

for i in range(m):
	numerator += (x[i] - mean_x) * (y[i] - mean_y)
	denominator += (x[i] - mean_x) ** 2

m = numerator / denominator
c = mean_y - (m * mean_x)

print "m = "+ str(m)
print "c = "+ str(c)

#plot reg line
max_x = np.max(x) + 100
min_x = np.min(x) - 100

xx = np.linspace(min_x, max_x, 1000)
yy = (m * xx) + c

plt.plot(xx, yy, color="red", label='regression line')
plt.scatter(xx, yy, c='yellow', label='scatter plot')

plt.xlabel('temperature_min')
plt.ylabel('temperature_max')
plt.legend()
plt.show()







