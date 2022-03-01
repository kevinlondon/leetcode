class Solution:
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def exist(self, board, word):
        if not board:
            return False

        def dfs(x, y, search_word):
            if not search_word:
                # We've trimmed it already
                return True

            if not (0 <= x < len(board[0]) and 0 <= y < len(board)):
                return False
            elif board[y][x] != search_word[0]:
                return False

            board[y][x] = '#'
            next_word = search_word[1:]
            for direction in self.directions:
                n_x, n_y = x + direction[0], y + direction[1]
                if dfs(n_x, n_y, next_word):
                    return True

            board[y][x] = search_word[0]
            return False

        for y in range(len(board)):
            for x in range(len(board[0])):
                found = dfs(x, y, word)
                if found:
                    return True

        return False

