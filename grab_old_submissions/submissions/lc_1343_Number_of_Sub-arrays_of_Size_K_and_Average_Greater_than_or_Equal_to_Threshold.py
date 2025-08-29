class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        curr_sum = sum(arr[0:k-1])
        sum_thresh = threshold * k
        window_count = 0
        for i in range(k-1,len(arr)):
            curr_sum = curr_sum + arr[i]
            if curr_sum >= sum_thresh:
                window_count+=1
            curr_sum -= arr[i-k+1]
        return window_count
