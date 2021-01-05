'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : ProgramersL1_체육복.py 
	URL : https://programmers.co.kr/learn/courses/30/lessons/42862
	
'''


def solution(n, lost, reserve):
    answer = 0
    # 학생배열을 n명만큼 0으로 선언
    student = []
    for i in range(n):
        student.append(0)
    # 도난당하면 -1, 여분 가지면 +1
    for i in lost:
        student[i-1] -= 1
    for i in reserve:
        student[i-1] += 1

    for i in range(0, len(student)):
        # 앞의 학생
        if student[i] == 1 and i -1 >= 0:
            if student[i-1] == -1:
                student[i-1] += 1
                student[i] -= 1
        # 뒤의 학생
        if student[i] == 1 and i + 1 < len(student):
            if student[i+1] == -1:
                student[i+1] += 1
                student[i] -= 1
    # -1(도난당하고 빌리지 못한)이 아닌 경우 세기
    for x in student:
        if x >= 0:
            answer += 1
    return answer


# s = solution(5, [2, 4], [1, 3, 5])
# print(s)