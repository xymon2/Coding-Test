#https://leetcode.com/problems/network-delay-time/

from collections import defaultdict
import heapq as hq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append([v, w])

        Q = [[0, k]]

        dist = defaultdict(int)

        while Q:
            time, node = hq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    hq.heappush(Q, [alt, v])

        if len(dist) == n:
            return max(dist.values())
        else:
            return -1

