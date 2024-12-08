from collections import defaultdict, deque

def sort_with_rules(row, rules):
    graph = defaultdict(list)
    in_degree = {page:0 for page in row}
    for rule in rules:
        if rule[0] in row and rule[1] in row:
            graph[rule[0]].append(rule[1])
            in_degree[rule[1]] = in_degree.get(rule[1], 0) + 1

    queue = deque([node for node in in_degree if in_degree[node] == 0])
    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
                
    if len(topo_order) != len(in_degree):
        raise ValueError("Cycle detected in rules; sorting not possible.")

    order_index = {num: i for i, num in enumerate(topo_order)}
    row.sort(key=lambda x: order_index.get(x, float('inf')))

    return row


def main():
    with open('rules.txt', 'r') as file:
        rules = [line.strip().split('|') for line in file]

    rules = [[int(value) for value in row] for row in rules]

    with open('input.txt', 'r') as file:
        matrix = [line.strip().split(',') for line in file]

    matrix = [[int(value) for value in row] for row in matrix]

    incorrect_matrix = []

    for row in matrix:
        flag = True
        for rule in rules:
            if rule[0] in row and rule[1] in row:
                if row.index(rule[0]) > row.index(rule[1]):
                    flag = False
                    continue
        if not flag:
            incorrect_matrix.append(row)

    answer = 0
    for row in incorrect_matrix:
        sorted_row = sort_with_rules(row, rules)
        answer+= sorted_row[len(sorted_row) // 2]
    
    print(answer)
        


main()