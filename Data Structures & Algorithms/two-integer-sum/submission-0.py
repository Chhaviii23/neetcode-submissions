class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        chhavi_map = {}
        for i in range(len(nums)):
            prev = nums[i]
            diff = target - prev
            if(target - nums[i]) in chhavi_map:
                return [chhavi_map[diff],i]
            
            chhavi_map[prev] = i

