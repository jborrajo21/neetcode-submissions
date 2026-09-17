class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = True
        i = len(digits) - 1
        while carry and i >=0:
            digits[i] = (digits[i] + 1) % 10
            carry = digits[i] == 0
            i -= 1
        
        if carry:
            digits[0] = 1
            digits.append(0)
        
        return digits

