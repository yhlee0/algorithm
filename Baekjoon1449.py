'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : baekjoon_1449
    URL : https://www.acmicpc.net/problem/1449
'''


N, L = map(int, input().split())
tofix = list(map(int, input().split()))
tofix.sort()

start = 0
count = 0
for i in tofix:
  # start + L - 1은 같이 수리되므로 무시
  if start < i:
    start = i + L - 1
    count += 1

print(count)