# Problem 721: Accounts Merge
# Difficulty: Medium
# Link: https://leetcode.com/problems/accounts-merge/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph=defaultdict(list)
        email_to_name={}
        for account in accounts:
            name=account[0]
            for i in range(1,len(account)):
                email=account[i]
                email_to_name[email]=name
                if i>1:
                    graph[account[i-1]].append(email)
                    graph[email].append(account[i-1])
        def dfs(email,visited,component):
            visited.add(email)
            component.append(email)
            for neighbor in graph[email]:
                if neighbor not in visited:
                    dfs(neighbor,visited,component)
        visited=set()
        result=[]
        for email in email_to_name:
            if email not in visited:
                component=[]
                dfs(email,visited,component)
                result.append([email_to_name[email]]+sorted(component))
        return result 