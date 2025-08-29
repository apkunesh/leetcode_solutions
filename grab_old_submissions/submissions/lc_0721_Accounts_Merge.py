class UnionFind:
    def __init__(self,unique_emails):
        self.parent = {elem:elem for elem in unique_emails}
        self.ranks = {elem:1 for elem in unique_emails}
    
    def find(self,email):
        if email != self.parent[email]:
            self.parent[email] = self.find(self.parent[email])
        return self.parent[email]

    def join(self,email1,email2):
        root1,root2 = self.find(email1),self.find(email2)
        if root1 == root2:
            return # Already joined, dupe information
        if self.ranks[root1] > self.ranks[root2]:
            self.parent[root2] = root1
        elif self.ranks[root2] > self.ranks[root1]:
            self.parent[root1] = root2
        else:
            self.parent[root1] = root2
            self.ranks[root2] +=1


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Big idea: union find -> dfs (traverse) to get all the accounts. We'll use emails as our union conditions -- name is a
        # red herring. We'll include the name on the node (space-inefficient, future optimization). At the end, we'll do DFS
        # to visit every element of each union-tree and spit out the associated emails.
        # Note that we don't want to add an email if it's duped
        email_to_name = {}
        for account in accounts:
            for email in account[1:]:
                email_to_name[email] = account[0]
        union_find = UnionFind(list(email_to_name.keys()))
        for account in accounts:
            for email_pair in zip(account[1:-1],account[2:]):
                union_find.join(*email_pair)
        root_to_list = {}
        for email in email_to_name:
            root = union_find.find(email)
            if root not in root_to_list:
                root_to_list[root] = []
            root_to_list[root].append(email)
        result = []
        for root,email_list in root_to_list.items():
            email_list.sort()
            result.append([email_to_name[root]]+email_list)
        return result