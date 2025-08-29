class PointNode:
    def __init__(self,point):
        self.point = point
        self.dist_sq = point[0]**2+point[1]**2

class PointHeap:
    # Much better than last problem. Mistakes here cenetered around
    # type issues (oops) and minor typos. A "dry run" / second
    # reading of the code was quite useful in spotting
    # a few careless mistakes.
    def __init__(self,points):
        self.points = [PointNode(point) for point in points]
        self._heapify()

    def _percolate_down(self,index):
            cur = index
            found = False
            while not found:
                has_left_child = 2*cur <= len(self.points) - 1
                has_right_child = 2*cur+1 <= len(self.points) - 1
                if not has_right_child and not has_left_child:
                    # We are a leaf!
                    found = True
                    continue
                cur_dist = self.points[cur].dist_sq
                left_child_dist = self.points[2*cur].dist_sq if has_left_child else 10000000000
                right_child_dist = self.points[2*cur+1].dist_sq if has_right_child else 10000000000
                if cur_dist <= left_child_dist and cur_dist <= right_child_dist:
                    # We're in the right interior position
                    found = True
                    continue
                elif left_child_dist <= right_child_dist:
                    # Left is smaller, swap up
                    tmp = self.points[2*cur]
                    self.points[2*cur] = self.points[cur]
                    self.points[cur] = tmp
                    cur = 2*cur
                elif right_child_dist < left_child_dist:
                    tmp = self.points[2*cur+1]
                    self.points[2*cur+1] = self.points[cur]
                    self.points[cur] = tmp
                    cur = 2*cur+1
                else:
                    raise Exception("This should not be reachable")

    def _heapify(self):
        self.points.append(self.points[0])
        self.points[0] = PointNode([0,0])
        max_index = len(self.points)-1
        first_with_children = max_index // 2
        for i in reversed(range(first_with_children+1)):
            if i ==0:
                # Don't mess with dummy node
                break
            self._percolate_down(i)
 
    def pop(self):
        if len(self.points) == 1:
            return None
        if len(self.points) == 2:
            return self.points.pop()
        least_distance = self.points[1]
        self.points[1] = self.points.pop()
        self._percolate_down(1)
        return least_distance


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        point_heap = PointHeap(points)
        closest_points = []
        for i in range(k):
            closest_points.append(point_heap.pop())
        return [point.point for point in closest_points]