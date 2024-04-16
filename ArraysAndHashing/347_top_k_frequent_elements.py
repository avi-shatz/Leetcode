from collections import defaultdict
from typing import Dict, List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the frequecy into a hasmap - o(n) where n=len(nums)
        num_to_frequency = {}
        for num in nums:
            num_to_frequency[num] = num_to_frequency.get(num, 0) + 1

        # store each number in a new array where the index is the frequency - o(n)
        freqencies_index_based: List[List[int]] = [[]
                                                   for i in range(len(nums) + 1)]
        for num, frequency in num_to_frequency.items():
            f = freqencies_index_based[frequency]
            f.append(num)
        # iterate threw the previous array in a descending order and return the first k elements - o(k)
        c = 0
        top_k_frequent = []
        for arr in reversed(freqencies_index_based):
            for num in arr:
                top_k_frequent.append(num)
                c += 1
                if c == k:
                    return top_k_frequent
        return top_k_frequent


class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_frequency: Dict[int, int] = defaultdict(int)
        for num in nums:
            num_to_frequency[num] += 1
        frequencies = list(num_to_frequency.items())
        frequencies.sort(key=lambda item: item[1], reverse=True)
        return [lst[0] for lst in frequencies][:k]


res = Solution().topKFrequent([3, 0, 1, 0], 1)
print(res)


# 347. Top K Frequent Elements
# Medium
# Topics
# Companies
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
