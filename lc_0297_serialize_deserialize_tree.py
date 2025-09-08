from typing import Optional


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


# Definition for a binary tree node.


class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def dfs(node: Optional[TreeNode], str_in: str):
            if not node:
                return str_in
            to_return = str_in + f"#{node.val}#"
            if node.left:
                to_return = to_return + "L"
                to_return = dfs(node.left, to_return)
            if node.right:
                to_return = to_return + "R"
                to_return = dfs(node.right, to_return)
            to_return = to_return + "P"
            return to_return

        return dfs(root, "")

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        value = ""
        i = 1
        while data[i] != "#":
            value = value + data[i]
            i += 1
        head = TreeNode(value)
        cur_node = head
        node_stack = [TreeNode("dummy")]
        # print(data)
        i += 1
        while i < len(data):
            cur_char = data[i]
            if cur_char == "P":
                cur_node = node_stack.pop()
                # print("Just popped up to ",cur_node.val)
                # print("it has children ", [cur_node.left.val if cur_node.left else None, cur_node.right.val if cur_node.right else None])
                i += 1
            elif cur_char in ["R", "L"]:
                # print("Adding to stack", cur_node.val)
                node_stack.append(cur_node)
                j = i + 2
                value = ""
                while data[j] != "#":
                    value = value + data[j]
                    j += 1
                i = j + 1
                if cur_char == "R":
                    # print("Creating node to right with value ",value)
                    cur_node.right = TreeNode(int(value))
                    cur_node = cur_node.right
                else:
                    # print("Creating  node to left with value ",value)
                    cur_node.left = TreeNode(int(value))
                    cur_node = cur_node.left
            else:
                raise Exception("Shouldn't be possible, we see ", i)

        return head
