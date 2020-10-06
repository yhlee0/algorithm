'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : Find the minimum number of repetitions.
			  Repeat '1 minus' or 'N divided by K'
			  , until any number N becomes 1.
			  
'''



#answer1

n, k = map(float, input().split())
count = 0

while(n>1):
    count += 1
    if n%k==0:
        n /= k
    else:
        n -= 1
print("count: ", count)




#answer2

n, k = map(int, input().split())
count =0

while True:
    #N이 K로 나누어떨어지는 수가 될때까지만 1씩빼기
    target = (n//k) *k         #target은 k의 배수가 됨
    count += (n - target)
    n = target

    #n이 k보다 작을 때 (=더이상 나눌수없을때) 반복문 탈출
    if n<k:
        break

    #k로 나누기
    count += 1
    n//=k

#마지막으로 남은 수에 대하여 1씩뺴기
count += (n-1)
print(count)