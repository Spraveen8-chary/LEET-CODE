from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prev = strs[0]
        for i in strs:
            while not i.startswith(prev):
                prev = prev[:-1]                
        return prev

print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))