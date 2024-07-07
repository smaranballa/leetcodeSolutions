class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for str1 in strs:
            order = [0] * 26
            for char in str1:
                order[ord(char) - ord("a")] += 1
            result[tuple(order)].append(str1)
        
        return result.values()
