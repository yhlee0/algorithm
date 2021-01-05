'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : ProgramersL1_자연수_뒤집어_배열로_만들기.py 
	URL :  https://programmers.co.kr/learn/courses/30/lessons/12932?language=python3
	
'''


def solution(n):
    nList = list(str(n))
    nList = list(map(int, nList))
    nList.reverse()
    return nList