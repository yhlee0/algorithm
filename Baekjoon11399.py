'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : Baekjoon 11399
	URL : https://www.acmicpc.net/problem/11399

'''


#answer1
n = int(input())    #number of people
time = map(int, input().split())
total = 0
timePerson = 0

time = list(time)
time.sort()

for i in time:
    timePerson += i
    total += timePerson

print(total)

#.
#.
#.

#answer2
'''
n = int(input())    #number of people
time = map(int, input().split())
total = 0
timePerson = 0

time = list(time)
time.sort()

for i in time:
    total += (i * n)
    n -= 1

print(total)
'''