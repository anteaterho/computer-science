language='c++, python, C, python, C++, C'.split(', ')

rs=[]

for i in language:
    if i not in rs:
        rs.append(i)

print(rs)