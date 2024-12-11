def main():
    with(open('input.txt', 'r')) as file:
        input = file.read().strip()
    
    processed_input = []
    id = 0

    for index, char in enumerate(input):
        num = int(char)
        if index % 2 == 0:
            processed_input.append([id, num])
            id+=1
        else:
            processed_input.append([-1, num])

    j = id-1

    compact_input = []

    while j>=0:
        idj = len(processed_input)-1
        idi = 0
        while idi < len(processed_input):
            if processed_input[idi][0] == -1 and processed_input[idi][1] > 0:
                break
            else:
                idi+=1

        while idj >= 0:
            if processed_input[idj][0] == j and processed_input[idj][1] > 0:
                break
            else:
                idj-=1

        if idi >= idj:
            j-=1
            continue
        while idi < idj:
            if processed_input[idi][0] == -1 and processed_input[idi][1] >= processed_input[idj][1]:
                    processed_input[idi][1] -= processed_input[idj][1]
                    processed_input[idj][0] = -1
                    processed_input.insert(idi, [j, processed_input[idj][1]])
                    j-=1
                    break
            else:
                idi+=1
        if(idi == idj):
            j-=1

    for row in processed_input:
        for i in range(row[1]):
            compact_input.append(row[0])

    answer = 0
    for i in range(len(compact_input)):
        if(compact_input[i] == -1):
            continue
        answer += (i * compact_input[i])
    print(answer)

main()