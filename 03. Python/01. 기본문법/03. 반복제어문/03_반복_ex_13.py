# [03. 반복제어문] ex_13
# 학습 목표: 1부터 n까지 특정 숫자가 몇 번 나오는지 세기 — str()로 자릿수 훑기

# 1부터 입력받은 수까지 숫자 '1'의 갯수를 구하라.

# n = int(input("숫자입력 : "))
# cnt = 0

# for i in range(1,n+1,1):
#     while True:
#         if i % 10 == 1:
#             cnt = cnt + 1
#         i=i//10
#         if i == 0:
#             break

# print("총 : ", cnt)

# n = int(input("숫자 입력 : "))
# sum = 0

# for i in str(n):
#     sum = sum+int(i)
# print(sum)


n = int(input("숫자 입력 : "))

sum = 0

for i in range(1,n+1, 1):
    # i = 137
    for j in str(i):
        if j == 1:
            sum = sum + 1
print(sum)