#indexing numpy

#get specific element[r,c]
y = a[1,2]
print(y)

#get a specific row
print(a[1,:])

#get a specific column
z = a[:,1]
print(z)

#get little more fancy[startindex :endindex:stepsize]
w = a[1,2:2]
print(w)

#change value
a[1,2] = 30
print(a)

#change column
a[:,2] =[20,60]
print(a)

#get specific element(work outside in)
b = np.array([[1,2,3],[2,4,6]])
q = b[0,0]
print(q)





