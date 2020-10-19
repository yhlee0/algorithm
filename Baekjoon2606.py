'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : Baekjoon2606 Virus
	URL : https://www.acmicpc.net/problem/2606

'''


n = int(input())
nOfLine = int(input())
matrix = [[0]*(n + 1) for i in range(n + 1)]

for k in range(nOfLine):
  a, b = map(int,(input().split()))
  matrix[a][b] = matrix[b][a] = 1

def bfs(s):     # s = 시작정점
  queue = [s]
  visited = [s]
  while queue:
    current_node = queue.pop(0)  #꺼내고
    for c in range(1, n+1):   
      if(matrix[current_node][c] == 1 and (c not in visited)):
        visited.append(c)   #//visited += [c]
        queue.append(c)     #//queue =+ [c]
  return len(visited)-1

print(bfs(1))
