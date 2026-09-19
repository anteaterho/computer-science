# [09. 딕셔너리_01] 숙제_02
# 학습 목표: 달리기 경주 — 리스트 index() 대신 딕셔너리 두 개로 이름↔등수 양방향 지도 만들기

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

# players = ["mumu", "soe", "poe", "kai", "mine"]
# grade = []

# # for i in range(len(players)):
# #     grade.append[i]

# # print(grade)

# dic1 = dict(zip(players,list(range(0,len(players)))))

# print(dic1)

def solution(players, callings):
    
    dic1 = dict(zip(players,list(range(0,len(players)))))
    dic2 = dict(zip(list(range(0,len(players))), players))
    
    for i in callings:
        
        # 현재 선수의 위치
        pos = dic1[i]

        # 바로 앞 선수
        fore = dic2[pos-1]
        
        # 이름 -> 위치 갱신
        dic1[fore]=pos
        dic1[i]=pos-1
        
        # 위치 -> 이름 갱신
        dic2[pos]=fore
        dic2[pos -1]=i
    
    print(dic1)
    print(dic2)
    
    return dic2