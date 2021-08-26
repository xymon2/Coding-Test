from collections import deque


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # temperatures = deque(temperatures)
        stack = []
        answer = [0 for i in range(len(temperatures))]
        for i, tmp in enumerate(temperatures):

            while stack and temperatures[stack[-1]] < tmp:
                l = stack.pop()
                answer[l] = i - l
            stack.append(i)

        return answer