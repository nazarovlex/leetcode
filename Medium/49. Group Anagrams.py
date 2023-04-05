import collections


class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = Solution().groupAnagrams(strs)
print(result)
