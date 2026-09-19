# [03. 반복제어문] 숙제_01
# 학습 목표: 3·6·9 게임 — 자릿수를 훑어 조건을 찾는 flag 패턴 익히기

# n = int(input(" 숫자 입력 : "))

# count = 0

# for i in range(1, n + 1):
    
#     s = str(i)

#     if '3' not in s and '6' not in s and '9' not in s:
#         print(i, end=", ")
#         count += 1


# print("total : ", count)

n=int(input("숫자 입력 : "))
cnt=0

for i in range(1,n+1,1):
  flag = 0
  for j in str(i):
    if j == '3'or j=='6' or j=='9':
      flag=1
      break
  if flag==0:
    print(i, end=', ')
    cnt+=1

print("total : ", cnt)