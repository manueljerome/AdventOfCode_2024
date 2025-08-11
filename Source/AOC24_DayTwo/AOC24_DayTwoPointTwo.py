
#"C:\Users\Emmanuel\Documents\PythonCode\AdventOfCode_2024\Source\AOC24_DayTwo\puzzle_input.txt"
#"/home/tarantula/Documents/AdventOfCodeRepo/AdventOfCode_2024/Source/AOC24_DayTwo/puzzle_input.txt
def main():
    with open(r"C:\Users\Emmanuel\Documents\PythonCode\AdventOfCode_2024\Source\AOC24_DayTwo\puzzle_input.txt", "r", encoding="utf-8") as puzzle_input:
        number_of_safe_reports = 0
        while True:
            puzzle_list = puzzle_input.readline()
            if not puzzle_list:
                break
            puzzle_list = puzzle_list.strip().split()
            #print(puzzle_list)
            is_safe = check_safety(puzzle_list)
            if(is_safe == True):
                number_of_safe_reports += 1
        print(number_of_safe_reports)

def check_safety(puzzle_list: list[str]) -> bool:
    """
    """
    levels = list(map(int, puzzle_list))
    safety_count = 0
    safety_count_max =1
    if (levels == sorted(levels) or levels == sorted(levels, reverse=True)):
        duplicates = find_duplicates(levels)
        if len(duplicates) == 0:
            if(check_sorted_list_is_safe(levels)):
                #print (levels)
                #print("needs no modification")
                return True
            else:
                for i in range(len(levels)):
                    result = remove_copy_list_item(i, levels)
                    if(check_sorted_list_is_safe(result)):
                        #print(levels)
                        #print("removing an item makes it safe")
                        return True
                    else: return False
        else:
            for i in range(len(levels)):
                    result = remove_copy_list_item(i, levels)
                    if(check_sorted_list_is_safe(result)):
                        #print(levels)
                        #print("duplicated but is safe after removing one level")
                        return True
                    else: return False
    else:
        return False

        
 
def remove_copy_list_item(index: int, unsafeList: list[int]) -> list[int]:
    """
    Remove duplicate value or value that might lead to unsafe condition from list
    """

    copy_list = unsafeList
    copy_list.pop(index)
    return copy_list

def find_duplicates(input_list: list[int]) -> dict[int, int]:
    """
    find out if list contains duplicate of a value and return the integer that's duplicated alongside its duplicate indexes
    """
    duplicate_dict = {}
    for i in range((len(input_list))):
        _count = 0
        #if(not input_list[i + 1]):   break
        for j in range(len(input_list)):
            if(input_list[i] == input_list[j]):
                _count += 1
                
        
        if (_count > 1):   
            entry = {input_list[i] : _count}
            duplicate_dict.update(entry)  
            print(input_list)
            #print(entry)
    
     
    return duplicate_dict
        
def check_sorted_list_is_safe(puzzle_list: list[int]) -> bool:
    """
    """
    previous_int = puzzle_list[0]
    if any(i == 0 for i in puzzle_list):
        return False
    
    for i in range(1, len(puzzle_list)):
            if(abs(int(puzzle_list[i]) - previous_int) > 3 or  abs(int(puzzle_list[i]) - previous_int) < 1):
                return False
            previous_int = puzzle_list[i]
    return True



if __name__ == "__main__":
    main()