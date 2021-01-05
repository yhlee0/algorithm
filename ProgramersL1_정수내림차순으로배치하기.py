'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : ProgramersL1_정수 내림차순으로 배치하기.py 
	URL :  https://programmers.co.kr/learn/courses/30/lessons/12933?language=python3
	
'''


def solution(n):
  nList = list(str(n))
  nList.sort(reverse = True)
  answer = int("".join(nList))
  return answer

# s = solution(118372)
# print(s)