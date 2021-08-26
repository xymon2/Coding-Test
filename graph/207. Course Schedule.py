#https://leetcode.com/problems/course-schedule/

from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        def dfs(a):
            if a in visited:
                return False

            elif a in rvisited:
                return True

            visited.add(a)

            for item in graph[a]:
                if not dfs(item):
                    return False

            visited.remove(a)
            rvisited.add(a)
            return True


        visited = set()
        rvisited = set()
        graph = defaultdict(list)

        for x ,y in prerequisites:
            graph[x].append(y)


        for route in list(graph):
            if not dfs(route):
                return False

        return True




