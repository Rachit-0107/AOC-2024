def valid_horizontal_forward(matrix, i, j):
    if j + 2 >= len(matrix[i]):
        return False
    if matrix[i][j] == 'M' and matrix[i][j+1] == 'A' and matrix[i][j+2] == 'S':
        return True
    return False

def valid_horizontal_backward(matrix, i, j):
    if j - 2 < 0:
        return False
    if matrix[i][j] == 'M' and matrix[i][j-1] == 'A' and matrix[i][j-2] == 'S':
        return True
    return False

def valid_vertical_down(matrix, i, j):
    if i + 2 >= len(matrix):
        return False
    if matrix[i][j] == 'M' and matrix[i+1][j] == 'A' and matrix[i+2][j] == 'S':
        return True
    return False

def valid_vertical_up(matrix, i, j):
    if i - 2 < 0:
        return False
    if matrix[i][j] == 'M' and matrix[i-1][j] == 'A' and matrix[i-2][j] == 'S':
        return True
    return False

def valid_diagonal_down_right(matrix, i, j):
    if i + 2 >= len(matrix) or j + 2 >= len(matrix[i]):
        return False
    if matrix[i][j] == 'M' and matrix[i+1][j+1] == 'A' and matrix[i+2][j+2] == 'S':
        return True
    return False

def valid_diagonal_down_left(matrix, i, j):
    if i + 2 >= len(matrix) or j - 2 < 0:
        return False
    if matrix[i][j] == 'M' and matrix[i+1][j-1] == 'A' and matrix[i+2][j-2] == 'S':
        return True
    return False

def valid_diagonal_up_right(matrix, i, j):
    if i - 2 < 0 or j + 2 >= len(matrix[i]):
        return False
    if matrix[i][j] == 'M' and matrix[i-1][j+1] == 'A' and matrix[i-2][j+2] == 'S':
        return True
    return False

def valid_diagonal_up_left(matrix, i, j):
    if i - 2 < 0 or j - 2 < 0:
        return False
    if matrix[i][j] == 'M' and matrix[i-1][j-1] == 'A' and matrix[i-2][j-2] == 'S':
        return True
    return False

def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    
    matrix = [list(line.strip()) for line in lines]
    answer = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'X':
                if(valid_horizontal_forward(matrix, i, j+1)):
                    answer += 1
                if(valid_horizontal_backward(matrix, i, j-1)):
                    answer += 1
                if(valid_vertical_down(matrix, i+1, j)):
                    answer += 1
                if(valid_vertical_up(matrix, i-1, j)):
                    answer += 1
                if(valid_diagonal_down_right(matrix, i+1, j+1)):
                    answer += 1
                if(valid_diagonal_down_left(matrix, i+1, j-1)):
                    answer += 1
                if(valid_diagonal_up_right(matrix, i-1, j+1)):
                    answer += 1
                if(valid_diagonal_up_left(matrix, i-1, j-1)):
                    answer += 1
    
    print(answer)
                

main()