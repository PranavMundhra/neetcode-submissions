class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paranthesis = {")" : "(", "]":"[", "}":"{"}

        for p in s:
            if p in paranthesis:
                if stack and stack[-1] == paranthesis[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
            
            print(stack)
        
        return not stack
            