import re


def main():
    width = 101
    length = 103
    matrix = []
    with open('input.txt', 'r') as file:
        for line in file:
            numbers = [int(num) for num in re.findall(r'-?\d+', line)]
            initial = dict(px = int(numbers[0]), py = int(numbers[1]), vx = int(numbers[2]), vy = int(numbers[3]))
            matrix.append(initial)
    
    seconds = 0
    while True:
        seconds+=1
        final = []
        for robot in matrix:
            px = robot['px']
            py = robot['py']
            vx = robot['vx']
            vy = robot['vy']

            px += vx
            if px < 0:
                px+= width
            if px > width:
                px-=width
            py += vy
            if py < 0:
                py+= (length)
            if py > length:
                py-= length
            
            px = px % width
            py = py % length

            robot['px'] = px
            robot['py'] = py
            final.append((px, py))
        
        unique = list(set(final))
        if len(unique) == len(matrix):
            print(seconds)
            break
    
    tree = []
    for _ in range(length):
        row = []
        for _ in range(width):
            row.append(0)
        tree.append(row)
    
    for robot in matrix:
        px = robot['px']
        py = robot['py']
        tree[py][px] = 1
    
    for row in tree:
        line = ''.join(map(str, row))
        print(line)

main()