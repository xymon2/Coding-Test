#https://programmers.co.kr/learn/courses/30/lessons/42840#
#완전탐색
# 더 간단하게 만들 수 있었을 텐데..

def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    thr = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0, 0, 0]

    while len(answers) > len(one):
        one.extend(one)

    while len(answers) > len(two):
        two.extend(two)

    while len(answers) > len(thr):
        thr.extend(thr)

    for i in range(len(answers)):

        if answers[i] == one[i]:
            score[0] += 1
        if answers[i] == two[i]:
            score[1] += 1
        if answers[i] == thr[i]:
            score[2] += 1

    mx = max(score)

    for idx, num in enumerate(score):
        if num == mx:
            answer.append(idx + 1)

    return answer