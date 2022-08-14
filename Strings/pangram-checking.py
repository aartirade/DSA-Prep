class Solution:
    
    #Function to check if a string is Pangram or not.
    def checkPangram(self,s):
        s=s.lower()
        char="abcdefghijklmnopqrstuvwxyz"
        if len(s)<26:
            return False
       
        for ch in char:
            if ch not in s:
                return False
        return True
        