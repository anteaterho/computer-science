# [03. 반복제어문] ex_11
# 학습 목표: 수열의 합 구하기 — 반복문으로 항을 갱신하면서 누적하기

# 초항과 공차
'''
a1 = int(input())
d = int(input())
n = int(input())

sum =  a1

for i in range(0, n-1, d):
    a1 = a1 + d
    sum = sum+a1
    #print("{}번째 항의 값은 {}이고, 합은 {}입니다. ".format(n, i, s))
print(a1, sum)
'''

a1 = 4
r = 2/3
n = 2

sum = a1

for i in range(0, n-1, 1):
    a1 = a1 * r
    sum = sum+a1
    #print("{}번째 항의 값은 {}이고, 합은 {}입니다. ".format(n, i, s))
print(a1, sum)