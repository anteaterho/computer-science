# [09. 세트_02] ex_02
# 학습 목표: set()으로 중복 제거하기, remove와 discard의 차이

colors = 'yellow, red, blue, green, yellow, red'.split(', ')
colors = set(colors)

print(type(colors))
print(colors)

# remove를 쓸 때 discard 쓸 때 차이점
#colors.remove('green')
colors.discard('green')
print(colors)
