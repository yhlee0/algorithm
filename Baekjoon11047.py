'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : Baekjoon 11047
	URL : https://www.acmicpc.net/problem/11047

'''


n, k = list(map(int, input().split()))
coins = []
count = 0

for i in range(n):
    c = int(input())
    coins.append(c)

coins.sort(reverse=True)

for i in coins:
    if i <= k:    #동전이 총액k보다 작거나 같을때
        count += (k // i)    #몫
        k %= i

print(count)
