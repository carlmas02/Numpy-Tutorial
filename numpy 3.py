#initialing diff arrays
#to specialize data type
#dtype = "int32" or "int16 or "float16/32"



a = np.array([[1,2,3],[2,4,6]])
print(a)

#all 0s matrix
x = np.zeros((2,4))
print(x)

#all 1s matrix

y = np.ones((4,3,3), dtype = 'int16')
print(y)

#any number
m = np.full((2,4),24)
print(m)

#any other number(full_like)
u = np.full_like(a,52)
print(u)

#any random decimal number(ignore ths)
s = np.random.rand(4,2,3)
print(s)

#rand integers
d = np.random.randint(6,size = (4,5))
print(d)

#identity matix
f = np.identity(3)
print(f)

#repeat array
g = np.array([[1,2,3],[3,5,6]])
r1 = np.repeat(g,6,axis= 0)
print(r1)




