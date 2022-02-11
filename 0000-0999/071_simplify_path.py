class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = []

        for p in path.split('/'):
            if p == '.' or not p:
                continue
            elif p == '..':
                if dirs:
                    dirs.pop()
            else:
                dirs.append(p)

        return '/' + '/'.join(dirs)

