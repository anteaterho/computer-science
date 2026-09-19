#color = ("red", "blue","yellow","gray")
color = 'red, blue, yellow, gray'.split(', ')
print(tuple(color))
color = list(color)
color[2] = "orange"
color = tuple(color)
print(color)