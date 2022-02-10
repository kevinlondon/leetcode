from queue import Queue

class MovingAverage:

    def __init__(self, size: int):
        if size <= 0:
            raise RuntimeException("Invalid size")

        self.size = size
        self.sum = 0
        self.window = Queue()

    def next(self, val: int) -> float:
        if self.window.qsize() >= self.size:
            removing = self.window.get()
            self.sum -= removing

        self.window.put(val)
        self.sum += val
        return self.sum / self.window.qsize()


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
