# [03. 반복제어문] ex_09
# 학습 목표: 이중 for문 — 바깥 루프가 한 번 돌 때 안쪽 루프는 전체를 돈다

'''
a = int(input())

for i in range(a, 100):
    a = a + i

print(a)
'''
a = 0
for j in range(0,5,1):
    #print("\n")
    for i in range(2,7,1):
        print(i+j, end = " ")
    print()