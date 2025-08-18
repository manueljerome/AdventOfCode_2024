
def main():
    import re
    with open(r"C:\Users\Emmanuel\Documents\PythonCode\AdventOfCode_2024\Source\AOC24_DayThree\puzzle_input.txt", "r", encoding = "utf-8") as file_input:
        puzzle_list = file_input.read()
        start = 0
        sum = 0
        pattern = r"mul\(\d+,\d+\)" 
        correct_occurences = list[str](re.findall(pattern, puzzle_list))
        for i in range(len(correct_occurences)): 
            x = re.sub(r"mul\(", "", correct_occurences[i])
            x = x.replace(")", "")
            correct_occurences[i] = x
            
        for i in range(len(correct_occurences)):
            x = correct_occurences[i].split(",")
            correct_occurences[i] = x
            sum += int(correct_occurences[i][0]) * int(correct_occurences[i][1])

        print(sum)






if __name__ == "__main__":
    main()