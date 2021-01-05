'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : ProgramersL1_모의고사.py 
	URL : https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3
	
'''


def solution(answers):
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    
    # s1, s2, s3의 정답 개수 세기
    count = [0, 0, 0]
    
    for i in range(len(answers)):
        if answers[i] == s1[i % 5]:
            count[0] += 1
        if answers[i] == s2[i % 8]:
            count[1] += 1
        if answers[i] == s3[i % 10]:
            count[2] += 1
    
    # 가장 점수를 많이 받은 사람            
    max_value = max(count[0], count[1], count[2])
    answer = []

    if max_value == count[0]:
        answer.append(1)
    if max_value == count[1]:
        answer.append(2)
    if max_value == count[2]:
        answer.append(3)       
    return answer