class Solution:
    def climbStairs(self, n: int) -> int:
        # Dynamic-Programming problem. We'll try bottom-up.
        # Idea: every step we add means we can do everything up to the previous step
        # (adding a single step) AND everything up to two steps ago (adding two steps).
        add_two_step,add_one_step = 1,1
        for i in range(n-1):
            new = add_two_step + add_one_step
            add_one_step = add_two_step
            add_two_step = new
        return add_two_step