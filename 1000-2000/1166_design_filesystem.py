class PathComponent:
    def __init__(self):
        self.children = defaultdict(PathComponent)
        self.value = -1

class FileSystem:

    def __init__(self):
        self.fs = PathComponent()

    def createPath(self, path: str, value: int) -> bool:
        path_components = path.lstrip("/").split("/")

        node = self.fs
        for i, component in enumerate(path_components):
            if i == len(path_components)-1:
                if component in node.children:
                    return False
                else:
                    node.children[component].value = value
            else:
                if component not in node.children:
                    return False

                node = node.children[component]

        return True

    def get(self, path: str) -> int:
        path_components = path.lstrip("/").split("/")

        node = self.fs
        for component in path_components:
            if component not in node.children:
                return -1

            node = node.children[component]

        return node.value


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
