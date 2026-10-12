class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[] #pair: [index,temp]
        for i,j in enumerate(temperatures):
            while stack and j>stack[-1][1]:
                res[stack[-1][0]]=i-stack[-1][0]
                stack.pop()
            stack.append([i,j])
        return res
                




                
        