'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : Minimum number of coins

'''


n = 1260
count =0

#Check the large units of coins in turn
listCoin = [500, 100, 50, 10]

for coin in listCoin:
    count += (n // coin)
    n %= coin  
print(count)