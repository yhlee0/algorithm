'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : JumpToPyhton5_5.py : class
	URL : https://blog.naver.com/fresh2816/222194046563
	
'''


class HousePark():
  lastname = "박"     # 클래스변수
  def __init__(self, name):
    self.fullname = self.lastname + name
  def travel(self, where):
    print("%s, %s여행을 가다." % (self.fullname, where))
  def love(self, other):
    print("%s, %s 사랑에 빠졌네" % (self.fullname, other.fullname))
  def fight(self, other):
    print("%s, %s 싸우네" % (self.fullname, other.fullname))
  def __add__(self, other):
    print("%s, %s 결혼했네" % (self.fullname, other.fullname))
  def __sub__(self, other):
    print("%s, %s 이혼했네" % (self.fullname, other.fullname))


class HouseKim(HousePark):
  lastname = "김"
  def travel(self, where, day):
    print("%s, %s여행 %d일 가네" % (self.fullname, where, day))


pey = HousePark("응용")  # Create instance, pey
juliet = HouseKim("줄리엣")
pey.travel("부산")
# print(pey.fullname)
juliet.travel("부산", 3)
pey.love(juliet)
pey + juliet
pey.fight(juliet)
pey - juliet