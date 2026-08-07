class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                if not stack: return False
                opening = stack.pop()
                if (c == ')' and opening != '(' 
                or c == ']' and opening != '[' 
                or c == '}' and opening != '{'):
                    return False

        return len(stack) == 0 
