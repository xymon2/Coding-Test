#https://programmers.co.kr/learn/courses/30/lessons/43164#
#결국 못풀었다...
#재귀로 푸는 연습을 해보자
from collections import deque


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        def dfs(a):
            if not a in tdict:
                answer.append(a)
                return

            while tdict[a]:
                dfs(tdict[a].pop())

            answer.append(a)

        answer = []

        tdict = {}
        for item in tickets:
            if tdict.get(item[0]) == None:
                tdict[item[0]] = [item[1]]
            else:
                tdict[item[0]].append(item[1])
                tdict[item[0]].sort(reverse=True)

        dfs('JFK')

        return answer[::-1]
