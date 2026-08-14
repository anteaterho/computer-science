a = [85,92,88]
print(a)
print(a[2])

a.append(90)
print(a)

#a[2] = 33
a.insert(2,33)
print(a)

b= []
for i in range(len(a)):
    if a[i]%2==0:
        b.append(a[i])
print(b)