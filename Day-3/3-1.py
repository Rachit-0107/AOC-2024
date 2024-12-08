import re 

def main():
    with open('input.txt', 'r') as file:
        file_content = file.read()
    
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, file_content)
    total_sum = sum(int(a) * int(b) for a, b in matches)

    print(total_sum)


main()