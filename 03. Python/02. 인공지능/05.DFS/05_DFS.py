grid_data = '''7
0110100
0110101
1110101
0000111
0100000
0111110
0111000'''

lines = grid_data.strip().split('\n')
n = int(lines[0])

apt=[]

for i in range(1, n+1):
    tmp = list(map(int,list(lines[i])))
    apt.append(tmp)

for row in apt:
    print(row)

visited=[[0] * n for _ in range(n)]
print("\n------ 방문 기록 배열 ---------")
print(visited)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(y,x):
    global cnt
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny <= n:
            if apt[ny][nx] == 1 and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                cut += 1
                dfs(ny,nx)

visited = [[0]* n for _ in range(n)]
ans = []

for i in range(n):
    for j in range(n):
        if apt[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            cnt = 1
            dfs(i,j)
            ans.append(cnt)

print("전체 단지 수",len(ans))
ans.sort()
for count in ans:
    print(count)