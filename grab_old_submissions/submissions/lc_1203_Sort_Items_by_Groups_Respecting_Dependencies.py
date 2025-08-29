#TODO: Need to include cycle detection at both dfs levels

def intra_group_dfs(item,group_dependencies,result,visited_elements,element_path):
    if item in element_path:
        return False
    if item in visited_elements:
        return
    element_path.append(item)
    visited_elements.add(item)
    for child in group_dependencies[item]:
        if intra_group_dfs(child,group_dependencies,result,visited_elements,element_path) is False:
            return False
    result.append(item)
    element_path.pop()

def inter_group_dfs(group_id,inter_group_dependencies,intra_group_dependencies,result,visited_groups, visited_elements,group_to_items,group_path):
    if group_id in group_path:
        return False
    if group_id in visited_groups:
        return
    group_path.append(group_id)
    visited_groups.add(group_id)
    for child in inter_group_dependencies[group_id]:
        if inter_group_dfs(child,inter_group_dependencies,intra_group_dependencies,result,visited_groups, visited_elements,group_to_items,group_path) is False:
            return False
    for item in group_to_items[group_id]:
        element_path = []
        if intra_group_dfs(item,intra_group_dependencies[group_id],result,visited_elements,element_path) is False:
            return False
    group_path.pop()

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        adj = defaultdict(set)
        for i, int_list in zip(range(len(beforeItems)),beforeItems):
            for elem in int_list:
                adj[i].add(elem) # adj leads to the end of the list, such as 6.
        # General idea:
        # Group elements into their groups, first (O(n))
        # Split beforeItems into intra-group and inter-group dependencies (O(len(beforeItems)))
        # Create a topological ordering for each internal set O(n)
        # create a topological ordering over outer sets O(m)
        # Return result
        group_to_items = defaultdict(set)
        no_group_item_to_group = {}
        nongroup_count = 0
        for i,elem in zip(range(len(group)),group):
            if elem == -1: # Elements without groups will be put into their own pseudo-group
                group_to_items[m+nongroup_count].add(i)
                no_group_item_to_group[i] = m+nongroup_count
                nongroup_count+=1
            else:
                group_to_items[elem].add(i) # Note that group-to-items contains all elements in its values
        inter_group_dependencies = defaultdict(set) # {group: set(dependent groups)}
        intra_group_dependencies = defaultdict(lambda: defaultdict(set)) # {group: {item: set(dependent items)}
        for upstream, downstream_set in adj.items():
            for downstream in downstream_set:
                if group[upstream] == group[downstream] and group[upstream] != -1:
                    shared_group = group[upstream]
                    intra_group_dependencies[shared_group][upstream].add(downstream)
                else:
                    upstream_group = group[upstream]
                    downstream_group = group[downstream]
                    if upstream_group == -1:
                        upstream_group = no_group_item_to_group[upstream]
                    if downstream_group == -1:
                        downstream_group = no_group_item_to_group[downstream]
                    inter_group_dependencies[upstream_group].add(downstream_group)
        # Now we do topological sort (dfs-style) on the inter-group and intra-group deps.
        result = []
        visited_groups = set()
        visited_elements = set()
        for group_id in list(group_to_items.keys()):
            group_path = []
            if inter_group_dfs(group_id,inter_group_dependencies,intra_group_dependencies,result,visited_groups, visited_elements,group_to_items,group_path) is False:
                return []
        return result
