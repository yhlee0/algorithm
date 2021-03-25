'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : Baekjoon11721 열 개씩 끊어 출력하기
	URL : https://www.acmicpc.net/problem/11721
'''


s = input()
for i in range(0, len(s), 10):
  print(s[i:i+10])