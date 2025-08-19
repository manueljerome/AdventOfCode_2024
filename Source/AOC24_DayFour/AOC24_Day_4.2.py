from pathlib import Path

DIRS = [(-1,-1),(-1,1),(1,-1),(1,1)]


p = Path(r"C:\Users\Emmanuel\Documents\PythonCode\AdventOfCode_2024\Source\AOC24_DayFour\puzzle_input.txt")
grid = p.read_text().splitlines()
R, C = len(grid), len(grid[0])

def inb(r,c): return 0 <= r < R and 0 <= c < C

def count_all():
    """
    Using a grid to count all occurrences of 'X - MAS' one step across each diagonal
    """
    total = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] != 'A': continue
            ok = True
            LETTERS = {"M", "S"}
            for dr,dc in DIRS:
                rp, cp = r + dr, c + dc #+ve diagonal cell
                rn, cn = r - dr, c - dc #-ve diagonal cell

                #if positive and negative diagonal cells are not within bounds, break loop
                if not inb(rp , cp) or not inb(rn , cn): ok = False; break 

                #if the cells are not equal to "M" or "S" ,break
                if grid[rp][cp] not in LETTERS or grid[rn][cn] not in LETTERS: ok = False; break 

                #if we have identical characters in the diagonal cells, break
                if grid[rp][cp] == grid[rn][cn]: ok = False; break 
                
            if ok:
                total += 1
    return total


def main():
    print(count_all())

if (__name__ == "__main__"):
    main()