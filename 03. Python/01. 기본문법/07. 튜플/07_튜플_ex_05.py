# [07. 튜플] ex_05
# 학습 목표: 언패킹 실전 — 최고점과 최저점을 빼고 평균 내기

#언팩의 사용법

import random

recode = []
for i in range(10):
    recode.append(random.randint(6000,10000)/100)

# print(record)

# record.sort()
# print(record)

# score = sum(record[0:-1])/8
# print("score {:.2f}".format(score))

recode = tuple(recode)
recode = list(recode)
recode.sort()
a, *b, c = recode # 언팩 *는 나머지 부분.
print("{:.1f}". format(sum(b)/len(b)))
