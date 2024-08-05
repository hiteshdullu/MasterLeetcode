class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hashmap = Counter(arr)
        iterator = 0
        while k and iterator < len(arr):
            if hashmap[arr[iterator]] == 1:
                k-=1
            iterator+=1
        if k==0:
            return arr[iterator-1]
        return ""
