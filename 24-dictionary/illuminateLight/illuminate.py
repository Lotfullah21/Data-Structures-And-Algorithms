

class Solution:
    def gridIllumination(self, n, lamps, queries):
        # Create empty dictionaries for four directions and grid indices
        m1,m2,m3,m4,m5 = {},{},{},{},{}
        # Place the lamps in the dictonaries
        for lamp in lamps:
            row = lamp[0]
            col = lamp[1]
            # If there is a lamp in a cell, it illuminates that column, that row and top left diagonal and top right diagonal.
            # We based on lamp location given by row and col, we are illuminating the corresponding cells and counting if there are more than one lamp in one cell.
            m1[row] = m1.get(row, 0)+1
            m2[col] = m2.get(col, 0)+1
            m3[row-col] = m3.get(row-col,0)+1
            m4[row+col] = m4.get(row+col,0)+1
            m5[row*n+col] = m5.get(row*n+col,0)+1
            # One answer for one query.
            ans = [0]*len(queries)
            # Each cell can illuminate all 8 adjacent directions and itself, in this array, we are saving all 9 possible movements
        directions = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[0,0]]
        # Search For given queries, if present return the answer and switch of the lamp.
        for i in range(len(queries)):
            x = queries[i][0]
            y = queries[i][1]
            if m1.get(x,0)>0 or m2.get(y,0)>0 or m3.get(x-y,0)>0 or m4.get(x+y,0)>0:
                ans[i] = 1
                # Switch off the lamp for all nine adjacent directions of current query
            for d in directions:
                # Create adjacent boxes for queries
                newX = x + d[0]
                newY = y + d[1]
                    # Check if lamp is illuminating in the new cells.
                    # Create adjacent boxes for queries
                # The boxes should be within the matrix and there is a lamp, then remove all lamps from adjacent.
                if 0<=newX<n and 0<=newY<n and (newX*n+newY) in m5:
                    # 
                    times = m5[ newX*n+newY]
                    m1[newX] = m1[newX]-times
                    m2[newY] = m2[newY]-times
                    m3[newX-newY] = m3[newX-newY]-times
                    m4[newX+newY] = m4[newX+newY]-times
                    del m5[newX*n+newY]     
            return ans    
                    