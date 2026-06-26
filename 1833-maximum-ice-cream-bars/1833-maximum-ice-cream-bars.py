class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        ans = 0 
        costs.sort()
        for cost in costs:
            if cost > coins:
                break
            ans += 1
            coins -= cost
        return ans
        