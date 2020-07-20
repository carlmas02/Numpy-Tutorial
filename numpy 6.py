import numpy as np

#reorganizing arrays

a = np.array([[1,2,3,4],[5,6,7,8]])
print(a)

#to re-shape

b = a.reshape((4,2))
x = a.reshape((8,1))

print(b)
print(x)

#vertically stacking matrices
c = np.array([[1,2,3]])
d = np.array([[3,4,5]])

q = np.vstack([c,d])

print(q)

#horizontal stacking matrices
y = np.hstack([d,c])
print(y)