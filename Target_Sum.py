class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def backtrack(i, s, dp):
            if (i, s) in dp:
                return dp[(i, s)]
            if len(nums)==i:
                if target == s:
                    return 1
                return 0
            dp[(i, s)] = backtrack(i+1, s+nums[i], dp) + backtrack(i+1, s-nums[i], dp)
            return dp[(i, s)]
        return backtrack(0, 0, dp)
