'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : ProgramersL1_체육복_v2.py 
	URL : https://programmers.co.kr/learn/courses/30/lessons/42862
	
'''


def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)