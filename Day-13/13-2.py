import re
import numpy
import math

def main():
    matrix = []
    with open("input.txt", "r") as file:
        for line in file:
            numbers = re.findall(r"\d+", line)
            if numbers:
                matrix.append([int(num) for num in numbers])
    
    pressA = 0
    pressB = 0
    add = 10000000000000
    i = 0
    while i+2 < len(matrix):
        x1 = matrix[i][0]
        x2 = matrix[i+1][0]
        y1 = matrix[i][1]
        y2 = matrix[i+1][1]
        coeff = numpy.array([[matrix[i][0], matrix[i+1][0]], [matrix[i][1], matrix[i+1][1]]])
        const = numpy.array([add + matrix[i+2][0], add + matrix[i+2][1]])
        solution = numpy.linalg.solve(coeff, const)
        a = math.floor(solution[0])
        b = math.floor(solution[1])
        if x1*a + x2*b == add + matrix[i+2][0] and y1*a + y2*b == add + matrix[i+2][1]:
            pressA += a
            pressB += b
        elif x1*(a+1) + x2*b == add + matrix[i+2][0] and y1*(a+1) + y2*b == add + matrix[i+2][1]:
            pressA += (a+1)
            pressB += b
        elif x1*a + x2*(b+1) == add + matrix[i+2][0] and y1*a + y2*(b+1) == add + matrix[i+2][1]:
            pressA += a
            pressB += (b+1)
        elif x1*(a+1) + x2*(b+1) == add + matrix[i+2][0] and y1*(a+1) + y2*(b+1) == add + matrix[i+2][1]:
            pressA += (a+1)
            pressB += (b+1)
        i+=3
    
    answer = 3*pressA + pressB
    print(answer)   

main()