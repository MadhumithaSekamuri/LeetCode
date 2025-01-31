class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
                left_plot = (i==0) or (flowerbed[i-1]==0) 
                right_plot = (i==len(flowerbed)-1) or (flowerbed[i+1]==0)
            
                if left_plot and right_plot and flowerbed[i]==0:
                    flowerbed[i]=1
                    n = n-1

        return n<=0

                
            