def main():
    with open(r"C:\Users\Emmanuel\Documents\PythonCode\AdventOfCode_2024\Source\AOC24_DayTwo\puzzle_input.txt", "r", encoding="utf-8") as puzzle_input:
        number_of_safe_reports = 0
        while True:
            puzzle_list = puzzle_input.readline()
            if not puzzle_list:
                break
            puzzle_list = list(map(int, puzzle_list.strip().split()))
            #print(puzzle_list)
            if(check_safety(puzzle_list)):
                number_of_safe_reports += 1
            else:
                print(puzzle_list)
                for i in range(len(puzzle_list)): #for all the elements of this list in range of the length of the list minus one
                    print(i)
                    new_list = remove_copy_list_item(i, puzzle_list.copy()) #new list is equal to the new list after removing the element at the index 'i'
                    if check_safety(new_list): 
                        number_of_safe_reports += 1
                        break
                    
        print(number_of_safe_reports)

def check_safety(puzzle_list=None):
    """
    Check that puzzle list adheres to the rules: adjacent integer mst differ by 1, 2 or 3
    """
    levels = puzzle_list
    if (levels == sorted(levels) or levels == sorted(list(map(int, levels)), reverse=True)):
        previous_int = int(puzzle_list[0])
        if any(i == 0 for i in puzzle_list):
            return False
        for i in range(1, len(puzzle_list)):
            if( abs(int(puzzle_list[i]) - previous_int) > 3 or  abs(int(puzzle_list[i]) - previous_int) < 1):
                return False
            previous_int = int(puzzle_list[i])
        print(puzzle_list)
        return True

def remove_copy_list_item(index: int, unsafeList: list[int]) -> list[int]:
    """
    Remove duplicate value or value that might lead to unsafe condition from list
    """

    copy_list = unsafeList #assign the list sent to a copy
    copy_list.pop(index)#remove the element at this index
    return copy_list#return the new list

if __name__ == "__main__":
    main()