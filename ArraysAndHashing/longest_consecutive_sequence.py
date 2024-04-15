from typing import List, Set


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        while len(nums_set) > longest:
            num = nums_set.pop()
            forward_count = self.countConsecutiveItems(nums_set, num)
            backwards_count = self.countConsecutiveItems(nums_set, num, True)
            length = forward_count + backwards_count + 1
            if length > longest:
                longest = length
        return longest

    def countConsecutiveItems(self, nums_set: Set[int], num: int, count_backwards=False) -> int:
        length = 0
        while True:
            num = num - 1 if count_backwards else num + 1
            if num in nums_set:
                length += 1
                nums_set.remove(num)
            else: 
                return length

nums = [100,4,200,1,3,2]
res = Solution().longestConsecutive(nums)
print(res)
# 128. Longest Consecutive Sequence
# Medium
# Topics
# Companies
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.


# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
