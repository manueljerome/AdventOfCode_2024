from pathlib import Path

"""
OBJECTIVES

1: To get the printers going as soon as possible, start by identifying which updates are already in the right order.
2: collect the middle number of each incorrectly-ordered update
3: add up all the middle page numbers
"""
def main():
    updates_path = Path(r"C:\Users\Emmanuel\Documents\PythonCode\AdventOfCode_2024\Source\AOC24_DayFive\puzzle_input.txt")
    rules_path = Path(r"C:\Users\Emmanuel\Documents\PythonCode\AdventOfCode_2024\Source\AOC24_DayFive\page_ordering_rules.txt")
    grouped_updates = parse_rules(rules_path)
    ordered_updates = fix_misordered_updates(grouped_updates, updates_path)
    sum_of_middle_numbers = get_sum_of_middle_numbers(ordered_updates)
    print(sum_of_middle_numbers)


from collections import deque

def fix_misordered_updates(successors: dict[str, set[str]], update_path: Path) -> list[list[str]]:
    """
    Reorder updates using topological sort.

    For each update, build the subgraph of ordering rules relevant to the pages 
    in that update and apply Kahn's algorithm to produce a valid sequence.Pages 
    are ordered so that all constraints X|Y (X must appear before Y) are satisfied. 
    Ties between unconstrained pages are broken using their original left-to-right 
    order to keep the result stable.

    Returns only the updates that were misordered and had to be corrected.
    """

    fixed = []
    lines = update_path.read_text(encoding="utf-8").splitlines()
    updates = [[t.strip() for t in ln.split(",")] for ln in lines if ln.strip()]

    for original in updates:
        nodes = set(original)
        indeg = {n: 0 for n in nodes}
        adj = {n: set() for n in nodes}
        for u in nodes:
            for v in successors.get(u, ()):
                if v in nodes and v not in adj[u]:
                    adj[u].add(v); indeg[v] += 1

        order_idx = {p: i for i, p in enumerate(original)}
        q = sorted([n for n in nodes if indeg[n] == 0], key=order_idx.get)
        result, dq = [], deque(q)
        while dq:
            u = dq.popleft()
            result.append(u)
            for v in sorted(adj[u], key=order_idx.get):
                indeg[v] -= 1
                if indeg[v] == 0:
                    dq.append(v)

        if len(result) != len(original):
            raise ValueError("Cycle in rules; cannot reorder.")
        if result != original:
            fixed.append(result)
    return fixed

               
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


#First Iteration of fix_misordered_updates
#
# def fix_misordered_updates(_grouped_updates: dict[str:list[str]], update_path: Path) -> list[list[str]]:
#     """
#     Read updates from file and reorder any that violate the rules.
#     Returns only the updates that were corrected.
#     """
#     validated_updates = []
#     update_list = update_path.read_text(encoding = "utf-8").splitlines()
#     update_list = [[t.strip() for t in r.split(",")] for r in update_list]
    
#     for update in update_list:
#         ok = True
        
#         for page_idx in range(len(update)): 
#             for i in range(len(update)):
#                 if i == page_idx : continue

#                 next_page = update[i]
#                 successors_list = _grouped_updates.get(update[page_idx], [])

#                 if ((next_page in successors_list and i > page_idx) or next_page not in successors_list and i < page_idx):
#                     continue
#                 b_pg_index = update.index(update[i])
#                 a_pg_index = update.index(update[page_idx])

#                 if(next_page in successors_list and i < page_idx):   
#                     ok = False
#                     before = update.pop(a_pg_index)
#                     update.insert(b_pg_index, before )

#                 if(next_page not in successors_list and i > page_idx):
#                     ok = False
#                     before = update.pop(b_pg_index)
#                     update.insert(a_pg_index, before)
                    
#         if ok == False:
#             validated_updates.append(update)
#     return validated_updates