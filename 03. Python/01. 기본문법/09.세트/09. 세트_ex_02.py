colors = 'yellow, red, blue, green, yellow, red'.split(', ')
colors = set(colors)

print(type(colors))
print(colors)

# remove를 쓸 때 discard 쓸 때 차이점
#colors.remove('green')
colors.discard('green')
print(colors)

