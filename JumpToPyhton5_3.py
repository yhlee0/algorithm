'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : JumpToPyhton5_3.py : class
	URL : https://blog.naver.com/fresh2816/222193132690
	
'''


class FourCal:
  def setdata(self, first, second):
    self.first = first
    self.second = second
  def sum(self):
    result = self.first + self.second
    return result
  def mul(self):
    result = self.first * self.second
    return result
  def sub(self):
    result = self.first - self.second
    return result
  def div(self):
    result = self.first / self.second
    return result

a = FourCal() #객체생성
b = FourCal()
a.setdata(4, 2) 
b.setdata(3, 7)

print(a.sum())
print(a.mul())
print(b.div())