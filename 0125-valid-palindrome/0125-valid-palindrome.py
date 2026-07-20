class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        my_string = [ ch for ch in s if ch.isalnum()] # .alpha  includes alphabet chars and .alnum includes onlu nums and alphas

       

        left = 0 
        right = len(my_string) - 1

        while left <= right:
            if my_string[left] == my_string[right]:
                left += 1
                right -= 1
            else:
                return False
        return True



