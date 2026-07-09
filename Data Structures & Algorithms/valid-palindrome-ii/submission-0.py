class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                i = left+1
                j = right
                while i < j and s[i] == s[j]:
                    i += 1
                    j -= 1
                if i >= j:
                    return True

                i = left
                j = right - 1
                while i < j and s[i] == s[j]:
                    i += 1
                    j -= 1
                return i >= j

            left += 1
            right -= 1

        return True