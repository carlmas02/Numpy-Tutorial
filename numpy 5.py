import numpy as np

#statistics

stats = np.array([[1,2,3],[4,5,6]])
print(stats)

#min
x = np.min(stats)
print(x)

#max
x = np.max(stats,axis = 1)
y = np.max(stats)

print(x)
print(y)


