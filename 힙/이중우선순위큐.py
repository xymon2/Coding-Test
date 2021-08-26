#https://programmers.co.kr/learn/courses/30/lessons/42628
#easy

import heapq as hq

def solution(operations):
    answer = []
    heap = []

    for op in operations:
        opl = op.split()

        if opl[0] == 'I':
            num = int(opl[1])
            hq.heappush(heap, num)

        else:
            if len(heap) == 0:
                continue

            if opl[1] == '1':
                heap.sort()
                a = heap.pop()
            else:
                a = hq.heappop(heap)

    if len(heap) == 0:
        answer = [0, 0]
    elif len(heap) == 1:
        answer = [0, 0]
    else:
        min = hq.heappop(heap)
        heap.sort()
        max = heap.pop()
        answer = [max, min]

    return answer