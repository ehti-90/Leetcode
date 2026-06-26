class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        rev_num = 0
        num = x

        if num < 0:
            return False

        while num > 0:
            last_dig =  num % 10
            rev_num = rev_num * 10 + last_dig
            num //= 10

        if rev_num == x:
            return True
        else:
            return False
        




        