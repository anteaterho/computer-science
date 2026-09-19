# [03. 반복제어문] ex_17
# 학습 목표: range의 증가폭을 음수로 줘서 거꾸로 세기

a = int(input("입력 : "))

for i in range(100, a-1, -1):
    print(i, end=" ")