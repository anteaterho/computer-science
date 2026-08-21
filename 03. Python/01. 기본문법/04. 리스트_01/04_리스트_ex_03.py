import random

score = []

for i in range(10):
    n = random.randint(1,100)
    score.append(n)

print(score)

score.sort()
score.reverse()
score.sort(reverse=True)
print(score)