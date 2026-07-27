class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = "+-*/"
        stack = []
        ans = 0
        for i in tokens:
            if i in ops:
                t1 = int(stack.pop())
                t2 = int(stack.pop())
                if i == '-':
                    ans = t2-t1
                if i == '+':
                    ans = t2+t1
                if i == '*':
                    ans = t2*t1
                if i == '/':
                    ans = int(t2/t1)
                stack.append(str(ans))
            else:
                stack.append(i)
                print(stack)
        
        return int(stack[-1])
            