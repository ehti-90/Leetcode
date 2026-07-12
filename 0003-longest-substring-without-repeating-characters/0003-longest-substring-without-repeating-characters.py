class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

       ####################### my brute force technique O(n^2)
        # max_len = 0
        # for i in range(0, len(s)):

        #     char_set = set()
        #     for j in range(i, len(s)):
        #         if s[j] in char_set:
        #             break
        #         char_set.add(s[j])
        #         max_len = max(max_len, j-i+1)

        # return max_len

        ################# Optimized O(n)
        left = 0
        right = 0
        my_dict = {}
        maxi = 0

        while right < len(s):
            if s[right] in my_dict:
                left = max(left, my_dict[s[right]] + 1 )    # left does not go back to char index but foward
                                                            # to new index of reapeated char
            maxi = max(maxi, right - left + 1)
            my_dict[s[right]] = right
            right += 1

        return maxi

                