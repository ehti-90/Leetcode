class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # if not nums:
        #     return 0
        # nums.sort()
        # current = 1
        # longest = 1

        # for i in range(1, len(nums)):

        #     if nums[i] == nums[i-1]:
        #         continue

        #     elif nums[i] == nums[i-1] + 1:
        #         current += 1

        #     else:
        #         longest = max(longest, current)
        #         current = 1
        # return max(longest, current)

        ## the above solution was nlogn

        numset = set(nums)
        longest = 0 

        for num in numset:
            if (num -1 )  not in numset:

                length = 0
                while (num + length ) in numset:
                    length += 1
                longest = max(length, longest)
        return longest


            





        