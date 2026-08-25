class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check={}
        for i,num in enumerate(nums):
            if num in check :
                return True
            check[num]=i
        return False
        
    
        