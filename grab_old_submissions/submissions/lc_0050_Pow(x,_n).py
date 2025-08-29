class Solution:
    def myPow(self, x: float, n: int) -> float:
        # But brute force is inefficient: we can alternatively bootstrap our way up
        # using the information we already have.
        # Idea:
        # Recursively construct as product of multiple added powers (probably 2,4,8,16, 32, 64)
        if x==0:
            return 0
        cache = {0:1,1:x,-1:1/x}
        def helper(x,n):
            if n in cache:
                return cache[n]
            multiple = x if n%2!=0 else 1
            half = helper(x,n//2)
            cache[n] = half*half * multiple
            return cache[n]
        return helper(x,n)

    
        '''
        # brute force soln would be something like:
        sign = 1 if n>=0 else -1
        result = 1
        for i in range(n*sign):
            result = result * x if sign==1 else result / x
        return result
        '''