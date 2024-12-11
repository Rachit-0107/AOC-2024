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
        val, coord = queue.popleft()
        nines = set()
        queue2 = deque()
        idi = coord[0]
        idj = coord[1]
        queue2.append([0, [idi,idj]])
        while queue2:
            value, coordinates = queue2.popleft()
            i = coordinates[0]
            j = coordinates[1]
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]):
                    if matrix[ni][nj] == value + 1 and value == 8:
                        nines.add((ni, nj))
                    elif matrix[ni][nj] == value + 1:
                        queue2.append([value+1, [ni, nj]])
        answer+= len(nines)
    
    print(answer)

main()