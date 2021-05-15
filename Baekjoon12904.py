'''
**Info**
	GitHub name : yhlee0
	Subject : baekjoon_12904
    URL : https://www.acmicpc.net/problem/12904
'''


S = str(input())
T = list(map(str, input()))

while len(S) != len(T):
  if T[-1] == 'A':
      T.pop()
  elif T[-1] == 'B':
      T.pop()
      T = T[::-1]

S = list(S) # S와 T의 비교를 위함
if S == T:
  print(1)
else:
  print(0)