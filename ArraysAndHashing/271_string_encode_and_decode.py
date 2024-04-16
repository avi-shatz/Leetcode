from typing import List

class Solution:
    NUMBER_SEPERATOR = "_"
    NUMBER_TO_STRS_SEPERATOR = "#"

    def encode(self, strs: List[str]) -> str:
        """
        Using 2 arrays one to concatenate the strings with no delimeters and one to count each string length.
        Will return both strings concatenated. To enable decoding we will have to add a delimeter between each number 
        and between end of numbers and start of strings.
        """
        encoded_prefix = [str(len(s)) for s in strs]
        encoded_prefix_str = self.NUMBER_SEPERATOR.join(encoded_prefix)
        joined_strs = "".join(strs)
        return encoded_prefix_str + self.NUMBER_TO_STRS_SEPERATOR + joined_strs

    def decode(self, s: str) -> List[str]:
        strs = []
        encoded_prefix, encoded_strs = s.split(
            self.NUMBER_TO_STRS_SEPERATOR, 1)
        if encoded_prefix == "":
            return []
        strs_len = [int(num_str)
                    for num_str in encoded_prefix.split(self.NUMBER_SEPERATOR)]
        i = 0
        for num in strs_len:
            strs.append(encoded_strs[i: i+num])
            i += num
        return strs

# s = "abcde"
# print (s[0:2])
strs = ["neet", "code", "love", "you"]
encoded_str = Solution().encode(strs)
print(f"encoded_str: {encoded_str}")
decoded_strs = Solution().decode(encoded_str)
print(f"decoded_str: {decoded_strs}")


# String Encode and Decode
# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

# Example 1:

# Input: ["neet","code","love","you"]

# Output:["neet","code","love","you"]
# Example 2:

# Input: ["we","say",":","yes"]

# Output: ["we","say",":","yes"]
# Constraints:

# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains only UTF-8 characters.
