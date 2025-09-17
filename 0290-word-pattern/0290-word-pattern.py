class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern)!= len(words):
            return False
        p2w, w2p ={} , {}
        for p,w in zip(pattern,words):
            if (p in p2w and p2w[p]!=w) or (w in w2p and w2p[w]!=p):
                return False
            p2w[p]=w
            w2p[w]=p
        return True