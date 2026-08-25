class Solution:
    def groupAnagrams(self, strs):
        finalDic={}
        for x in strs:
            sortedS = ''.join(sorted(x))
            if sortedS in finalDic:
                finalDic.get(sortedS).append(x)
            else:
                finalDic[sortedS]=[x]
         
        final=list(finalDic.values())
        return final
        
        