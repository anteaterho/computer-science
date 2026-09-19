# [10. 딕셔너리_02] ex_07
# 학습 목표: zip()으로 두 리스트를 묶어 딕셔너리 만들기

fruits = ["apple", "banana", "orange", "kiwi"]
price = [1200, 1000, 900, 600]

kk = dict(zip(fruits, price)) # zip에 대해서 복습할 것

print(kk)