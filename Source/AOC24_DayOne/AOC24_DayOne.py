def main():
    try:
        with open(r"C:\Users\Emmanuel\Documents\PythonCode\AdventOfCode\puzzle.txt", "r", encoding="utf-8") as puzzle:
            first_list = []
            second_list = []
            while True:
                puzzle_input = puzzle.readline()
                if not puzzle_input:
                    break
                puzzle_input = puzzle_input.strip()
                first_list.append(puzzle_input.split()[0])
                second_list.append(puzzle_input.split()[1])
            second_list.sort()   
            first_list.sort() 
            total_difference = 0

            total_difference = sum(abs(int(a) - int(b))for a, b in zip(first_list, second_list))
            print(total_difference)
            


            

    except:
        print("Not Found")

    


if __name__ == '__main__':
    main()