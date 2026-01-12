# Last updated: 1/12/2026, 10:03:10 AM
1# """
2# This is the interface that allows for creating nested lists.
3# You should not implement it, or speculate about its implementation
4# """
5#class NestedInteger:
6#    def isInteger(self) -> bool:
7#        """
8#        @return True if this NestedInteger holds a single integer, rather than a nested list.
9#        """
10#
11#    def getInteger(self) -> int:
12#        """
13#        @return the single integer that this NestedInteger holds, if it holds a single integer
14#        Return None if this NestedInteger holds a nested list
15#        """
16#
17#    def getList(self) -> [NestedInteger]:
18#        """
19#        @return the nested list that this NestedInteger holds, if it holds a nested list
20#        Return None if this NestedInteger holds a single integer
21#        """
22
23class NestedIterator:
24    def __init__(self, nestedList: [NestedInteger]):
25        # We put the whole list into a deque
26        self.dq = deque(nestedList)
27
28    def next(self) -> int:
29        # hasNext() ensures the first element is an integer
30        return self.dq.popleft().getInteger()
31    
32    def hasNext(self) -> bool:
33        while self.dq:
34            if self.dq[0].isInteger():
35                return True
36            # If front is a list, pop it and spread its contents to the front
37            first = self.dq.popleft().getList()
38            # We must add them to the left in reverse to maintain order
39            for i in range(len(first) - 1, -1, -1):
40                self.dq.appendleft(first[i])
41        return False
42
43# class NestedIterator:
44#     def __init__(self, nestedList: [NestedInteger]):
45#         self.list = []
46#         self.index = 0
47
48#         def flatten(nested_list):
49#             for item in nested_list:
50#                 if item.isInteger():
51#                     self.list.append(item.getInteger())
52#                 else:
53#                     flatten(item.getList())
54        
55#         flatten(nestedList)
56
57#     def next(self) -> int:
58#         res = self.list[self.index]
59#         self.index += 1
60#         return res
61    
62#     def hasNext(self) -> bool:
63#         return self.index < len(self.list)
64        
65
66# Your NestedIterator object will be instantiated and called as such:
67# i, v = NestedIterator(nestedList), []
68# while i.hasNext(): v.append(i.next())