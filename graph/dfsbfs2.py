
#https://programmers.co.kr/learn/courses/30/lessons/43162
#지 렸 다

from collections import deque


def solution(n, computers):
    a = deque()
    for idx, net in enumerate(computers):
        a.append([net, idx])

    vv = []

    for item in a:
        visited = []
        queue = deque([item])

        while queue:
            n = queue.popleft()
            if not n in visited:
                visited.append(n)
                for idx, num in enumerate(n[0]):
                    if num == 1:
                        queue.append(a[idx])
        visited.sort()
        if visited in vv:
            continue
        else:
            vv.append(visited)

    answer = len(vv)
    return answer