'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : baekjoon_2751
    URL : https://www.acmicpc.net/problem/2751
'''


import sys
n = int(sys.stdin.readline())
a = []      #a=list()
for i in range(n):
  a.append(int(sys.stdin.readline()))
a.sort()

for i in a:
  print(i)