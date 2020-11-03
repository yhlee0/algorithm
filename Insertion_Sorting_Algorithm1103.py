'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : Insertion sorting algorithm
	
	
'''


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):        #두번째 데이터부터 시작
  for j in range(i, 0, -1):     	  #인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
    if array[j]<array[j-1]:   		  #자신과 자산의 왼쪽의 값과 비교
      array[j], array[j-1]=array[j-1], array[j]   #한칸씩 왼쪽으로 이동
    else:     #자기보다 작은 데이터를 만나면 그 위치에서 멈춤
      break

print(array)