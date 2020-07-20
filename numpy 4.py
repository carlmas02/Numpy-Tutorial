#linear algebra


a = np.ones((2,3))
print(a)

b = np.full((3,2),2)
print(b)

#multiply (will only work if shapes are same)
#print(a*b)

#multiply inclusive of opp shape like(2,3) and (3,2)

x = np.matmul(a,b)

print(x)