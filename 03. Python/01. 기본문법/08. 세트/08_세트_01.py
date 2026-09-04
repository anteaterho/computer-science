a = [1,2,3,4,6,8,12,24]
b = [1,2,3,4,6,9,12,18,36]

c = []
for i in a:
    if i in b:
        c.append(i)

#print(c)

d = a+[]
# for i in b:
#     if i != a:
#         d.append(i)
# print(d)

# for i in b:
#     if i not in a:
#         d.append(i)

# print(d)

e=[]

for i in a:
    if i not in b:
        e.append(i)

print(e)