class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        num=0
        row=len(grid)
        col=len(grid[0])
        visited=set()
        
        def dfs(r,c):
            if r<0 or r>=row or c<0 or c>=col or grid[r][c]!='1' or (r,c) in visited:
                return 
            visited.add((r,c))
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        for i in range(row):
            for j in range(col):
                if grid[i][j]=='1' and (i, j) not in visited:
                    num+=1
                    dfs(i, j)
        return num