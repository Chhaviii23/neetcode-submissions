class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        result = ""
        first = strs[0]

        for i in range(len(first)):
            for word in strs[1:]:
                if i == len(word) or word[i] != first[i]:
                    return result
            result += first[i]
            
        return result