class Solution:
    def isValid(self, s: str) -> bool:
        list=[]

        for ch in s:
            if ch== '(':
                list.append(')')
            elif ch== '[':
                list.append(']')
            elif ch== '{':
                list.append('}')
            else:
                if not list or list.pop() !=ch:
                    return False
        return not list