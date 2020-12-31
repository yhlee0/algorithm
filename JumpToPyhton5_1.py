'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : JumpToPyhton5_1.py : Calculation
	URL : https://blog.naver.com/fresh2816/222192247769
	
'''


#answer1(using class)
class Calculator:
  def __init__(self):
    self.result=0

  def adder(self, num):
    self.result += num
    return self.result

cal1=Calculator()
cal2=Calculator()

print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(3))
print(cal2.adder(7))

#.
#.
#.

#answer2(not using class, not recommend)
'''
result1=0
result2=0

def adder1(num):
  global result1
  result1 += num
  return result1

def adder2(num):
  global result2
  result2 += num
  return result2


print(adder1(3))
print(adder1(4))
print(adder2(3))
print(adder2(7))
'''