
def main():
    with open(r"C:\Users\Emmanuel\Documents\PythonCode\AdventOfCode\puzzle.txt", "r", encoding="utf-8" ) as puzzle_input:
        first_list = []
        second_list = []
        while True:
            puzzle = puzzle_input.readline()
            if not puzzle:
                break
            puzzle = puzzle.strip()
            first_list.append(int(puzzle.split()[0]))
            second_list.append(int(puzzle.split()[1]))
        similarity_list = []
        for i in range(0, len(first_list)):
            multiplier = 0
            for j in second_list:
                if (first_list[i] == j):
                    multiplier += 1
            print(multiplier)
            similarity_list.append(multiplier * first_list[i])
        similarity_score = sum(similarity_list)
        print(similarity_score)

        

if __name__ == '__main__':
    main()