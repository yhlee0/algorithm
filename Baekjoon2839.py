'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : Baekjoon 2839
	URL : https://www.acmicpc.net/problem/2839

'''


n = int(input())    # gram of suger
count = 0

while n >= 0:
    if n % 5 ==0:   #n이 5의 배수이면
        count += (n // 5)   #5로나눈 몫
        print(count)
        break
    n = n-3
    count += 1       #5의 배수가 될때까지 설탕무게-3, count +1
else:                
    print(-1)
