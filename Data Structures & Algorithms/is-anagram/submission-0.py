class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_char = Counter(s)
        t_char = Counter(t)

        return s_char == t_char