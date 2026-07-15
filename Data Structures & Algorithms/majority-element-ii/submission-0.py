class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1 = None
        c2 = None
        n1=0
        n2=0

        for x in nums:
            if x == c1:
                n1 += 1
            elif x == c2:
                n2 += 1
            elif n1 == 0:
                c1 = x
                n1 = 1
            elif n2 == 0:
                c2 = x
                n2 = 1
            else:
                n1 -= 1
                n2 -= 1

        ans = []
        if nums.count(c1) > len(nums)//3:
            ans.append(c1)
        if c2 != c1 and nums.count(c2) > len(nums)//3:
            ans.append(c2)

        return ans