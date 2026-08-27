class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        fdr=path.split("/")

        for fdr in fdr:
            if fdr == "" or fdr == ".":
                continue
            elif fdr == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(fdr)
        return "/" + "/".join(stack)