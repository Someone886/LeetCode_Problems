# Last updated: 5/17/2025, 12:12:49 AM
class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.in_stack = []  # Stack for pushing elements
        self.out_stack = [] # Stack for popping and peeking elements

    def push(self, x: int) -> None:
        """
        Push element x to the back of the queue.
        """
        self.in_stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of the queue and returns that element.
        """
        self._transfer_elements()
        return self.out_stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        self._transfer_elements()
        return self.out_stack[-1] # Peek at the top of the out_stack

    def empty(self) -> bool:
        """
        Returns true if the queue is empty, false otherwise.
        """
        return not self.in_stack and not self.out_stack

    def _transfer_elements(self) -> None:
        """
        Helper function to transfer elements from in_stack to out_stack
        when out_stack is empty.
        """
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()