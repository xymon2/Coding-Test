
#https://leetcode.com/problems/combination-sum/
# 나가는 조건을 다르게 하기만해도 시간복잡도가 많이줄어든다
#나가는 조건을 잘 생각해보자

from collections import deque


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        answer = []

        candidate = deque([])

        for item in candidates:
            candidate.append([[item], target - item])

        candict = {}

        while candidates:
            a = candidates[0]
            candict[a] = candidates[:]
            candidates.pop(0)

        while candidate:
            a = candidate.popleft()

            if a[1] == 0:
                a[0].sort()
                if not a[0] in answer:
                    answer.append(a[0])
                continue

            elif a[1] < 0:
                continue

            b = candict[a[0][0]]
            for item in b:
                a2 = a[0][:]
                a2.append(item)
                candidate.append([a2, a[1] - item])

        return answer





