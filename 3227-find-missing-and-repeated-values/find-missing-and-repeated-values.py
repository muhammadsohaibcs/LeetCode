class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        List = range(1,len(grid) ** len(grid)+1)
        arr = []
        for i in grid:
            arr += i
        repeating = None
        missing = None

        for i in List:
            if repeating and missing:
                break
            if not repeating and arr.count(i) == 2:
                repeating = i
            elif not missing and arr.count(i) == 0:
                missing = i
            
        return [repeating, missing]