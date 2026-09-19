# [07. 튜플] ex_02
# 학습 목표: 튜플의 값을 바꾸려면 list()로 바꿔 고치고 다시 tuple()로 되돌린다

#color = ("red", "blue","yellow","gray")
color = 'red, blue, yellow, gray'.split(', ')
print(tuple(color))
color = list(color)
color[2] = "orange"
color = tuple(color)
print(color)