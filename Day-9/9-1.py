def main():
    with(open('input.txt', 'r')) as file:
        input = file.read().strip()
    
    processed_input = []
    id = 0

    for index, char in enumerate(input):
        num = int(char)
        if index % 2 == 0:
            for i in range(num):
                processed_input.append(id)
            id+=1
        else:
            for i in range(num):
                processed_input.append(-1)
    
    i = 0
    j = len(processed_input)-1

    compact_input = []

    while i <= j:
        if processed_input[i] == -1:
            if processed_input[j] == -1:
                j-=1
            else:
                compact_input.append(processed_input[j])
                j-=1
                i+=1
        else:
            compact_input.append(processed_input[i])
            i+=1

    answer = 0

    for i in range(len(compact_input)):
        answer += (i * compact_input[i])
    print(answer)

main()