class Solution:
    def isValid(self, s: str) -> bool:
        mapping={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stack=[]
        for c in s:
            if c in mapping:
                if not stack or stack[-1]!=mapping[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return len(stack)==0 
        