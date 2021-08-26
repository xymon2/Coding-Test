#https://programmers.co.kr/learn/courses/30/lessons/42578
#답먼저보지 말것.
#순열조합 잘 생각할 것.


def solution(clothes):
    answer = 1
    clt = {}

    for item in clothes:
        if item[1] in clt.keys():
            clt[item[1]] += 1
        else:
            clt[item[1]] = 1

    for key in clt:
        answer *= (clt[key] + 1)

    return answer - 1