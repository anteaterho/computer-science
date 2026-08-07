'''
a = input("숫자입력 : ")
b = 0

for i in range(len(a)):
    b += int(a[i])

print(b)
'''

n = int(input("숫자입력 : "))
sum = 0

while True:
    sum = sum + n % 10
    n = n // 10
    if n == 0:
        break
    
print(sum)