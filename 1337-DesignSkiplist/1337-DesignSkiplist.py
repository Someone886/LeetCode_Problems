# Last updated: 6/22/2025, 2:50:45 PM
import random

class Node:
    def __init__(self, val=-1, right=None, down=None):
        self.val = val
        self.right = right
        self.down = down

class Skiplist:

    def __init__(self):
        self.head = Node() 

    def search(self, target: int) -> bool:
        node = self.head

        # layer = 0

        while node:
            # print(layer, node.val, node.right)

            while node.right and node.right.val < target:
                node = node.right
            if node.right and node.right.val == target:
                return True

            # layer += 1
            node = node.down

        return False

    def add(self, num: int) -> None:
        nodes = []
        node = self.head
        while node:
            # Move to the right in the current level
            while node.right and node.right.val < num:
                node = node.right
            nodes.append(node)
            # Move to the next level
            node = node.down
        
        insert = True
        down = None
        while insert and nodes:
            node = nodes.pop()
            node.right = Node(num, node.right, down)
            down = node.right
            insert = (random.getrandbits(1) == 0)      
        
        if insert:
            self.head = Node(-1, None, self.head)

    def erase(self, num: int) -> bool:
        node = self.head
        found = False

        while node is not None:
            while node.right and node.right.val < num:
                node = node.right
            
            if node.right and node.right.val == num:
                found = True
                node.right = node.right.right
                
            node = node.down
        
        return found


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)