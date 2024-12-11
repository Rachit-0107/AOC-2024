from collections import deque

def main():
    with open('input.txt', 'r') as file:
        matrix = [list(line.strip()) for line in file if line.strip()]  
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '.':
                matrix[i][j] = -1
            else:
                matrix[i][j] = int(matrix[i][j])

    queue = deque()

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                queue.append([0, [i,j]])
    
    answer = 0
    while queue:
        value, coord = queue.popleft()
        queue2 = deque()
        i = coord[0]
        j = coord[1]
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]):
                if matrix[ni][nj] == value + 1 and value == 8:
                    answer+=1
                elif matrix[ni][nj] == value + 1:
                    queue.append([value+1, [ni, nj]])
    
    print(answer)

main()