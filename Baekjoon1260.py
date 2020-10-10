'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : Baekjoon1260 DFS and BFS
	URL : https://www.acmicpc.net/problem/1260

'''


n, m, v = map(int, input().split())			#n = 정점의 개수, m=간선의 개수, v =탐색 시작할 정점의 번호
matrix = [[0]*(n+1) for i in range(n+1)]
for i in range(m):        
  a, b = map(int, input().split())  #공백 기준 입력
  matrix[a][b]=matrix[b][a]=1       #양방향 간선, 이어지면 1로 바꿔
visit_list=[0]*(n+1)


def dfs(v):
  visit_list[v] = 1   #방문한 점 1로 표시
  print(v, end = ' ')
  for i in range(1, n+1):
    if(visit_list[i]==0 and matrix[v][i]==1): #아직 방문X & v와i가 연결O되었을때 순차적으로 dfs실행
      dfs(i)

def bfs(v):
  queue = [v] 		  #들려야 할 정점을 저장
  visit_list[v] = 0   #방문한 점 0으로 표시
  while queue:
    #print("before queue: ",queue)
    v = queue.pop(0)    #왼쪽부터 꺼낸다
    #print("afterPop queue :",queue)
    print(v, end =' ')
    for i in range(1, n+1):
      if(visit_list[i]==1 and matrix[v][i]==1): #아직 방문X & v와 i가 연결되어있을때 i를 큐에 추가한다. 
        queue.append(i)  #오른쪽으로 들어간다.
        visit_list[i]=0     #방문한 노드는 0으로 표시

dfs(v)
print()
bfs(v)



#.
#.
#.



'''
with 주석

#n = 정점의 개수, m=간선의 개수, v =탐색 시작할 정점의 번호
#matrix의 0행 0열은 생각 X

n, m, v = map(int, input().split())
matrix = [[0]*(n+1) for i in range(n+1)]
#for i in range(n+1):    #matrix 확인(0부터 n까지 반복)
#  print(matrix[i])
for i in range(m):        
  a, b = map(int, input().split())  #공백 기준 입력
  matrix[a][b]=matrix[b][a]=1       #양방향 간선, 이어지면 1로 바꿔
visit_list=[0]*(n+1)

#for i in range(n+1):    #matrix 확인(0부터 n까지 반복)
#  print(matrix[i])
#print("visit_list: ", visit_list)   #확인

def dfs(v):
  visit_list[v] = 1   #방문한 점 1로 표시
  #print('v:',v,"visit_list: ", visit_list)
  print(v, end = ' ') #방문한 점 출력
  for i in range(1, n+1):
    if(visit_list[i]==0 and matrix[v][i]==1): #아직 방문X & v와i가 연결O되었을때 순차적으로 dfs실행
      dfs(i)

def bfs(v):
  queue = [v] #들려야 할 정점을 저장, 여기서는 시작 정점v
  visit_list[v] = 0   #방문한 점 0으로 표시, dfs함수에서 모두 1이 default가 되었기 때문
  while queue:
    #print("before queue: ",queue)
    v = queue.pop(0)    #왼쪽부터 꺼낸다
    #print("afterPop queue :",queue)
    print(v, end =' ')
    for i in range(1, n+1):
      if(visit_list[i]==1 and matrix[v][i]==1): #아직 방문X & v와 i가 연결되어있을때 i를 큐에 추가한다. 
        queue.append(i)  #오른쪽으로 들어간다.
        visit_list[i]=0     #방문한 노드는 0으로 표시

dfs(v)
print()   #줄바꿈
bfs(v)


'''
