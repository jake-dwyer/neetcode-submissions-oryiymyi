class Solution:
    def isPalindrome(self, s: str) -> bool:
        # chars = list(map(chr, range(97, 123))) + list(map(chr, range(65, 91))) +  list(map(chr, range(48, 58)))
        # print(chars)
        
        # for i in s:
        #     if i not in chars:
        #         s = s.replace(i, "")
        
        # if s[::-1].lower() == s.lower():
        #     return True
        # else:
        #     return False

# The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (az) and numbers (0-9).
        s = [i for i in s.lower() if i.isalnum()]
        return s == s[::-1]
            
            