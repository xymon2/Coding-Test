#https://programmers.co.kr/learn/courses/30/lessons/42883
#시간초과 2개통과못함
#로직은 맞는듯> 저기 pop부분만 어떻게 deque로 stack이나 그런걸로 하면 될듯.
#뒤 숫자보다 작으면 무조건 날리는 방식


# from collections import deque
def solution(number, k):
    nl = list(map(int, number))
    # nl = deque(nl)
    count = 0

    while count < k:
        for i in range(len(nl) - 1):
            if nl[i] < nl[i + 1]:
                # nl.remove(nl[i])
                nl.pop(i)
                count += 1
                break

    nnl = list(map(str, nl))

    return ''.join(nnl)