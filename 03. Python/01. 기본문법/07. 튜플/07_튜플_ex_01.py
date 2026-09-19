# [07. 튜플] ex_01
# 학습 목표: 튜플은 바꿀 수 없다 — 삭제와 수정이 왜 실패하는지 확인하기

a = (21,32,43,24,15)
print(a)
print(len(a))
print(list(a))
print(tuple(a))

# a.remove(43)
# del a[2]
# print(a)

print(a[3:5])