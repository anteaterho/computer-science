# [04. 리스트_01] ex_03
# 학습 목표: 난수로 리스트 채우기, sort()·reverse()·sort(reverse=True)의 차이

import random

score = []

for i in range(10):
    n = random.randint(1,100)
    score.append(n)

print(score)

score.sort()
score.reverse()
score.sort(reverse=True)
print(score)