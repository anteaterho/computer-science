# [09. 세트_02] 과제풀이
# 학습 목표: 08장 숙제(중복 제거)를 다시 풀기 — set()을 쓰면 어떻게 달라지는지 비교해 보기

language='c++, python, C, python, C++, C'.split(', ')

rs=[]

for i in language:
    if i not in rs:
        rs.append(i)

print(rs)