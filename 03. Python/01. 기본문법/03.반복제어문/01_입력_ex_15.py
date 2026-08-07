k = int(input("k : "))
sum = 0

for k in range(4,11,1):
    sum = sum + (2*k-3)**2
for k in range(5,13,1):
    sum = sum + (2*k + 3)**3

print(sum)