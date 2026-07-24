class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d ={0:1}
        s=0
        ans=0

        for x in nums:
            s += x
            ans += d.get(s-k, 0)
            d[s] = d.get(s,0)+1
        return ans