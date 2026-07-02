class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 1
        k = 1

        while(right<len(nums)):
            if(nums[right] == nums[left]):
                right += 1
                continue
            else:
                nums[left+1] = nums [right]
                left += 1
                k += 1
                right += 1

        return k