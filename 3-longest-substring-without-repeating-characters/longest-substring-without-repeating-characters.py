class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        else:
            ans = 0
            visited = []
            for i in s:
                if i not in visited:
                    visited.append(i)
                    ans = max (len(visited) , ans)
                else:
                    visited =visited[visited.index(i)+1: ]
                    visited.append(i)

            return ans
        