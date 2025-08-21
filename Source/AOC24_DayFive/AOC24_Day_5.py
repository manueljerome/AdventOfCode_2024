from pathlib import Path

"""
OBJECTIVES

1: To get the printers going as soon as possible, start by identifying which updates are already in the right order.
2: collect the middle number of each correctly-ordered update
3: add up all the middle page numbers
"""
def main():
    updates_path = Path(r"C:\Users\Emmanuel\Documents\PythonCode\AdventOfCode_2024\Source\AOC24_DayFive\puzzle_input.txt")
    rules_path = Path(r"C:\Users\Emmanuel\Documents\PythonCode\AdventOfCode_2024\Source\AOC24_DayFive\page_ordering_rules.txt")
    grouped_updates = parse_rules(rules_path)
    ordered_updates = filter_valid_updates(grouped_updates, updates_path)
    sum_of_middle_numbers = get_sum_of_middle_numbers(ordered_updates)
    print(sum_of_middle_numbers)



from typing import Dict, List, Set

def filter_valid_updates(successors: Dict[str, Set[str]], update_path: Path) -> List[List[str]]:
    """
    Load updates from file and keep only those that satisfy the ordering rules.

    For each update (a comma-separated line of page IDs), build a position map and
    verify that for every rule X|Y (X must come before Y) where both X and Y appear
    in the update, we have pos[X] < pos[Y]. Returns the list of valid updates.
    """
    valid_updates: List[List[str]] = []

    # Read and tokenize, trimming whitespace; ignore blank lines
    raw_lines = update_path.read_text(encoding="utf-8").splitlines()
    updates = [[tok.strip() for tok in line.split(",")] for line in raw_lines if line.strip()]

    for update in updates:
        pos = {page: idx for idx, page in enumerate(update)}
        is_valid = True

        # Check all constrained pairs that appear in this update
        for x in (p for p in update if p in successors):
            for y in successors[x]:
                if y in pos and pos[x] > pos[y]:
                    is_valid = False
                    break
            if not is_valid:
                break


        if is_valid:
            valid_updates.append(update)

    return valid_updates


def parse_rules(rules_path: Path) -> dict[str, list[str]]:
    """
    Read page-ordering rules from a file and build a successor map.

    Each line in the file has the form "A|B" meaning page A must appear before page B.
    Returns a dict mapping each page to a set of its required successors.
    """
    successors: dict[str, list[str]] = {}
    for lines in rules_path.read_text(encoding = "utf-8").splitlines():
        line = lines.strip()
        if not line: continue

        a,b = line.split("|")
        successors.setdefault(a, []).append(b)
    return successors
    
def get_sum_of_middle_numbers(ordered_list: list[list[str]]) -> int:

    """
    Compute the sum of each update's middle page number.
    Assumes each update has odd length. Converts the middle token to int and sums them.
    """
    total = 0
    for i in ordered_list:
        middle_num_index = int(len(i) // 2) 
        total += int(i[middle_num_index])
    return total



if __name__ == "__main__":
    main()

#First Iteration of filter_valid_updates
#
# def filter_valid_updates(_grouped_updates: dict[str:list[str]], update_path: Path) -> list[list[str]]:
#     """
#     Load updates from file and keep only those that satisfy the ordering rules.

#     For each update (comma-separated page IDs on a line), we verify that
#     for every constrained pair (X -> Y) present in the update, X appears
#     at a lower index than Y. Returns a list of valid updates (lists of page IDs).
#     """
#     valid_updates = []
#     update_list = update_path.read_text(encoding = "utf-8").splitlines()
#     update_list = [r.split(",") for r in update_list]

#     for update in update_list:
#         ok = True
        
#         for page_idx in range(len(update)): 
#             for i in range(len(update)):
#                 if i == page_idx : continue

#                 next_page = update[i]
#                 successors_list = _grouped_updates.get(update[page_idx], [])

#                 if ((next_page not in successors_list and i > page_idx) or next_page in successors_list and i < page_idx): ok = False
#         if ok == True:
#             valid_updates.append(update)
#     return valid_updates