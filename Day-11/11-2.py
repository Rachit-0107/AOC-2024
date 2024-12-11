from collections import defaultdict

def main():
    with(open('input.txt', 'r')) as file:
        for line in file:
            input = line.strip().split()
    
    counts = defaultdict(int)

    for ele in input:
        counts[int(ele)] += 1

    for i in range(75):
        new_counts = defaultdict(int)
        print(counts)
        for key, value in counts.items():
            if int(key) == 0:
                new_counts[1] += value
            elif len(str(key))%2 == 0:
                mid = len(str(key)) // 2
                part1 = int(str(key)[:mid])
                part2 = int(str(key)[mid:])
                new_counts[part1] += value
                new_counts[part2] += value
            else:
                new_counts[str(int(key)*2024)] += value
        counts = new_counts

    print(sum(counts.values()))


main()