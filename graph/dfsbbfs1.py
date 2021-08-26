#https://programmers.co.kr/learn/courses/30/lessons/43165
#겨우풀었다 근데 dfs,bfs 쓴거같지는 않은데..
# from itertools import product
# def solution(numbers, target):
#     l = [(x, -x) for x in numbers]
#     s = list(map(sum, product(*l)))
#     return s.count(target)
# 위 코드를 풀어쓴 것....

def dfs(numbers):
    if len(numbers) == 1:
        return [[1], [-1]]

    else:
        numbers.pop()
        a_list = dfs(numbers)
        b_list = []
        for item in a_list:
            item2 = item[:]
            item2.append(-1)
            item.append(1)
            b_list.append(item2)

        a_list.extend(b_list)

    return a_list


def solution(numbers, target):
    o_list = []
    for i in range(len(numbers)):
        o_list.append(1)

    a = dfs(o_list)

    answer = 0

    for comb in a:
        num = 0

        for i in range(len(numbers)):
            num += numbers[i] * comb[i]

        if num == target:
            answer += 1

    return answer