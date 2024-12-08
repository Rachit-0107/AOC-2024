def main():
    with(open('input.txt', 'r')) as file:
        odd_index_list = []
        even_index_list = []
        for line in file:
            left, right = line.split()
            odd_index_list.append(int(left))
            even_index_list.append(int(right))
    odd_index_list.sort()
    even_index_list.sort()

    answer = 0

    for i in range(len(odd_index_list)):
        answer += abs(odd_index_list[i] - even_index_list[i])

    print(answer)

main()
