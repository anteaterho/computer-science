# [03. 반복제어문] ex_16
# 학습 목표: 여러 나머지 조건을 동시에 만족하는 수 찾기 + 최솟값 갱신 패턴

#a = input("a: ")
#b = input("b: ")

# a = int(a)
# b = int(b)

# for i in range(max(a,b), a*b+1, 1):
#     if i % a == 0 and i % b == 0:
#         lcm = i
#         break
# print(lcm)

# for i in range(1, b+1, 1):
#     if(a*i)%b == 0:
#         lcm=(a*i)
#         break
# print(lcm)


mn = 1000
for i in range(1, 400):
    if i % 4 == 2 and i % 6 == 4 and i % 9 ==7:
        #print(i, end=' ')
        #if i > 180 and i < 250:
        #    print(i)
        diff=abs(200-i)
        if diff < mn:
            mn=diff
            ans = i
print(ans)