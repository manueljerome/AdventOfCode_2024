
from pathlib import Path
from hashlib import md5

WORD = "XMAS"
DIRS = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]

p = Path(r"C:\Users\Emmanuel\Documents\PythonCode\AdventOfCode_2024\Source\AOC24_DayFour\puzzle_input.txt")
grid = p.read_text().splitlines()
R, C = len(grid), len(grid[0])

def inb(r,c): return 0 <= r < R and 0 <= c < C

def count_all():
    """
    Using a grid to count all occurrences of 'XMAS' across all 8 directions E, W, N, S, SE, NE, SW, NW
    """
    total = 0
    per_dir = [0]*8
    coords = []
    for r in range(R):
        for c in range(C):
            if grid[r][c] != 'X': continue
            for d,(dr,dc) in enumerate(DIRS):
                rr, cc = r, c
                ok = True
                for ch in WORD[1:]:
                    rr += dr; cc += dc
                    if not inb(rr,cc) or grid[rr][cc] != ch:
                        ok = False; 
                        break
                if ok:
                    total += 1
                    
    
    print(total)
    return total


def main():
    count_all()

if (__name__ == "__main__"):
    main()