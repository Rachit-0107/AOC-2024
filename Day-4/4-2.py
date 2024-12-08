def valid(matrix, i, j):
    if j + 1 >= len(matrix[i]) or j - 1 < 0 or i + 1 >= len(matrix) or i - 1 < 0:
        return False
    if matrix[i-1][j-1] == 'M' and matrix[i+1][j+1] == 'S' and matrix[i+1][j-1] == 'M' and matrix[i-1][j+1] == 'S':
        return True
    if matrix[i-1][j-1] == 'M' and matrix[i+1][j+1] == 'S' and matrix[i+1][j-1] == 'S' and matrix[i-1][j+1] == 'M':
        return True
    if matrix[i-1][j-1] == 'S' and matrix[i+1][j+1] == 'M' and matrix[i+1][j-1] == 'M' and matrix[i-1][j+1] == 'S':
        return True
    if matrix[i-1][j-1] == 'S' and matrix[i+1][j+1] == 'M' and matrix[i+1][j-1] == 'S' and matrix[i-1][j+1] == 'M':
        return True
    return False


def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    
    matrix = [list(line.strip()) for line in lines]
    answer = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'A':
                if(valid(matrix, i, j)):
                    answer += 1
    
    print(answer)
                

main()