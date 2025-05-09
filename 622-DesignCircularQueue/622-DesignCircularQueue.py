# Last updated: 4/30/2025, 10:58:26 PM
class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [0] * k
        self.size = k
        self.head = 0
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.count == self.size:
            return False

        else:
            tail = (self.head + self.count) % self.size
            self.arr[tail] = value
            self.count += 1

            return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False

        else:
            self.head = (self.head + 1) % self.size
            self.count -= 1

            return True

    def Front(self) -> int:
        return -1 if self.count == 0 else self.arr[self.head]

    def Rear(self) -> int:
        return -1 if self.count == 0 else self.arr[(self.head + self.count - 1) % self.size]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()