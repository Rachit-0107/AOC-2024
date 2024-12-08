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

def tolerance(row):
    # print(row)
    for i in range(len(row)):
        modified_list = row[:i] + row[i + 1:]
        # print(modified_list)
        ascending = inc_safe(modified_list)
        descending = dec_safe(modified_list)
        if ascending or descending:
            return True
    return False

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
        elif not ascending and not descending:
            # print("else")
            valid = tolerance(row)
            if valid:
                answer+=1

    print(answer)

main()