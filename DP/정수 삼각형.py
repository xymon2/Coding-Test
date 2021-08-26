#https://programmers.co.kr/learn/courses/30/lessons/43105
#다시풀어보자 어케생각했지?

def solution(triangle):
    answer = 0

    for idx, item in enumerate(triangle):
        if len(item) == 1:
            continue

        for idx2, num in enumerate(item):
            pr_list = triangle[idx - 1]
            if idx2 == 0:
                item[idx2] += pr_list[0]
            elif idx2 == len(item) - 1:
                item[idx2] += pr_list[-1]
            else:
                value = max(pr_list[idx2 - 1], pr_list[idx2])
                item[idx2] += value

    answer = max(triangle[-1])
    return answer