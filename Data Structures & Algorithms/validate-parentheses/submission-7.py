class Solution:
    def isValid(self, s: str) -> bool:
        mapping={
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack=[]
        for c in s:
            if c in mapping:
                if not stack or mapping[c]!=stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        return len(stack)==0
        