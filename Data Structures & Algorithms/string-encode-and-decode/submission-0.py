class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for word in strs:
            encoded += str(len(word)) +"#"+ word
        return encoded

    def decode(self, s: str) -> List[str]:
        res=[]
        idx=0

        while idx<len(s):
            sep=idx
            while s[sep]!= "#":
                sep += 1
            length=int(s[idx:sep])

            start=sep + 1
            end = start + length
            res.append(s[start:end])
            idx=end
        return res
