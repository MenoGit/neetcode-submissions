class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        hashmapS = {};
        hashmapC = {};

        for i in range(len(s)):
            hashmapS[s[i]] = hashmapS.get(s[i],0) + 1;
            hashmapC[t[i]] = hashmapC.get(t[i],0) + 1;
        return hashmapC == hashmapS
