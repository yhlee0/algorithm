'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : Count of the time including '3'
	
'''


h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            #매 시각안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i)+str(j)+str(k):
                count += 1

print(count)
