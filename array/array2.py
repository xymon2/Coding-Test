#https://leetcode.com/problems/3sum/
#two pointer도 어렵다...

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []

        nums.sort()

        for idx, num in enumerate(nums):
            left = idx + 1
            right = len(nums) - 1

            while left < right:

                if (0 - num) > nums[left] + nums[right]:
                    left += 1
                elif (0 - num) < nums[left] + nums[right]:
                    right -= 1
                else:
                    if not [num, nums[left], nums[right]] in answer:
                        answer.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1

        return answer