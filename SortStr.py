'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : SortStr
	
'''


a = input()
result = []
sum = 0
#문자를 하나씩 확인하며
for i in a:
    #알파벳인 경우 결과 리스트에 삽입
    if i.isalpha():
        result.append(i)
    #숫자는 따로 더하기
    else:
        sum += int(i)

#알파벳을 오름차순으로 정렬
result.sort()

#숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if sum != 0:
    result.append(str(sum))

#최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))