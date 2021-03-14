'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : Baekjoon1541.py
	URL : https://www.acmicpc.net/problem/1541
'''



# import sys
s = input().split('-')
n = []
for i in s:
    sum = 0
    b = i.split('+')
    for i in b:
        sum += int(i)
    n.append(sum)
answer = n[0]
for j in range(1,len(n)):
    answer -= n[j]
print(answer)