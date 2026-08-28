# 풀이
a = [1, 2, 3, 4, ['a', 'b', ['Life', 'is', 'too', 'short']]]

# tmp = a[-1][-1]
# del a[-1]
# print(a)
# a.append(tmp)
# print(a)
# a.append(6)
# a.append(9)
# print(a)

# b=[23,4,343,24,2342]
# b+=[10,20,30]
# print(b)

a[-1]=a[-1][-1]
a+=[6,9]
print(a)