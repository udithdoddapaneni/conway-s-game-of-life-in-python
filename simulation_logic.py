

# conway's game of life


# rule 1: A live cell with fewer than 2 live neighbors dies (underpopulation)
# rule 2: A live cell with 2 or 3 live neighbors remains alive (survival)
# rule 3: A live with more than 3 live neighbors dies (overpopulation)
# rule 4: A dead cell with exactly 3 live neigbors becomes alive (reproduction)


def count_neighbors(grid, i, j):
    count = 0
    if i+1 < len(grid):
        if j+1 < len(grid[0]):
            if grid[i+1][j+1]:
                count += 1
        if j-1 >= 0:
            if grid[i+1][j-1]:
                count += 1
        if grid[i+1][j]:
            count += 1
    if i-1 >= 0:
        if j+1 < len(grid[0]):
            if grid[i-1][j+1]:
                count += 1
        if j-1 >= 0:
            if grid[i-1][j-1]:
                count += 1
        if grid[i-1][j]:
            count += 1
    if j+1 < len(grid[0]):
        if grid[i][j+1]:
            count += 1
    if j-1 >= 0:
        if grid[i][j-1]:
            count += 1
    
    return count


def nextgen(grid: list):
    temp = [[0]*len(grid[0]) for i in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            n = count_neighbors(grid, i, j)
            if n < 2: # underpopulation
                continue
            if n == 2: # survival
                temp[i][j] = grid[i][j]
                continue
            if n == 3: # reproduction
                temp[i][j] = 1
                continue
            if n > 3: # overpopulation
                continue
    
    return temp