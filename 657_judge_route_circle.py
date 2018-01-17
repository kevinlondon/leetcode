class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        if not moves:
            return True
        elif len(moves) % 2 > 0:
            return False
        
        x, y = 0, 0
        for move in moves:
            if move == 'L':
                x -= 1
            elif move == 'R':
                x += 1
            elif move == 'D':
                y -= 1
            elif move == 'U':
                y += 1
        
        return x == y == 0