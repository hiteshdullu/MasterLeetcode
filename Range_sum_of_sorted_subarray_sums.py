class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sub_array_sum = []
        for i in range(len(nums)):
            current_sum = nums[i]
            sub_array_sum.append(current_sum)
            for j in range(i+1, len(nums)):
                current_sum = current_sum+nums[j]
                sub_array_sum.append(current_sum)
        sub_array_sum.sort()
        return sum(sub_array_sum[left-1: right])%(pow(10, 9)+ 7)
