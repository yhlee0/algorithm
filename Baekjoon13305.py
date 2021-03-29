'''
**Info**
	GitHub name : yhlee0(https://blog.naver.com/fresh2816/222291282821)
	Subject : Baekjoon 13305 주유소
	URL : https://www.acmicpc.net/problem/13305
'''


n = int(input())
d = list(map(int, input().split()))
p = list(map(int, input().split()))

minP = p[0]
total = 0

for i in range(n-1):
  if p[i] < minP:
    minP = p[i]
  total += minP * d[i]
print(total)