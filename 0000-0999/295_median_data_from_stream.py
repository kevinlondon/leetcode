from queue import PriorityQueue

class MedianFinder:

    def __init__(self):
        self.min_heap = PriorityQueue()
        self.max_heap = PriorityQueue()

    def addNum(self, num: int) -> None:
        if self.min_heap.qsize() == 0:
            self.min_heap.put(-num)
            return

        if -num < self.min_heap.queue[0]:
            self.max_heap.put(num)
        else:
            self.min_heap.put(-num)

        if self.min_heap.qsize() > self.max_heap.qsize() + 1:
            self.max_heap.put(-self.min_heap.get())
        elif self.min_heap.qsize() + 1 < self.max_heap.qsize():
            self.min_heap.put(-self.max_heap.get())

    def findMedian(self) -> float:
        min_size, max_size = self.min_heap.qsize(), self.max_heap.qsize()
        if not min_size and not max_size:
            return 0

        if min_size == max_size:
            return (-self.min_heap.queue[0] + self.max_heap.queue[0]) / 2
        elif min_size > max_size:
            return -self.min_heap.queue[0]
        else:
            return self.max_heap.queue[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
