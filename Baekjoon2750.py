'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : baekjoon_2750
    URL : https://www.acmicpc.net/problem/2750
'''


n = int(input())
a = []     
for i in range(n):
  a.append(int(input()))

a.sort()
for i in a:
  print(i)
