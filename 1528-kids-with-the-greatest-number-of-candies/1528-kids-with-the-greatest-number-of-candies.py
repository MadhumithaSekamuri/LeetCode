class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = [True]*len(candies)
        maximum_candies = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies < maximum_candies:
                res[i]=False
        return res
            