# [06. 리스트_03] ex_03
# 학습 목표: ex_02의 코드를 def 함수로 바꾸기 — 매개변수와 return

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

