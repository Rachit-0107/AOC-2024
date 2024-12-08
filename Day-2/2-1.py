def inc_safe(row):
    for i in range(len(row) - 1):
        if row[i] >= row[i + 1] or (row[i + 1] - row[i] > 3):
            return False
    return True

def dec_safe(row):
    for i in range(len(row) - 1):
        if row[i] <= row[i + 1] or (row[i] - row[i+1] > 3):
            return False
    return True

def main():
    matrix = []
    answer = 0
    with open('input.txt', 'r') as file:
        for line in file:
            matrix.append([int(num) for num in line.split()])

    for row in matrix:
        ascending = inc_safe(row)
        descending = dec_safe(row)
        if ascending or descending:
            answer+=1

    print(answer)

main()