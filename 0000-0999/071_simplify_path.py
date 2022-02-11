class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = []

        open_path = []
        def is_cur_dir():
            return len(open_path) == 1 and open_path[0] == '.'

        def is_par_dir():
            return len(open_path) == 2 and open_path[0] == '.' and open_path[1] == '.'

        for letter in path:
            if letter == '/':
                if open_path:
                    if is_par_dir():
                        if dirs:
                            dirs.pop()
                    elif not is_cur_dir():
                        dirs.append(''.join(open_path))
                    open_path = []
            else:
                open_path.append(letter)
        else:
            if is_par_dir():
                if dirs:
                    dirs.pop()
            elif not is_cur_dir() and open_path:
                dirs.append(''.join(open_path))

        return '/' + '/'.join(dirs)

