time_table = [4,8,2,5,4,6,7]
n = 4

# def solution(tb, n):
#     cnt = 0
#     tmp = []
#     for i in range(0,len(tb)):
#         if cnt < 4:
#             tmp.append(tb[i])
#             cnt +=1
#         return cnt

def solution(tb, n):
    cnt=[0]*n
    for i in range(len(tb)):
        cnt[i%n]+=tb[i]
    return max(cnt)

ret = solution(time_table, n)
print(ret)