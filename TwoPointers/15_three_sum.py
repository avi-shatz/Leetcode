from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        triplets: List[List[int]] = []
        prev_start = None

        for s in range(n - 2):
            start = nums[s]
            if start == prev_start:
                continue
            prev_start = start

            target = start * -1
            l = s + 1
            r = n - 1
            prev_left, prev_right = None, None
            while l < r:
                left = nums[l]
                right = nums[r]
                if right > target - left or right == prev_right:
                    r -= 1
                elif right < target - left or left == prev_left:
                    l += 1
                else:
                    triplets.append([start, left, right])
                    prev_left, prev_right = left, right

        return triplets


class SlowForSomeReasonSolution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        num_to_index = {num: i for i, num in enumerate(nums)}
        triplets = set()
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                c = (nums[i] + nums[j]) * -1
                index = num_to_index.get(c)
                if index is not None and index != i and index != j:
                    triplets.add(tuple(sorted([nums[i], nums[j], c])))
        return [list(t) for t in triplets]


class NaiveSolution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        triplets = set()
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplets.add(
                            tuple(sorted([nums[i], nums[j], nums[k]])))
        return [list(t) for t in triplets]


nums = [-1, 0, 1, 2, -1, -4]
res = Solution().threeSum(nums)
print(res)

"""
15. 3Sum
Solved
Medium
Topics
Companies
Hint
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""
