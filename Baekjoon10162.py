'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : Baekjoon 10162 전자레인지
	URL : https://www.acmicpc.net/problem/10162
'''


# anwer1
time = int(input())
A = B = C = n =0

A = time // 300 
n = time % 300 

B = n // 60 
n = n % 60 

C = n // 10 
n = n % 10 

if (n != 0):
  print(-1) 
else: 
  print(A, B, C)
  
  
# .
# .
# .


# answer2  
time = int(input())

if time % 10 != 0:
    print(-1)
else:
    A = B = C = 0
    A = time // 300
    B = (time % 300) // 60
    C = (time % 300) % 60 // 10
    print(A, B, C)