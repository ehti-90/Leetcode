class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        my_string = [ ch for ch in s if ch.isalnum()] 
        # .alpha  includes alphabet chars and .alnum includes onlu nums and alphas

        return my_string == my_string[::-1]




