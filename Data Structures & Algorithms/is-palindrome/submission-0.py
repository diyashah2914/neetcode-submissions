import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # convert the string into alphanumeric characters using re
        clean_text = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        # create 2 pointers left and right
        left = 0
        right = len(clean_text) - 1

        while left < right:
            if clean_text[left] != clean_text[right]:
                return False
            left += 1
            right -= 1
        return True



        