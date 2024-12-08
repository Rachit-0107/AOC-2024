import re 

def main():
    with open('input.txt', 'r') as file:
        file_content = file.read()
    
    pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    matches = re.findall(pattern, file_content)

    result = []
    for match in matches:
        if match.startswith("mul"):
            nums = re.findall(r"\d{1,3}", match)
            result.append((nums[0], nums[1]))
        else:
            result.append(match)

    flag = True
    answer = 0
    for element in result:
        if element == "do()":
            flag = True
        elif element == "don't()":
            flag = False
        elif flag:
            answer+= (int(element[0]) * int(element[1]))
    
    print(answer)

main()