# [06. 리스트_03] ex_02
# 학습 목표: 등수 매기기 — 초기 리스트를 만드는 세 가지 방법과 이중 루프

score = [90, 87, 87, 23, 35, 28, 12, 46]
rank=[]

for i in range(len(score)):
    rank.append(1)
print(rank)

# rank=[1 for i in range(len(score))]
# print(rank)

# rank=[1]*len(score)
# print(rank)

for i in range(0,len(score)):
    for j in score:
        if score[i] < j:
            rank[i]+=1
print(rank)