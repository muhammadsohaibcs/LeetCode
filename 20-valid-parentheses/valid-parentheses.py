class Solution:
    def isValid(self, j: str) -> bool:
        dictionary = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        arr = []
        for s in j :
            if s in ["(" , "{" , "["]:
                arr.append(s)
            elif s in  [")" , "}" , "]"]:
                try:
                    if arr.pop() == dictionary[s]:
                        continue
                    else:
                        return False 
                except :
                    return False 
        return len(arr) == 0
         