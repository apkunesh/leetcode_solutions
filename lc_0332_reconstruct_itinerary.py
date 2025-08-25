# NOTE: First thought is, construct nodes whose children are heaps, go to those buggers,
# construct doubly-linked list popping from heap;
# Then if any connections remain, find the lexically-largest and traverse backwards until we hit this one. Take the node (from our main connect) and traverse again until we again
from collections import defaultdict
from heapq import heappop, heappush
from typing import Dict, List, Optional, Tuple


class DirectedNode:
    def __init__(self, value):
        self.val = value
        self.children: List[DirectedNode] = []

    def __hash__(self):
        return self.val

    def __lt__(self, other):
        return self.val < other.val


class LinkedNode:
    def __init__(self, value: str):
        self.val: str = value
        self.left: "LinkedNode" = None
        self.right: "LinkedNode" = None


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        node_map: Dict[str, DirectedNode] = {}
        connection_count: Dict[Tuple[str, str], int] = defaultdict(int)
        for source, dest in tickets:
            connection_count[(source, dest)] += 1
            if node_map.get(source) is None:
                node_map[source] = DirectedNode(source)
            if node_map.get(dest) is None:
                node_map[dest] = DirectedNode(dest)
            heappush(node_map[source].children, node_map[dest])
        # Cool, now we traverse, starting from JFK and going until we can't go anymore.
        dum_left = LinkedNode("dum_left")
        dum_right = LinkedNode("dum_right")
        dum_left.right = dum_right
        dum_right.left = dum_left
        cur_node = node_map["JFK"]
        linked_left = dum_left
        linked_right = dum_right
        while cur_node:
            print("Adding ", cur_node.val)
            linked_left.right = LinkedNode(cur_node.val)
            linked_right.left = linked_left.right
            linked_left.right.left = linked_left
            linked_left.right.right = linked_right.left
            if linked_left.val != "dum_left":
                print("decrementing")
                connection_count[(linked_left.val, linked_left.right.val)] -= 1
            if connection_count[(linked_left.val, linked_left.right.val)] == 0:
                del connection_count[(linked_left.val, linked_left.right.val)]
            if not cur_node.children:
                cur_node = None
                continue
            cur_node = heappop(cur_node.children)
            linked_left = linked_left.right
        no_more = list(connection_count.keys()) == []
        print(no_more)
        while not no_more:
            raise Exception("This far")
            conn_count_keys = list(connection_count.keys())
            print("KEYS ", conn_count_keys)
            print("VALS ", list(connection_count.values()))
            biggest_str = max(conn_count_keys)
            match_link: LinkedNode = dum_right

            while (
                match_link.val != biggest_str
            ):  # NOTE: Could there be inaccessible areas using this method? If so, we actually want the union of these keys and the already-present keys.
                print(match_link.val, biggest_str)
                match_link = match_link.left  # type: ignore
            cur_node = node_map[match_link.val]
            val_to_match = cur_node.val
            cur_node = heappop(cur_node.children)
            linked_left = match_link
            linked_right = match_link.right
            # traverse right-to-left until we find the node matching biggest_str``

            while (
                cur_node
            ):  # TODO: Update such that we quit once we loop back. Most of this while should be changed.
                if cur_node.val == val_to_match:
                    connection_count[(linked_left.val, linked_left.right.val)] -= 1
                    cur_node = None
                    continue
                linked_left.right = LinkedNode(cur_node.val)
                linked_right.left = linked_left.right
                linked_left.right.left = linked_left
                linked_left.right.right = linked_right.left
                connection_count[(linked_left.val, linked_left.right.val)] -= 1
                if connection_count[(linked_left.val, linked_left.right.val)] == 0:
                    del connection_count[(linked_left.val, linked_left.right.val)]
                if not cur_node.children:
                    cur_node = None
                    continue
                cur_node = heappop(cur_node.children)
                linked_left = linked_left.right
            no_more = list(connection_count.keys()) == []

        # Finally, traverse and report the output
        cur = dum_left.right
        output = []
        while cur != "dum_right":
            output.append(cur.val)
            cur = cur.right

        return output


Solution().findItinerary([["BUF", "HOU"], ["HOU", "SEA"], ["JFK", "BUF"]])
