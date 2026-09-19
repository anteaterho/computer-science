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