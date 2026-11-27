class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        start_color = image[sr][sc]
        
        # Avoid infinite recursion if the color doesn't need to change
        if start_color == color:
            return image
            
        rows, cols = len(image), len(image[0])
        
        def dfs(r: int, c: int):
            # Stop if out of bounds or not matching the original color
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != start_color:
                return
            
            # Paint the pixel with the new color
            image[r][c] = color
            
            # Recursively fill the 4 neighboring directions
            dfs(r - 1, c)  # Up
            dfs(r + 1, c)  # Down
            dfs(r, c - 1)  # Left
            dfs(r, c + 1)  # Right

        dfs(sr, sc)
        return image
        