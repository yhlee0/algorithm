'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : Baekjoon2667 apartment complex numbering
	URL : https://www.acmicpc.net/problem/2606

'''


import sys

n=int(sys.stdin.readline())
a=[list(sys.stdin.readline()) for _ in range(n)]
cnt=0
apt=[]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def dfs(x,y):
    global cnt
    a[x][y] = '0' #방문한 곳은 0으로
    cnt+=1
    for i in range(4):
        nx = x + dx[i] #i=0일때 (nx,ny)는 좌 , i=1일때 (nx,ny)는 상
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >=n:
            continue
        if a[nx][ny] == '1':
            dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if a[i][j] == '1':
            cnt= 0
            dfs(i,j)
            apt.append(cnt)

print(len(apt))
apt.sort()
for i in apt:
    print(i)
    
