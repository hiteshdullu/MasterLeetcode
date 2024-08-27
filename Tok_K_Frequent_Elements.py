class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        mf = 0
        for i in range(len(nums)):
            m[nums[i]] = m.get(nums[i], 0) + 1
            if mf < m[nums[i]]:
                mf = m[nums[i]]
        
        arr = [0]*(mf+1)
        for i in m:
            if arr[m[i]] == 0:
                arr[m[i]] = [i]
            else:
                arr[m[i]].append(i)

        ans = []
        for i in range(len(arr)-1, -1, -1):
            if arr[i] != 0:
                for j in arr[i]:
                    ans.append(j)
                    k-=1
                    if k == 0:
                        return ans
        return ans
