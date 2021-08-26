#https://programmers.co.kr/learn/courses/30/lessons/43238
#이거 너무 어려운데..?
#언제써야할지 모르겠다.

def solution(n, times):
    answer = 0

    alist = []
    left = 1
    right = max(times) * n

    while right >= left:

        mid = (left + right) // 2
        sum = 0
        for time in times:
            sum += mid // time

        if sum >= n:
            right = mid - 1
            alist.append(mid)
        else:
            left = mid + 1

    return min(alist)