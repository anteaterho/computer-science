# [04. 리스트_01] ex_01
# 학습 목표: 리스트 만들기와 인덱싱, append와 insert의 차이, 조건에 맞는 원소만 골라 담기

a = [85,92,88]
print(a)
print(a[2])

a.append(90)
print(a)

#a[2] = 33
a.insert(2,33)
print(a)

b= []
for i in range(len(a)):
    if a[i]%2==0:
        b.append(a[i])
print(b)