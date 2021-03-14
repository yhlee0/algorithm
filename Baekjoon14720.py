'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : Baekjoon14720.py
	URL : https://www.acmicpc.net/problem/14720
'''



n = int(input())
store = list(map(int, input().split()))
count = 0

for i in range(n):
    if(store[i] == count % 3):
        count+=1

print(count)