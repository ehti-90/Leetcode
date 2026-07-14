class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        my_dict_s = {}

        for ch in s:
            my_dict_s[ch] = my_dict_s.get(ch, 0) + 1
     
        for ch in t:
            if ch not in my_dict_s:
                return False
            
            my_dict_s[ch] -= 1

            if my_dict_s[ch] == 0:
                del my_dict_s[ch]

        if len(my_dict_s) == 0:
            return True
        return False