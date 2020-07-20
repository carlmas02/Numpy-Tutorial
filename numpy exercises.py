#1 make this array using initializing methods
#11111
#10001
#10901
#10001
#11111


a = np.ones((5,5))

x = np.zeros((3,3))
print(x)
x[1,1] = 9
print(x)

a[1:4,1:4] = x
print(a)

#be careful while copying arrays
a = np.array([1,2,3])
b= a
#this is wrong
#prper approach
b = a.copy()
print(b)


#we can also add subtract
c = a +1
print(c)


#take sin cos etc.
x = np.sin(a)
print(x)
