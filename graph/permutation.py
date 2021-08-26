#https://leetcode.com/problems/permutations/submissions/
# "끝"

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        answer = []

        if len(nums) == 1:
            answer.append([nums[0]])
            return answer

        num2 = nums[:]

        for i in range(len(nums)):
            nums[i] = [nums[i]]

        while nums:
            a = nums.pop()
            for item in num2:
                b = a[:]
                if not item in b:
                    b.append(item)
                else:
                    continue
                if len(b) == len(num2):
                    answer.append(b)
                else:
                    nums.append(b)

        answer.sort()
        return answer

