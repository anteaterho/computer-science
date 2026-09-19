# [03. 반복제어문] ex_18
# 학습 목표: map(int, input().split())으로 두 값을 한 번에 받아 곱셈표 만들기

a, b = map(int, input().split())

for i in range(1,a+1):
    for j in range(1, b+1):
        print(i*j, end=" ")
    print()
