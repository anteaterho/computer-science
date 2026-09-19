# [03. 반복제어문] ex_10
# 학습 목표: random으로 주사위 굴리기 + while True와 elif 분기로 보드게임 만들기


import random

'''
for i in range(0,10):
    n = random.randrange(1,7)
    print(n, end=' ')
'''

while True:
    n = random.randint(1,6)

    if n == 1:
        print("1 : 종료")
        break
    elif n == 3:
        print("3 : 통행료 지불")
    elif n == 5:
        print("5 : 건물 건축")
    else:
        print("PASS")