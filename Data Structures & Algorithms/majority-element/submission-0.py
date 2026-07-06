class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        new_nums = None

        for num in nums:
            if cnt == 0:
                new_nums = num
            if num == new_nums:
                cnt += 1
            else:
                cnt -= 1

        return new_nums