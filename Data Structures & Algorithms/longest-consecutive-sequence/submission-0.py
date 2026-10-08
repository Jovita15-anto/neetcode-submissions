class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        longest = 0

        for num in num_set:

            # Check if this number is the beginning
            # of a consecutive sequence
            if num - 1 not in num_set:

                length = 1

                # Count the consecutive numbers
                while num + length in num_set:
                    length += 1

                longest = max(longest, length)

        return longest