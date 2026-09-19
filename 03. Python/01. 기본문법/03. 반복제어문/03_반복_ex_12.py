# [03. 반복제어문] ex_12
# 학습 목표: 자릿수 분해 — %10으로 끝자리를 떼고 //10으로 줄여 나가기

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