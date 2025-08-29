from heapq import heappush, heappop, heapify

def will_intersect_before_dest(x_lead,v_lead,x_follow,v_follow,dest):
    if v_lead >= v_follow:
        return False
    leader_time_to_dest = (dest - x_lead)/v_lead
    time_to_intersect = (x_lead-x_follow)/(v_follow-v_lead)
    if time_to_intersect <= leader_time_to_dest:
        return True
    return False

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # My soln is O(n) SC and O(nlogn) TC
        # Basically, we're gonna reduce the # of fleets based calculations between leaders
        # and followers.
        # MISTAKE 1: missed an edge case where time to intersect is negative, namely where
        # the leader speed is faster than the follower speed.
        fleets = len(position)
        heap = [(-pos,vel) for pos,vel in zip(position,speed)] #Careful, pos is -
        heapify(heap)
        leader_x,leader_v = heappop(heap)
        leader_x = -leader_x
        while heap:
            follower_x,follower_v = heappop(heap)
            follower_x = -follower_x
            if will_intersect_before_dest(leader_x,leader_v,follower_x,follower_v,target):
                # NOTE: we're calculating time to dest every call here, better to pass & update with leader update
                fleets -= 1
            else:
                leader_x = follower_x
                leader_v = follower_v
        return fleets
