class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        l = 0
        r = 0

        while r < len(triplets):
            while r < len(triplets) and (triplets[r][0] > target[0] or triplets[r][1] > target[1] or triplets[r][2] > target[2]):
                r += 1
            while l < r and (triplets[l][0] > target[0] or triplets[l][1] > target[1] or triplets[l][2] > target[2]):
                l += 1

            if r < len(triplets):
                triplets[r] = [max(triplets[l][i], triplets[r][i]) for i in range(3)]
                if triplets[r] == target:
                    return True
                l = r
                r +=1 
        return False