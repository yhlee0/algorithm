'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : sorting algorithm
    URL : https://blog.naver.com/fresh2816/222134393503
'''


n, k = map(int, input().split())

a = list(map(int, input().split()))     #list
b = list(map(int, input().split()))

a.sort() #오름차순 정렬
b.sort(reverse=True)  #내림차순 정렬

#첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k):
  if a[i]<b[i]:         #A의 원소 < B의 원소라면
    a[i], b[i] = b[i], a[i]
  else:                  #A의 원소 >= B의 원소라면
    break

print(sum(a))           #리스트 A의 모든 원소의 합 출력