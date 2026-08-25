class Solution:
    def isAnagram(self, s,t):
        if(len(s)!=len(t)):
            return False
        if(sorted(list(s))==sorted(list(t))):
            return True
        else:
            return False
        
        
            
        
        

            
        
        