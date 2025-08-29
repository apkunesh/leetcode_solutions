class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # Wow, totally silly mistake: forgot to iterate, moving the most recent element to the old
        # current element.
        # Could be a good idea to just include this line as soon as I think of it.
        # This is Kadane's with a different requirement: if the flip doesn't happen, 
        # We reset the sum
        def less_than(x,y):
            return x<y
        def greater_than(x,y):
            return x>y
        max_turb_len = 1
        last = arr[0]
        next_compar = None
        cur_len = 1
        for i in range(1,len(arr)):
            if not next_compar:
                next_compar = greater_than if last>arr[i] else less_than
            if next_compar(last,arr[i]):
                cur_len += 1
                max_turb_len = max(cur_len,max_turb_len)
                next_compar = less_than if next_compar == greater_than else greater_than

            elif last == arr[i]:
                cur_len=1
                next_compar = None
            else:
                cur_len = 2
                next_compar = greater_than if last<arr[i] else less_than
            last = arr[i]
            print(str(last) + " and " +str(arr[i]) + " gives " + str(cur_len))
        return max_turb_len