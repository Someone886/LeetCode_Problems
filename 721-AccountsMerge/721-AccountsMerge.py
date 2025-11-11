# Last updated: 11/11/2025, 4:18:57 AM
class Union_Find:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
    
    def find(self, node):
        while node != self.parents[node]:
            self.parents[node] = self.parents[self.parents[node]]
            node = self.parents[node]
        
        return node
    
    def union(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)
        if parent1 == parent2:
            return False

        if self.size[parent1] < self.size[parent2]:
            self.parents[parent1] = parent2
            self.size[parent2] += self.size[parent1]
        
        else:
            self.parents[parent2] = parent1
            self.size[parent1] += self.size[parent2]
        
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = Union_Find(len(accounts))
        email_to_acc_index = {}

        for account_index, account in enumerate(accounts):
            for email in account[1:]:
                # email \in account A already seen under another account B
                # union account A and account B
                if email in email_to_acc_index:
                    uf.union(account_index, email_to_acc_index[email])
                else:
                    email_to_acc_index[email] = account_index
        
        email_groups = defaultdict(list)
        for email, account_index in email_to_acc_index.items():
            # email --mapped to--> account_index i --parent--> parent account_index p
            leader_account_index = uf.find(account_index)
            email_groups[leader_account_index].append(email)
        
        output = []
        for leader_account_index, email in email_groups.items():
            leader_account_name = accounts[leader_account_index][0]
            output.append([leader_account_name] + sorted(email_groups[leader_account_index]))
        
        return output