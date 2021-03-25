'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : Baekjoon2217 rope
	URL : https://www.acmicpc.net/problem/2217
'''


n = int(input())
rope = []
for i in range(n):
    rope.append(int(input()))
rope.sort(reverse = True)
answer = 0

for i in range(n):
  answer = max(answer, rope[i] * (i + 1))

print(answer)