class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    
        num_dict  = {}
        for i, item in enumerate(nums):
            com = target - item
            
            if com in num_dict:     # we chcek if the complement is in dictionary then return com index in dict and i iterating through array
                return [num_dict[com], i] 
                
            num_dict[item] = i  # if not store in in dict as num : index
        return []