class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        set_s = list(s)
        set_t = list(t)

        if sorted(set_s) == sorted(set_t):
            return True
        else: 
            return False

