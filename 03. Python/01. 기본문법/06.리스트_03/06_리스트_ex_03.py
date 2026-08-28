score = [90, 87, 87, 23, 35, 28, 12, 46]

def ranker(scroe):
    rank = [1]*len(score)
    for i in range(0,len(score)):
        for j in score:
            if score[i] < j:
                rank[i]+=1
    return rank

result = ranker(score)
print(result)

