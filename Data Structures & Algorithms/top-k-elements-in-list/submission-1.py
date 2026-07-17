class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = Counter(nums)
        res = []

        for num,val in nums.items():
            res.append((val,num))
        res.sort()
        buk = []
        for i in range(len(res)-1, (len(res)-1)-k, -1):
            buk.append(res[i][1])
        return buk