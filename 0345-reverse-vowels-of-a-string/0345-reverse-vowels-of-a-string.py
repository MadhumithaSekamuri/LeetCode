class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        s_list = list(s)
        left=0
        right =len(s) - 1

        while left < right:
            while left < right and s_list[left] not in vowels:
                left += 1
            while left < right and s_list[right] not in vowels:
                right -= 1
            
            s_list[left], s_list[right] = s_list[right], s_list[left]
            
            left += 1
            right -= 1
        
        return "".join(s_list)