# [01. 출력] ex_07
# 학습 목표: 변수를 넣어 구구단 한 줄 만들기 — .format()과 % 비교

dan = 5
num = 2

print("{} Dan". format(dan))
print("{} * {} = {}".format(dan, num, dan * num))
print("%d * %d = %d" % (dan, num, dan * num))