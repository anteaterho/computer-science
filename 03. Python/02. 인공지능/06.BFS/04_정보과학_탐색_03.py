# dfs 연습
# https://cafe.naver.com/f-e/cafes/29899143/articles/2241?menuid=19&referrerAllArticles=false&page=8

# n,m=5,6

# canvas=[[0]*m for _ in range(n)]
# #print(canvas)

# num = 1


# y,x = 0,0

# dx=[1,0,-1,0]
# dy=[0,1,0,-1]
# canvas[y][x]=num
# num+=1

# while num <= n*m:
#     for k in range(4):
#         nx=x+dx[k]
#         ny=y+dy[k]
#         while 0 <= nx < m and 0 <= ny < n and canvas[ny][nx] == 0:
#             canvas[ny][nx]=num
#             num+=1
#             x,y=nx,ny
#             nx=x+dx[k]
#             ny=y+dy[k]

# print(canvas)


#==================================================================
# 1번 문제(https://cafe.naver.com/f-e/cafes/29899143/articles/2214?menuid=19&referrerAllArticles=false&page=8)를 bfs로 다시 푼다.
# dq, 자료구조
# 자료구조에서 DQ(Deque, 디큐 또는 덱)는 Double-Ended Queue의 약자로, 양쪽 끝(앞과 뒤) 모두에서 데이터의 삽입과 삭제가 가능한 선형 자료구조입니다.
#스택(Stack)의 특징과 큐(Queue)의 특징을 모두 가지고 있는 일종의 '혼종' 자료구조이기도 합니다.
#1. 주요 특징
#• 양방향 연산: 한쪽으로만 넣고 뺄 수 있는 큐와 달리, 앞(Front)과 뒤(Rear) 어디서든 데이터를 넣고 뺄 수 있습니다.
#• 스택과 큐의 결합: 앞쪽을 막고 뒤쪽만 쓰면 스택(LIFO)처럼 동작하고, 앞과 뒤를 각각 입력과 출력으로 고정하면 큐(FIFO)처럼 동작합니다.
#• 독립된 입력/출력 제한: 목적에 따라 한쪽의 입력을 제한하는 스크롤(Scroll)이나, 한쪽의 출력을 제한하는 쉘프(Shelf) 형태로 변형해 쓸 수 있습니다

n=int(input())
apt=[]
for i in range(n):
    apt.append(input())
print(apt)

visited = [[0]*n for i in range(n)]

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def bfs(y,x):
    global cnt
    dq = [(y,x)]
    while dq!=[]:
        y,x = dq.pop(0)
        cnt+=1
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<= ny < n:
                if apt[ny][nx] == '1' and visited[ny][nx]==0:
                    visited[ny][nx]=1
                    dq.append([ny,nx])

cnt=0
gcnt=[]
for i in range(n):
    for j in range(n):
        if apt[i][j] == '1' and visited[i][j]==0:
            visited[i][j] = 1
            bfs(i,j)
            gcnt.append(cnt)
            cnt=0

gcnt.sort()
for c in gcnt:
    print(c)


# 숙제 https://cafe.naver.com/f-e/cafes/29899143/articles/2214?menuid=19&referrerAllArticles=false&page=8
# 최종 보스? https://cafe.naver.com/f-e/cafes/29899143/articles/2445?menuid=19&referrerAllArticles=false&page=7