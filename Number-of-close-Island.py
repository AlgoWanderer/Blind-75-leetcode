#1254
#Number of Closed Island Problem.
#This can be solved using either DFS or BFS. I prefer DFS 

class Solution(object):
    def closedIsland(self, grid):
        ROWS, COLS = len(grid), len(grid[0]) #len(grid) is the number of rows and len(grid[0]) is the number of columns 
        visit = set() #created a set for visited nodes

        def dfs(r, c):
            if (r < 0 or c < 0 or  #if r<0 or c<0 i.e. if its negative, it goes out of bound, therefore it is not valid
            r == ROWS or c == COLS):  #if r==ROWS or c==COLS meaning, r and c are the row number we are currently in and if r becomes equal to the number of rows or c becomes equal to number of colums then it is out of bound 
                return 0 #we return false
            if grid[r][c] == 1 or (r, c) in visit: #if the cell is water or if the cell already exist in the visited set, then: 
                return 1 #return true
            
            visit.add((r,c)) #after you visit that cell add that in the cell in the visited node  
            return min(dfs(r + 1 ,c), 
                    dfs(r - 1,c),
                    dfs(r, c + 1),
                    dfs(r, c - 1)) #here we are checking for every direction from the current cell. 0 if any edge reaches 0 else 1
        res = 0 #we initialize the result 
        for r in range(ROWS): #traverse through the rows
            for c in range(COLS): #traverse through the colums
                if grid[r][c] == 0 and (r,c) not in visit: #if its land and is not visited
                    res += dfs(r,c) #keep going
        return res #return the result
