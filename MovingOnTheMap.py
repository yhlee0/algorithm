'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : Moving on the map
	
'''

n = int(input())         #공간의 크기
x, y = 1, 1              #시작좌표
plans = input().split()  #이동경로

#L, R, U ,D에 따른 이동방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0 ,0]
move_types = ['L', 'R', 'U', 'D']

#이동 계획을 하나씩 확인하기
for p in plans:
    #이동 후 좌표구하기
    for i in range(len(move_types)):
        if p == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    #공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx>n or ny>n:
        continue
    #이동수행
    x, y = nx, ny

print(x, y)