'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : * or +
			  
'''



#answer1

a = input()
sum = 0
for temp in a:
    temp = int(temp)
    if temp<=1 or sum<=1:
        sum += temp
    else :
        sum *= temp

print(sum)


#.
#.
#.


#answer2

data = input()
result = int(data[0])
for i in range(1, len(data)):
    num = int(data[i])
    if num <=1 or result <= 1:
        result += num
    else:
        result *= num

print(result)