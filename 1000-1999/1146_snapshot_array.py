import copy

class SnapshotArray:

    def __init__(self, length: int):
        self.snaps = []
        self.set_vals = {}

    def set(self, index: int, val: int) -> None:
        self.set_vals[index] = val

    def snap(self) -> int:
        self.snaps.append(copy.deepcopy(self.set_vals))
        return len(self.snaps) - 1

    def get(self, index: int, snap_id: int) -> int:
        return self.snaps[snap_id].get(index, 0)


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
