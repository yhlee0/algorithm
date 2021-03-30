'''
**Info**
	GitHub name : yhlee0 (fresh2816@naver.com)
	Subject : Baekjoon 4949 균형잡힌 세상
	URL : https://www.acmicpc.net/problem/4949
'''


while True:
    stack = []
    sentence = input()
    if sentence == ".":
        break
    for word in sentence:
        if word in "[(":
            stack.append(word)
        elif word in "])":
            if len(stack) > 0 and stack[-1] == "(" and word == ")":
                stack.pop()
            elif len(stack) > 0 and stack[-1] == "[" and word == "]":
                stack.pop()
            else:
                stack = [None]
                break
    if len(stack) > 0:
        print("no")
    else:
        print("yes")
