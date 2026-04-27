class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        counts={}
        countt={}
        for c in s:
            counts[c]=counts.get(c,0)+1
        for c in t:
            countt[c]=countt.get(c,0)+1
        return counts==countt
        
            
