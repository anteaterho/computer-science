up, down, depth = map(int, input().split())
day = 0

while True:
    day += 1
    depth = depth-up
    if depth  <= 0:
        break
    depth = depth + down

print(day)