"""
    Using hashset calculate the frequency of each element in the array and create another hashset from 
    the values of the previous hashset to group the elements
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        
        freqs = freq.items()
        wow = len(nums)
        n = wow
        reachk = 0
        freqToItems = defaultdict(list)

        for key, value in freq.items():
            freqToItems[value].append(key)
        # print(freqToItems)
        ans = []
        while n > 0:
            print(n, freqToItems[n])
            if n in freqToItems:
                limst = freqToItems[n]
                for i in limst:
                    if k == 0:
                        break
                    k -= 1
                    ans.append(i)
            n -= 1
            # k -= 1
        return ans