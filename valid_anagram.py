class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1, map2 = {}, {}
        for i in s:
            if i not in map1:
                map1[i] = 0
            else:
                map1[i] += 1
        
    
        for j in t:
            if j not in map2:
                map2[j] = 0
            else:
                map2[j] += 1
        
        
        for k in map1:
            print(map1, map2)
            if map2.get(k) != map1.get(k):
                return False
        if len(map1) != len(map2):
            return False
        
        # print(map1, map2)
        return True
