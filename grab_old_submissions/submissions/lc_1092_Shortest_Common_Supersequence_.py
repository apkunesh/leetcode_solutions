from collections import defaultdict
class StringNode():
    def __init__(self,val,ind_1,ind_2):
        self.val = val
        self.ind_1 = ind_1
        self.ind_2 = ind_2

        # TODO: Include anki for string inserts
        # TODO: include anki for insert at end of array
    
    def spawn_children(self,char,right_or_up):
        all_children = []
        if right_or_up == "right":
            for i in range(self.ind_1,len(self.val)+1):
                if i<len(self.val) and self.val[i] == char:
                    # no val update, just index 1 increment
                    all_children.append(StringNode(self.val,i+1,self.ind_2+1 if self.ind_2>self.ind_1 else self.ind_2))
                else:
                    # val insert and increment index 1, perhaps index 2 if larger than index 1
                    all_children.append(StringNode(self.val[0:self.ind_1]+char+self.val[self.ind_1:],i+1,self.ind_2+1 if self.ind_2>self.ind_1 else self.ind_2))
        elif right_or_up == "up":
            for i in range(self.ind_2,len(self.val)+1):
                if i<len(self.val) and self.val[i] == char:
                    all_children.append(StringNode(self.val,self.ind_1+1 if self.ind_1>self.ind_2 else self.ind_1,i+1))
                else:
                    # val insert and incremet index 2
                    all_children.append(StringNode(self.val[0:self.ind_2]+char+self.val[self.ind_2:],self.ind_1+1 if self.ind_1>self.ind_2 else self.ind_1,i+1))
        else:
            raise Exception("This shouldn't be possible")
        return all_children

def smallest_nodes(list_stringnode):
    if not list_stringnode:
        return None
    cur_smallest = list_stringnode[0]
    small_list = [cur_smallest]
    for string_node in list_stringnode[1:]:
        if (string_node.ind_1 + string_node.ind_2) < (cur_smallest.ind_1+cur_smallest.ind_2):
            small_list = [string_node]
            continue
        if (string_node.ind_1 + string_node.ind_2) > (cur_smallest.ind_1+cur_smallest.ind_2):
            # don't include this one
            continue
        # now all is equal
        small_list.append(string_node)
    present_set = set()
    tiny_list = []
    for node in small_list:
        if (node.val,node.ind_1,node.ind_2) in present_set:
            continue
        tiny_list.append(node)
        present_set.add((node.val,node.ind_1,node.ind_2))
    return tiny_list

def print_row(row):
    all_str = ""
    for children in row:
        entry_str = "["
        for child in children:
            entry_str = entry_str + child.val + str(child.ind_1) + str(child.ind_2)+", "
        all_str = all_str + entry_str[:-2] + "], "
    print(all_str)

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # str 1 goes across top, str 2 on vertical
        row = [[StringNode('',0,0)]]
        for char in str1:
            children = []
            for child in row[-1]:
                children = children + child.spawn_children(char,'right')
            row.append(smallest_nodes(children))
        print_row(row)
        for i in range(len(str2)):
            new_row = [row[0][0].spawn_children(str2[i],'up')]
            for j,char in enumerate(str1):
                children = []
                for child in row[j+1]:
                    children = children + child.spawn_children(str2[i],'up')
                for child in new_row[-1]:
                    children = children + child.spawn_children(char,'right')
                new_row.append(smallest_nodes(children))
            row = new_row
        min_length = len(row[-1][0].val)
        cur_best = row[-1][0]
        for node in row[-1]:
            if len(node.val) < min_length:
                cur_best = node
                min_length = len(node.val)
        return cur_best.val