# [05. 리스트_02] 숙제_예습_01
# 학습 목표: 리스트 안에 리스트 넣기 — append는 통째로 원소 하나로 들어간다

a = [1,2,3,4]
#tmp = ['a','b','c']
tmp=list('abc')

a.append(tmp)

print(a[4][1])