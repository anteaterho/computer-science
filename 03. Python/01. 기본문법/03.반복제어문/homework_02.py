# '''
# 첫 번째 시도   ██████████████  14층 이동
# 두 번째 시도   █████████████   13층 이동
# 세 번째 시도   ████████████    12층 이동
# 네 번째 시도   ███████████     11층 이동
#                ...
# 마지막 시도    █               1층 이동

#               전부 합치면 105층
# 계란 떨어뜨리기 문제(Egg Dropping Problem).
# 최악의 경우를 최소화하는 최적화 전략(미니맥스(minimax))적인 접근이 필요
# '''

# total = 0
# count = 0

# while total < 100:
#     count += 1
#     total += count

# print(count)

# -----------------------------------------------------------------

h = 100

for cnt in range(7,101,1):
  height = h
  flag = 0
  count = cnt
  while True:
    height=height-cnt
    if height <= 0:
      flag = 1
      break
    cnt=cnt-1
    if cnt == 0:
      break
  if flag == 1:
    break
print(count)