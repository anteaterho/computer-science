n,m=map(int, input().split())
canvas=[]

for i in range(n):
    tmp=list(map(int, input().split()))
    canvas.append(tmp)
print(canvas)

visited =[[0]*m for _ in range(n)]

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def dfs(y,x):
  global cnt
  for k in range(4):
    nx=x+dx[k]
    ny=y+dy[k]
    if 0 <= nx and 0<=ny<n:
      if canvas[ny][nx]==1 and canvas[ny][nx]==0:
        visited[ny][nx]=1
        cnt+=1
        dfs(ny,nx)

cnt=0
gcnt=[]

for i in range(n):
  for j in range(m):
    if canvas[i][j]==1 and visited[i][j]==0:
      cnt+=1
      visited[i][j]=1
      dfs(i,j)
      gcnt.append(cnt)
      cnt=0

print(gcnt)
print(max(gcnt))