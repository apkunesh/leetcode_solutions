class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Modes: 0 right, 1 down, 2 left, 3 up
        mode_to_boundary_index = {0:1,1:0,2:1,3:0}
        mode_to_delta = {0:[0,1],1:[1,0],2:[0,-1],3:[-1,0]}
        mode_to_oob = {0:len(matrix[0]),1:len(matrix),2:-1,3:-1}
        out = []
        curr = [0,0]
        mode = 0
        # At each point, we're going to (1) append to the list and (2) update the delta 
        # and boundary if we are on a boundary.
        # Then we'll attempt to move to the point and check for if we've moved *beyond*
        # a boundary. If we have, we return, as we've made it to the middle.
        while True:
            if curr[0] in [mode_to_oob[1],mode_to_oob[3]] or curr[1] in [mode_to_oob[0],mode_to_oob[2]]:
                return out
            out.append(matrix[curr[0]][curr[1]])
            dist_to_boundary = mode_to_oob[mode] - curr[mode_to_boundary_index[mode]]
            sign = 1 if dist_to_boundary > 0 else -1
            if dist_to_boundary == 1 or dist_to_boundary == -1:
                if mode == 0:
                    mode_to_oob[3]+=1
                elif mode == 1:
                    mode_to_oob[0]-=1
                elif mode == 2:
                    mode_to_oob[1]-=1
                elif mode == 3:
                    mode_to_oob[2]+=1
                mode = (mode+1) % 4
            delta = mode_to_delta[mode]
            curr = [curr[0]+delta[0],curr[1]+delta[1]]