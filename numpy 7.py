

#load data from file
file_info = np.genfromtxt('filename.txt',delimiter = "," )
a =file_info.astype('int32')
print(a)

# boolean maskingg and advanced indexing
y = file_info<50
print(y)

w = file_info[file_info>50]
print(w)

#you can index with a list
b = np.array([1,3,5,7,9])
print(b[[1,4,3]])


#imp
q = ((file_info< 50) & (file_info > 20 ))
print(q)