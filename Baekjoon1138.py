'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : Baekjoon1138.py
	URL : https://www.acmicpc.net/problem/1138
'''



n = int(input())
info = list(map(int, input().split()))
line = []

for i in range(len(info)-1, -1, -1):
  line.insert(info[i], i+1)

for i in line:
  print(i, end=' ')