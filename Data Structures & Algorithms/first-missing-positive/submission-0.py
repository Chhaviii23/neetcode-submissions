class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numbers=set(nums)
        not_present= 1

        while not_present in numbers:
            not_present += 1
        return not_present