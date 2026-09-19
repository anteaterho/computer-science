# [03. 반복제어문] 숙제_03
# 학습 목표: 소수 판별 — 나눠떨어지는 수가 하나라도 있으면 break하는 flag 패턴

cnt = 0
sum = 0

for i in range(47,184,1):
  divisor = 0
  flag=0
  for j in range(2, i):
    if i%j==0:
      flag=1
      break
  if flag==0:
    print(i, end=' ')
    cnt += 1
    sum += i
    
print()
print(sum, cnt)