def main():
    with(open('input.txt', 'r')) as file:
        for line in file:
            input = line.strip().split()
    
    for i in range(25):
        temp = []
        for j in range(len(input)):
            if int(input[j]) == 0:
                temp.append('1')
            elif len(input[j])%2 == 0:
                mid = len(input[j]) // 2
                part1 = str(int(input[j][:mid]))
                part2 = str(int(input[j][mid:]))
                temp.append(part1)
                temp.append(part2)
            else:
                temp.append(str(int(input[j])*2024))
        input = []
        input.extend(temp)

    print(len(input))


main()