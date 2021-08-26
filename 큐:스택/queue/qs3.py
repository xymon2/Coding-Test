#https://programmers.co.kr/learn/courses/30/lessons/42583
#무난했음 근데 이번에도 에러가 없었으면 edge 케이스 못찾았을 것.

from collections import deque

def solution(bridge_length, weight, truck_weights):
    crossing = deque()
    arrived = deque()
    count = deque()
    answer = 0

    while len(truck_weights) != 0 or len(crossing) > 0:

        c_len = len(count)

        if c_len != 0:
            for i in range(c_len):
                count[i] -= 1

            if count[0] == 0:
                count.popleft()
                arrived.append(crossing.popleft())

        if len(truck_weights) != 0 and not sum(crossing) + truck_weights[0] > weight:
            t = truck_weights.pop(0)
            crossing.append(t)
            count.append(bridge_length)

        answer += 1

    return answer