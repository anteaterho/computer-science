# [02. 입력] ex_04
# 학습 목표: 사칙연산 결과를 형식에 맞춰 출력하기 — 나눗셈(/)과 몫(//)의 차이

import math

a = input("첫 번째 숫자: ")
b = input("두 번째 숫자: ")

print("{} * {} = {}".format(a, b, int(a) * int(b)))
print("{} / {} = {:.2}".format(a, b, a/b))
#print("{} / {} = {}".format(a,b, int(a/b)))
#print("{} / {} = {}".format(a,b, (a//b)) #몫은 //
     
#print("{} / {} = {}".format(a, b, math.floor(int(a) / int(b), 2)))
#print("{} % {} = {}".format(a, b, int(a) % int(b)))
