class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def bt(op, cl):
            if op == cl == n:
                res.append("".join(stack))
                return
            
            if op < n:
                stack.append("(")
                bt(op + 1, cl)
                stack.pop()
            if cl < op:
                stack.append(")")
                bt(op, cl + 1)
                stack.pop()
            return
        bt(0,0)
        return res