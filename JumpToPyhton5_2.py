'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : JumpToPyhton5_2.py : what is init?
	URL : https://blog.naver.com/fresh2816/222192442180
	
'''


#answer1(with __init__)
class Service:
  secret= "비밀은 네모상자안에 있다."
  def __init__(self, name):        
    self.name = name
  def sum(self, a, b):
    result = a+b
    print("%s님 %s + %s = %s입니다." % (self.name, a,b,result))

pey=Service("kim")
pey.sum(1, 1)

#.
#.
#.

#answer2(without __init__)
'''
class Service:
  secret= "비밀은 네모상자안에 있다."
  def setname(self, name):        
    self.name = name
  def sum(self, a, b):
    result = a+b
    print("%s님 %s + %s = %s입니다." % (self.name, a,b,result))

pey=Service()
pey.setname("kim")
pey.sum(1, 1)

'''