class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        stars = []
        for i,c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == '*':
                stars.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
        
        for _ in range(len(stack)):
            if not stars or stack.pop() > stars.pop():
                return False
        
        return True
                
        