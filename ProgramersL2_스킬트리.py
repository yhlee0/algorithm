'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : ProgramersL2_스킬트리.py
	URL : https://programmers.co.kr/learn/courses/30/lessons/49993?language=python3
	
'''



def solution(skill, skill_trees):
    answer = 0
    arr = []
    
    for i in range(len(skill_trees)):
        exist = 0
        learn = 0
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in skill:
                exist += 1 # 스킬에 존재한다면 +1
                
            if skill_trees[i][j] == skill[learn]:
                learn += 1 # 배웠다는 의미 c->b->d로 이동
                if learn == len(skill): # 만약, 배운 것의 개수가 skill의 총 개수와 같다면 종료(모두 배운 것.)
                    break
                    
        if exist == learn: #순서가 다르면 불가능한 스킬트리이므로, 존재함과 순서가 같아야 답임
            answer += 1
    
    return answer