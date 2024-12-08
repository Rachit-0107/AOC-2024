# answer - 1443

def main():
    with open('input.txt', 'r') as file:
        matrix = [list(line.strip()) for line in file.readlines()]
    
    i = 0
    j = 0
    for row_idx, row in enumerate(matrix):
        for col_idx, cell in enumerate(row):
            if cell == '^':
                i = row_idx
                j = col_idx
                break
    
    answer = 0

    while not (i < 0 and i> len(matrix) and j < 0 and j > len(matrix[0])):
        if i == 0 or i == len(matrix)-1 or j == 0 or j == len(matrix[0])-1:
            break
        if matrix[i][j] == '^':
            if i-1 >= 0 and matrix[i-1][j] != '#':
                if(matrix[i-1][j] != '^' and matrix[i-1][j] != 'v' and matrix[i-1][j] != '<' and matrix[i-1][j] != '>'):
                    answer += 1
                matrix[i-1][j] = '^'
                i -= 1
            elif j+1 < len(matrix[0]) and matrix[i][j+1] != '#':
                if(matrix[i][j+1] != '^' and matrix[i][j+1] != 'v' and matrix[i][j+1] != '<' and matrix[i][j+1] != '>'):
                    answer += 1
                matrix[i][j+1] = '>'
                j += 1
            elif i+1 < len(matrix) and matrix[i+1][j] != '#':
                if(matrix[i+1][j] != '^' and matrix[i+1][j] != 'v' and matrix[i+1][j] != '<' and matrix[i+1][j] != '>'):
                    answer += 1
                matrix[i+1][j] = 'v'
                i += 1
            elif j-1 >= 0 and matrix[i][j-1] != '#':
                if(matrix[i][j-1] != '^' and matrix[i][j-1] != 'v' and matrix[i][j-1] != '<' and matrix[i][j-1] != '>'):
                    answer += 1
                matrix[i][j-1] = '<'
                j -= 1
            else:
                break
        elif matrix[i][j] == '>':
            if j+1 < len(matrix[0]) and matrix[i][j+1] != '#':
                if(matrix[i][j+1] != '^' and matrix[i][j+1] != 'v' and matrix[i][j+1] != '<' and matrix[i][j+1] != '>'):
                    answer += 1
                j += 1
                matrix[i][j] = '>'
            elif i+1 < len(matrix) and matrix[i+1][j] != '#':
                if(matrix[i+1][j] != '^' and matrix[i+1][j] != 'v' and matrix[i+1][j] != '<' and matrix[i+1][j] != '>'):
                    answer += 1
                i += 1
                matrix[i][j] = 'v'
            elif j-1 >= 0 and matrix[i][j-1] != '#':
                if(matrix[i][j-1] != '^' and matrix[i][j-1] != 'v' and matrix[i][j-1] != '<' and matrix[i][j-1] != '>'):
                    answer += 1
                j -= 1
                matrix[i][j] = '<'
            elif i-1 >= 0 and matrix[i-1][j] != '#':
                if(matrix[i-1][j] != '^' and matrix[i-1][j] != 'v' and matrix[i-1][j] != '<' and matrix[i-1][j] != '>'):
                    answer += 1
                i -= 1
                matrix[i][j] = '^'
            else:
                break
        elif matrix[i][j] == 'v':
            if i+1 < len(matrix) and matrix[i+1][j] != '#':
                if(matrix[i+1][j] != '^' and matrix[i+1][j] != 'v' and matrix[i+1][j] != '<' and matrix[i+1][j] != '>'):
                    answer += 1
                i += 1
                matrix[i][j] = 'v'
            elif j-1 >= 0 and matrix[i][j-1] != '#':
                if(matrix[i][j-1] != '^' and matrix[i][j-1] != 'v' and matrix[i][j-1] != '<' and matrix[i][j-1] != '>'):
                    answer += 1
                j -= 1
                matrix[i][j] = '<'
            elif i-1 >= 0 and matrix[i-1][j] != '#':
                if(matrix[i-1][j] != '^' and matrix[i-1][j] != 'v' and matrix[i-1][j] != '<' and matrix[i-1][j] != '>'):
                    answer += 1
                i -= 1
                matrix[i][j] = '^'
            elif j+1 < len(matrix[0]) and matrix[i][j+1] != '#':
                if(matrix[i][j+1] != '^' and matrix[i][j+1] != 'v' and matrix[i][j+1] != '<' and matrix[i][j+1] != '>'):
                    answer += 1
                j += 1
                matrix[i][j] = '>'
            else:
                break
        elif matrix[i][j] == '<':
            if j-1 >= 0 and matrix[i][j-1] != '#':
                if(matrix[i][j-1] != '^' and matrix[i][j-1] != 'v' and matrix[i][j-1] != '<' and matrix[i][j-1] != '>'):
                    answer += 1
                j -= 1
                matrix[i][j] = '<'
            elif i-1 >= 0 and matrix[i-1][j] != '#':
                if(matrix[i-1][j] != '^' and matrix[i-1][j] != 'v' and matrix[i-1][j] != '<' and matrix[i-1][j] != '>'):
                    answer += 1
                i -= 1
                matrix[i][j] = '^'
            elif j+1 < len(matrix[0]) and matrix[i][j+1] != '#':
                if(matrix[i][j+1] != '^' and matrix[i][j+1] != 'v' and matrix[i][j+1] != '<' and matrix[i][j+1] != '>'):
                    answer += 1
                j += 1
                matrix[i][j] = '>'
            elif i+1 < len(matrix) and matrix[i+1][j] != '#':
                if(matrix[i+1][j] != '^' and matrix[i+1][j] != 'v' and matrix[i+1][j] != '<' and matrix[i+1][j] != '>'):
                    answer += 1
                i += 1
                matrix[i][j] = 'v'
            else:
                break

    print(answer)


main()