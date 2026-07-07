class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        i = 0
        j = 0
        k = 0
        ans = [0] * len(nums)

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                ans[k] = left[i]
                i += 1
            else:
                ans[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            ans[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            ans[k] = right[j]
            j += 1
            k += 1

        return ans