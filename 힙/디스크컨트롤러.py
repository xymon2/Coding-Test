#https://programmers.co.kr/learn/courses/30/lessons/42627
#에지케이스는 찾았는데 고치느라 고생했다
#최솟값, 최댓값뽑고 추기하고 정렬하 반복되면 heap을쓰는게 맞는 것 같다.

import heapq as hq
from collections import deque

def solution(jobs):
    answer = 0
    sptime = []
    heap = []
    jobs.sort()
    jobs = deque(jobs)
    time = jobs[0][0]

    #여기서도 edge케이스 발생했었지.
    while jobs and jobs[0][0] <= time:
        item = jobs.popleft()
        hq.heappush(heap, (item[1], item))

    while heap:
        cur = hq.heappop(heap)
        spt = time - cur[1][0] + cur[1][1]
        time += cur[1][1]
        sptime.append(spt)

        while jobs and jobs[0][0] <= time:
            item = jobs.popleft()
            hq.heappush(heap, (item[1], item))

        #에지케이스 고치기 순서만 바꿨는데 되네..? 왠지는 잘 모르겠
        if jobs and not heap:
            time = jobs[0][0]
            item = jobs.popleft()
            hq.heappush(heap, (item[1], item))

    # print(sptime)
    answer = int(sum(sptime) / len(sptime))

    return answer