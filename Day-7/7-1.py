from itertools import product

def main():
    matrix = []

    with open("input.txt", 'r') as file:
        for line in file:
            first_number, numbers = line.strip().split(':')
            row = [int(first_number)] + list(map(int, numbers.split()))
            matrix.append(row)

    answer = 0
    for row in matrix:
        n = len(row) - 1
        combinations = list(product(["+", "*"], repeat=n-1))
        for operators in combinations:
            result = row[1]
            for i, op in enumerate(operators):
                if op == '+':
                    result += row[i+2]
                elif op == '*':
                    result *= row[i+2]
            if result == row[0]:
                answer += row[0]
                break
    
    print(answer)


main()