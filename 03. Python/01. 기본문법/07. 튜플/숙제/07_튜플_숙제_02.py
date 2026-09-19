# [07. 튜플] 숙제_02
# 학습 목표: 06장 숙제_01을 효율적으로 다시 풀기 — 문자열을 다 만들지 않고 필요한 길이에서 멈춰 위치 역산하기

# num = 2000000
# result = ''

# for i in range(1,num+1):
#   result += str(i)

# print(result)
# # print(result[10000000])
# # print(result[2345678])

i = 1
#n=1000000
num = ''
n=2345678
while True:
  num=num+str(i)
  if len(num)>n:
    last_num=str(i)
    diff=n-(len(num)-len(last_num))
    pre=i-1
    break
  i=i+1
print(num, len(num), last_num)
if diff==0:
  print(pre%10)
else:
  print(last_num[diff-1])