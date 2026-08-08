class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for ch in t:
            need[ch] = need.get(ch,0)+1
        window={}
        left=0
        count=0
        start=0
        min_len=float("inf")

        for right in range(len(s)):
            ch=s[right]
            window[ch] = window.get(ch,0)+1
            if ch in need and window[ch]<= need[ch]:
                count += 1
            while count==len(t):
                if right-left+1 < min_len:
                    min_len = right-left+1
                    start=left

                ch =s[left]
                window[ch] -= 1
                if ch in need and window[ch]<need[ch]:
                    count -= 1
                left+=1

        if min_len == float("inf"):
            return ""
        return s[start:start + min_len]