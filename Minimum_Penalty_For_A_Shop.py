class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        y_count = [0]*n
        n_count = [0]*n
        ycount = 0
        ncount = 0
        for i in range(n):
            if customers[i] == "N":
                ncount +=1
            n_count[i] = ncount
        for i in range(n-1, -1, -1):
            if customers[i] == "Y":
                ycount+=1
            y_count[i] = ycount
        min_pen = ncount+1
        time = n
        for i in range(n):
            if customers[i] == "Y":
                if y_count[i] + n_count[i] < min_pen:
                    min_pen = y_count[i] + n_count[i]
                    time = i
            else:
                if y_count[i] + n_count[i]-1 < min_pen:
                    min_pen = y_count[i]- 1 + n_count[i]
                    time = i
        return n if min_pen is ncount+1 else time
