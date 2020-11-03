'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : baekjoon_1026
    URL : https://www.acmicpc.net/problem/1026
'''


n = int(input())    #length
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s=0       #answer

a.sort()
b.sort(reverse=True)


for i in range(n):
  s+=a[i]*b[i]
print(s)



''' v2
while a:
  s += (a.pop(a.index(min(a)))*b.pop(b.index(max(b))))
print(s)
'''