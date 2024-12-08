

def main():
    with open('rules.txt', 'r') as file:
        rules = [line.strip().split('|') for line in file]

    rules = [[int(value) for value in row] for row in rules]

    with open('input.txt', 'r') as file:
        matrix = [line.strip().split(',') for line in file]

    matrix = [[int(value) for value in row] for row in matrix]

    correct_matix = []

    for row in matrix:
        flag = True
        for rule in rules:
            if rule[0] in row and rule[1] in row:
                if row.index(rule[0]) > row.index(rule[1]):
                    flag = False
                    continue
        if flag:
            correct_matix.append(row)

    answer = 0
    for row in correct_matix:
        answer+= row[len(row) // 2]
    
    print(answer)
        


main()