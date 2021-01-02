'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : JumpToPyhton5_4.py : class
	URL : https://blog.naver.com/fresh2816/222194014922
	
'''


class HousePark():
  lastname = "박"     # 클래스변수
  def __init__(self, name):
    self.fullname = self.lastname + name
  def travel(self, where):
    print("%s, %s여행을 가다." % (self.fullname, where))

pey = HousePark("응용")  # Create instance, pey
pey.travel("부산")
print(pey.fullname)

pes = HousePark("도민")
pes.travel("통영")
