# [03. 반복제어문] ex_14
# 학습 목표: range로 홀수항과 짝수항을 나눠 제곱의 합 구하기

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