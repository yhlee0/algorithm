'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : Baekjoon5585 exchange change
	URL : https://www.acmicpc.net/problem/5585
'''


pay = int(input())
change = 1000 - pay
count = 0
for x in [500, 100, 50, 10, 5, 1]:
    count += change // x
    change %= x
print(count)