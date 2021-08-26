#https://programmers.co.kr/learn/courses/30/lessons/43163
#찢었노.

from collections import deque

def comp(str1, str2):
    strl1 = list(str1)
    strl2 = list(str2)
    cnt = 0
    for i in range(len(strl1)):
        if strl1[i] != strl2[i]:
            cnt += 1

    if cnt == 1:
        return True
    else:
        return False


def solution(begin, target, words):
    if not target in words:
        return 0

    visited = []
    cnt = 0
    queue = deque([[begin, cnt]])

    while queue:
        n = queue.popleft()
        if not n[0] in visited:
            visited.append(n[0])
            for item in words:
                if comp(n[0], item) and not item in visited:
                    if item == target:
                        return n[1] + 1
                    # print(item,n[1]+1)
                    queue.append([item, n[1] + 1])
                    # print(visited)

    answer = 0
    return answer