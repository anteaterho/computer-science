# k = int(input("k : "))
# a = 0
# b = 0

# for k in range(1, 11, 1):
#     a = a + (2*k-1)**2
# for k in range(1, 11, 1):
#     b = b + (2*k)**2

# print(a + b)

k = int(input("k : "))
sum = 0

for k in range(1, 11, 1):
    sum = sum + (2*k-1)**2
for k in range(1, 11, 1):
    sum = sum + (2*k)**2

print(sum)