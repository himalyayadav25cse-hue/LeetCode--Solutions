class Solution:
    def grayCode(self, n):
        result = []
        
        for i in range(1 << n):   # 2^n
            result.append(i ^ (i >> 1))
        
        return result