class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # 3,5 -> [1,2] and [5]
        # -> 1 to 5//2 for the left (1+2)//2 * 2, that is (1+k//2)/2 * k//2 -> (1+2)
        left_contribution = (
            int(((1 + k // 2) / 2) * (k // 2)) if n > k // 2 else (n + n * n) // 2
        )
        if n <= k // 2:
            return left_contribution
        right_contribution = (
            k if n == k // 2 + 1 else ((n - k // 2) * (2 * k + n - 1 - k // 2)) // 2
        )
        print(f"LEFT, RIGHT {[left_contribution,right_contribution]}")
        return left_contribution + right_contribution

    def minimumSumOneLiner(self, n, k) -> int:
        # NOTE: This is not quite right after adjusting left side compute above
        return (
            min([(k + (k * k) // 2) // 4, (n + n * n) // 2])
            if n <= k // 2
            else min([(k + (k * k) // 2) // 4, (n + n * n) // 2])
            + (k if n == k // 2 + 1 else ((n - k // 2) * (2 * k + n - 1 - k // 2)) // 2)
        )


print(f"{Solution().minimumSum(5,4)} should be 18")
print(f"{Solution().minimumSum(2,6)} should be 3")
print(f"{Solution().minimumSum(1,1)} should be 1")
print(f"{Solution().minimumSum(2,3)} should be 4")
print(f"{Solution().minimumSum(3,1)} should be 6")
print(f"{Solution().minimumSum(3,5)} should be 8")

# print("Similarly, ")
# print(f"{Solution().minimumSumOneLiner(5,4)} should be 18")
# print(f"{Solution().minimumSumOneLiner(2,6)} should be 3")
# print(f"{Solution().minimumSumOneLiner(1,1)} should be 1")
# print(f"{Solution().minimumSumOneLiner(2,3)} should be 4")
# print(f"{Solution().minimumSumOneLiner(3,1)} should be 6")


"""
Take n=13.
The minimal such array is [1,2,3,4,5,6], as 7 and 6 would sum to 13.
The trouble is if n is too large. For example, say n is 8 and k is 7.
We could start with 
[1,2,3]
but if we include 4, we're in a bad state. We need 5 more, but we cannot use any elements between 4 and 8, exclusive.
[5,6,7] are all out. Therefore, we have to add [8,9,10,11,12]. The sum is then 56.
Are there any choices which would reduce this sum further?
*no*. For every positive integer less than k, there's a friend which sums to k. Taking all elements <=k//2 allows us to have all of these.
Then the remainder are all numbers <= k, which obviously have no positive friend in the array.
So, for a given n, k:
 - if n<=k//2, we have elements [1,2,...k//2], so for example 3,6 3,7, 3,8 we have [1,2,3] in the cases of the first two and [1,2,3] for the latter.
 What does this slice contribute? Well, it's going to be the average of the beginning and ending times the number of elements, so the minimum of ((1+k//2)/2)*(k//2) and ((1+n//2)/2)*(n//2)
 - now if n>k//2, we have to deal with the pieces *beyond*. For example, 5,8 gives not only [1,2,3,4] -> (1+8//2)/2 * (8//2) = 10 but also [8], which is obviously just 8.
 - What, in general does that extra slice contribute?
 well, the # of elements we'll need are n - k//2. For 5,8, this is just 1; for 5,9, also 1.
    - Note that if n==k//2, this is just the 1 element.
    - Otherwise, the first element is k, and the last element is (k + (n-k//2) -1). For example, 7,8 has the first four: [1,2,3,4], but the last 3 elements [8,9,10] start at 8 and go up to 10. Does this match (k+(n-k//2)-1)? (8+(7-4)-1) is 10, indeed. So the contribution is (n-k//2) * (k + (k+(n-k//2)-1))/2, or (n-k//2)*(2*k+n-1-k//2)/2
 # NOTE THE EDGE CASE of k=1!

"""

"""
You are given two integers, n and k.

An array of distinct positive integers is called a k-avoiding array if there does not exist any pair of distinct elements that sum to k.

Return the minimum possible sum of a k-avoiding array of length n.

 

Example 1:

Input: n = 5, k = 4
Output: 18
Explanation: Consider the k-avoiding array [1,2,4,5,6], which has a sum of 18.
It can be proven that there is no k-avoiding array with a sum less than 18.

Example 2:

Input: n = 2, k = 6
Output: 3
Explanation: We can construct the array [1,2], which has a sum of 3.
It can be proven that there is no k-avoiding array with a sum less than 3.

 

Constraints:

    1 <= n, k <= 50

"""
