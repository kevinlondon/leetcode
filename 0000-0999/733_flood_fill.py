class Solution:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int, startColor = None) -> List[List[int]]:
        x, y = sc, sr

        def in_bounds(x, y):
            return 0 <= y < len(image) and 0 <= x < len(image[0])

        if not image or not in_bounds(x, y) or (startColor is not None and startColor != image[y][x]):
            return image

        if startColor is None:
            startColor = image[y][x]
            if startColor == newColor:
                return image

        image[y][x] = newColor

        for direction in self.directions:
            n_x, n_y = x + direction[0], y + direction[1]
            self.floodFill(image, n_y, n_x, newColor, startColor)

        return image
