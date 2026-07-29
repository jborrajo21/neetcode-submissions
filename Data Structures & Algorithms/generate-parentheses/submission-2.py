class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        valid = []
        opens = closes = 0
        def bt(state):
            nonlocal opens, closes
            if opens == closes and opens + closes == 2 * n:
                valid.append(str(state))
                return
            if closes > opens:
                return
            if opens < n:
                state = "".join([state, "("])
                opens += 1
                bt(state)
                opens -= 1
                state = state[:-1]

            state = "".join([state, ")"])
            closes += 1
            bt(state)
            closes -= 1
            state = state[:-1]

            return
            
        
        bt("")
        return valid