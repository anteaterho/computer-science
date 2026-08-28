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