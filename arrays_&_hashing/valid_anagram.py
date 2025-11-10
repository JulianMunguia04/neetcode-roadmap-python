class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHash = {}
        tHash = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in sHash:
                sHash[s[i]] = 1
            else: 
                sHash[s[i]] = sHash[s[i]] + 1
            if t[i] not in tHash:
                tHash[t[i]] = 1
            else: 
                tHash[t[i]] = tHash[t[i]] + 1
        if sHash == tHash:
            return True
        return False

#Time Complexity O(n) 