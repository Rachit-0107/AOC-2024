import math

def main():
    with open("input.txt", "r") as f:
        grid = [list(line.strip()) for line in f]
    
    antennas = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != ".":
                antennas.append((grid[row][col], row, col)) 

    rows, cols = len(grid), len(grid[0])
    antinode_positions = set()
    
    for i in range(len(antennas)):
        freq1, row1, col1 = antennas[i]
        for j in range(i + 1, len(antennas)):
            freq2, row2, col2 = antennas[j]
            
            if freq1 == freq2: 
                if row1 == row2:
                    left_col = min(col1, col2) - abs(col1 - col2)
                    right_col = max(col1, col2) + abs(col1 - col2)
                    antinode_positions.add((row1, left_col))
                    antinode_positions.add((row1, right_col))
                
                elif col1 == col2:
                    top_row = min(row1, row2) - abs(row1 - row2)
                    bottom_row = max(row1, row2) + abs(row1 - row2)
                    antinode_positions.add((top_row, col1))
                    antinode_positions.add((bottom_row, col1))
                
                else:
                    slope = (row2 - row1) / (col2 - col1)
                    for c in range(cols):
                        r = row1 + slope * (c - col1)
                        if r % 1 != 0:
                            continue
                        r = int(r)
                        if 0 <= r < rows:
                            antinode_positions.add((r, c))

    valid_positions = {(r, c) for r, c in antinode_positions if 0 <= r < rows and 0 <= c < cols}
    
    print(len(valid_positions))

main()
