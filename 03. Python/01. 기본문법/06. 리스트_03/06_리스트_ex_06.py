
votes = [3,2,2,3,1,1,2,1,1,3]

# def solustion(vote):
#     first = 0
#     second = 0
#     for i in range(0,len(vote)):
#         if vote[i] == 1:
#             first += 1
#         elif vote[i] == 3:
#             second += 1

def solution(votes):
    cnt=[0]*(3+1)
    for i in votes:
        cnt[i]+=1
    return [cnt.index(max(cnt)),max(cnt)]

ret = solution(votes)
print(ret)