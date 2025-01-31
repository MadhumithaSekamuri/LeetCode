class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        maximum_candies = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maximum_candies:
                res.append(True)
            else:
                res.append(False)
        return res
            