
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