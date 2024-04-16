from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums)
        prefix = 1
        suffix = 1

        for i, num in enumerate(nums):
            prefix = prefix * num
            products[i] = prefix
        print([i for i in range(len(nums) - 1, -1, -1)])
        for i in range(len(nums) - 1, -1, -1):
            prefix = products[i-1] if i > 0 else 1
            products[i] = prefix * suffix
            suffix *= nums[i]

        return products


nums = [1, 2, 3, 4]
# expected res: [24,12,8,6]
res = solution().productexceptself(nums)
print(res)

class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        1. create a prefix product which will calculate the product of all items before the given index
        2. create suffix pruduct array which will calculate the product of all items before the given index
        3. for each item in nums calculate the product of the index before in prefix and next index in suffix
        3.a. don't forget to deal with first/last item
        """
        prefix_arr = [1] * len(nums)
        suffix_arr = [1] * len(nums)
        results = []
        # 1
        prefix = 1
        for i, num in enumerate(nums):
            prefix = prefix * num
            prefix_arr[i] = prefix
        # 2
        suffix = 1
        for i, num in enumerate(reversed(nums)):
            suffix = suffix * num
            suffix_arr[len(nums) - i - 1] = suffix
        # 3
        for i, num in enumerate(nums):
            prefix = prefix_arr[i - 1] if i > 0 else 1
            suffix = suffix_arr[i + 1] if i + 1 < len(nums) else 1
            results.append(prefix * suffix)
        return results


"""
238. Product of Array Except Self
Medium
Topics
Companies
Hint
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

[1, 2, 3, 4]
[6, 3, 2, 6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""
