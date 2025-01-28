class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        for str1, str2 in zip(word1,word2):
            res.append(str1)
            res.append(str2)
        
        if len(word1) > len(word2):
            res.append(word1[len(word2):])
        elif len(word2) > len(word1):
            res.append(word2[len(word1):])
        return ''.join(res)