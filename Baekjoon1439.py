'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : Baekjoon1439.py 뒤집기
	URL : https://www.acmicpc.net/problem/1439
'''



s = input()
count = 0
for i in range(1, len(s)):
    if s[i] != s[i-1]:
        count += 1
print((count+1) // 2)