class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        # sort tickets now for lexicographical order
        # destinations are stored in descending lexicographical order
        # when we later do adj[src].pop(),
        # we’ll be removing and visiting the smallest remaining destination.
        for ticket in sorted(tickets)[::-1]:
            adj[ticket[0]].append(ticket[1])
        
        res = []

        def dfs(src):
            while adj[src]:
                next_stop = adj[src].pop()
                dfs(next_stop)
            
            # Note that a dead end always be visited last
            # if src is an dead end, then the algorithm will always stop at src first
            # so src would be appended to res first to be reversed later
            res.append(src)
        
        dfs("JFK")
        return res[::-1]
