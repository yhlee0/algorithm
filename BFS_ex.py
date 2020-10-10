'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : BFS_ex
	
'''


from collections import deque

#BFS 메서드 정의
def bfs(graph, start, visited):
  
  queue = deque([start])	#Queue 구현을 위해 deque라이브러리 사용
  visited[start] = True		#현재 노드 방문 처리
  
  while queue:				#큐가 빌 때까지 반복
    v = queue.popleft()		#큐에서 하나의 원소를 뽑아 출력하기
    print(v, end=' ')
  
    #아직 방문하지 않은 인접한 원소들을 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

#각 노드가 연결된 정보를 표현(2차원리스트)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

#각 노드가 방문된 정보를 표현(1차원리스트)
visited = [False]*9

#정의된 BFS함수 호출
bfs(graph, 1, visited)