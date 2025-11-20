class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        newStr = {}
        ans = []
        for i in range(len(strs)):
            a = "".join(sorted( strs [i]))
            newStr[a] =  newStr.get( a, []) + [i]
        for i , j in newStr.items():
            l =[]
            for k in j:
                l.append(strs[k])
            ans.append(l)
        return ans

        