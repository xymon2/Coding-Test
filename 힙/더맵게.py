# https://programmers.co.kr/learn/courses/30/lessons/42626
# heap 으로 바꿨을 뿐인데...다 통과했네.
# queue,stack 과 heap의 차이? 자동 정렬이 필요할때인가.
#pop,append sort 보다 heap쓰는게 빠르다
# sort가 여러번 들어가면 heap을 써보자.


import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for item in scoville:
        heapq.heappush(heap, item)

    # heapq.heapify(scoville)
    # 하면 더 편함

    while heap[0] < K:
        if len(heap) == 1:
            return -1
        one = heapq.heappop(heap)
        two = heapq.heappop(heap)
        mixed = one + 2 * two
        heapq.heappush(heap, mixed)
        answer += 1

    return answer