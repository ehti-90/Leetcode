class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # answer = []
        # my_dic = {}

        # my_len = len(nums)
        
        # for i in range(0,my_len):
        #     product = 1

            
        #     for j in range(i+1,my_len):
        #         product *= nums[j]

        #     for key, val in my_dic.items():        ---------> first brute force 
        #         product *= val
        #     my_dic[i] = nums[i]
            
        #     answer.append(product)
            
        # return answer

        n = len(nums)

        prefix = [1] * n
        suffix = [1] * n
        answer = [1] * n

        # Build prefix array
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # Build suffix array
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        # Multiply prefix and suffix
        for i in range(n):
            answer[i] = prefix[i] * suffix[i]

        return answer