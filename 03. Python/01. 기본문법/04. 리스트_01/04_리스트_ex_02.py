# [04. 리스트_01] ex_02
# 학습 목표: 원소 삭제 총정리 — remove / del / 슬라이스 삭제, 반복문 안에서 지울 때 인덱스가 밀리는 문제

a = [85,92,33,88,71,90]

# print(a)
# a.remove(88)
# print(a)
# #del a[2:5]
# del a[3]
# print(a)
# a.insert(3, 77)
# print(a)
#del a[1:5]
# for i in range(1,4,1):
#     del a[1]
# print(a)
# for i in range(3,0,-1):
#     del a[i]
# print(a)

del a[1:4]
print(a)