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
    
    
    quad = [0,0,0,0]
    for robot in matrix:
        px = robot['px']
        py = robot['py']
        vx = robot['vx']
        vy = robot['vy']

        for _ in range(100):
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
        
        if px < width // 2 and py < length // 2:
            quad[0] += 1
        elif px-1 >= width // 2 and py < length // 2:
            quad[1] += 1
        elif px < width // 2 and py-1 >= length // 2:
            quad[2] += 1
        elif px-1 >= width // 2 and py-1 >= length // 2:
            quad[3] += 1
    
    answer = 1
    for ele in quad:
        answer*= ele
    
    print(answer)
    
    

main()