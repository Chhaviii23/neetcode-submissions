class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        
        while low<high:
            cap = (low+high)//2
            curr_weight=0
            req_days = 1
            
            for weight in weights:
                if curr_weight+weight > cap:
                    req_days += 1
                    curr_weight = 0
                curr_weight += weight
            if req_days <= days:
                high=cap
            else:
                low=cap+1
        return low