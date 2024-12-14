import re

def main():
    matrix = []
    with open("input.txt", "r") as file:
        for line in file:
            numbers = re.findall(r"\d+", line)
            if numbers:
                matrix.append([int(num) for num in numbers])

    pressA = 0
    pressB = 0
    i = 0
    while(i + 2 < len(matrix)):
        for a in range(100):
            for b in range(100):
                if matrix[i][0]*a + matrix[i+1][0]*b == matrix[i+2][0] and matrix[i][1]*a + matrix[i+1][1]*b == matrix[i+2][1]:
                    print(matrix[i+2][0], matrix[i+2][1])
                    print(a, b)
                    pressA+=int(a)
                    pressB+=int(b)
                    break
        i+=3
    
    answer = 3*pressA + pressB
    print(answer)

main()