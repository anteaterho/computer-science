# [06. 리스트_03] 숙제_01
# 학습 목표: 1부터 200만까지 이어 붙인 문자열에서 n번째 글자 찾기 — 되지만 아주 느린 풀이

num = 2000000
result = ''

for i in range(1,num+1):
  result += str(i)

#print(result)
print(len(result))
print(result[1000000])
print(result[2345678])