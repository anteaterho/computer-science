# # 스왑 문제

# a = 1
# b = 2

# # 스왑

# # tmp = a
# # a = b
# # b = tmp
# a,b = b,a

# print(a,b)

# #리스트로 풀었을 경우
# ##----------------------------------

# def solution(players, callings):
#     for i in callings:
#         pos = players.index(i)
#         players[pos],players[pos-1]=players[pos-1],players[pos]
#     return players

players = ["mumu", "soe", "poe", "kai", "mine"]
grade = []

# for i in range(len(players)):
#     grade.append[i]

# print(grade)

dic1 = dict(zip(players,list(range(0,len(players)))))

print(dic1)