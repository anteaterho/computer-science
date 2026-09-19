# [02. 입력] ex_05
# 학습 목표: ord()와 chr()로 문자와 아스키 코드 번호 사이를 변환하기

a = int(input())
b = input()

print(a + 1)
tmp = ord(b)
#print(chr(ord(b)+1))
print(chr(tmp + 1))