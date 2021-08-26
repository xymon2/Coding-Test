#https://leetcode.com/problems/number-of-islands/
#그래프는 1을 0으로 바꾸는 다이나믹식으로 하는 것도 도움이 된다.
#dfs,bfs식으로 풀었더니 시간초과가 뜸

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:

        def expand(i, j):

            if i < 0 or i >= len(grid) or j >= len(grid[0]) or j < 0 or grid[i][j] != '1':
                return

            grid[i][j] = '0'

            expand(i - 1, j)
            expand(i + 1, j)
            expand(i, j + 1)
            expand(i, j - 1)

        cnt = 0
        for i in range(len(grid)):
            for idx, num in enumerate(grid[i]):
                if num == '1':
                    expand(i, idx)
                    cnt += 1

        return cnt


