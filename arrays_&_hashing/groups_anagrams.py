class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashed = {}
        for i in range(len(strs)):
            print(strs[i])
            count = [0] * 26
            for ch in strs[i]:
                count[ord(ch) - ord('a')] += 1
            key = tuple(count)
            print("key", key)
            if key in hashed:
                hashed[key].append(strs[i])
            else: 
                hashed[key] = [strs[i]]
        return list(hashed.values())                  
      
#Time Complexity O(n * m) with n being the amount of strings in strs and m being the lenght of the longest n 