from typing import Final
import re
from pathlib import Path

#Final is not really necessary here since it's just my code, using it for muscle memory for when I work on production code. also, compiling regex for performance boost when calling multiple times(also for muscle memory)
PATTERN: Final[re.Pattern[str]] = re.compile(r"mul\((\d+),(\d+)\)")
def main() -> int:
    """
    Sum products of mul(a,b) instructions,
    ignoring sections between don't() and do().
    """
    
    
    p = Path(r"C:\Users\Emmanuel\Documents\PythonCode\AdventOfCode_2024\Source\AOC24_DayThree\puzzle_input.txt")
    puzzle_list = p.read_text(encoding = "utf-8")
    
    # Remove disabled chunks across newlines; stop at nearest do()
    clean_puzzle  = re.sub(r"don't\(\).*?do\(\)", "", puzzle_list , flags = re.S)

    # Then remove any dangling final don't() <EOF>
    clean_puzzle = re.sub(r"don't\(\).*", "", clean_puzzle, flags = re.S)
    
    total = sum(int(a.group(1)) * int(a.group(2)) for a in PATTERN.finditer(clean_puzzle))
    print(total)
    return total
        






if __name__ == "__main__":
    main()