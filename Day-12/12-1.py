from collections import deque

def main():
    with open('input.txt', 'r') as file:
        matrix = [list(line.strip()) for line in file.readlines()]
    
    visited = []
    for _ in range(len(matrix)):
        row = []
        for _ in range(len(matrix[0])):
            row.append(False)
        visited.append(row)
    
    answer = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if visited[i][j] == False:
                val = matrix[i][j]
                perimeter = 0
                area = 0
                queue = deque()
                queue.append([i, j])
                while queue:
                    x, y = queue.popleft()
                    if visited[x][y] == True:
                        continue
                    visited[x][y] = True
                    perimeter += 4
                    area += 1
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and visited[nx][ny] == False:
                            if matrix[nx][ny] == val:
                                queue.append([nx, ny])
                                perimeter -= 2
                answer+= area * perimeter

    print(answer)

main()