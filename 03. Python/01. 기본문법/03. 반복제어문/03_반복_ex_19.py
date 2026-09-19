# [03. 반복제어문] ex_19
# 학습 목표: while문으로 상태를 갱신하며 조건을 만족할 때까지 걸린 횟수 세기

up, down, depth = map(int, input().split())
day = 0

while True:
    day += 1
    depth = depth-up
    if depth  <= 0:
        break
    depth = depth + down

print(day)