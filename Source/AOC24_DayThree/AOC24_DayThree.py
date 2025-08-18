from pathlib import Path
from typing import Final
import re

# Precompile the regex pattern for efficiency and clarity.
# This regex matches "mul(X,Y)" where X and Y are integers without spaces.
#Final is not really necessary here since it's just my code, using it for muscle memory for when I work on production code. also, compiling regex for performance boost when calling multiple times(also for muscle memory)
PATTERN: Final[re.Pattern[str]] = re.compile(r"mul\((\d+),(\d+)\)")

def main() -> int:
    """
    Reads the puzzle input file, finds all valid mul(X,Y) instructions,
    multiplies each pair, and sums the results.
    
    """
    # Path to the puzzle input file
    p = Path(
        r"C:\Users\Emmanuel\Documents\PythonCode\AdventOfCode_2024\Source\AOC24_DayThree\puzzle_input.txt"
    )
    
    # Read the entire file content into a single string.
    puzzle_list = p.read_text(encoding="utf-8")

    # Use finditer() to lazily iterate through all regex matches.
    # Convert groups to int, multiply them, and sum across all matches.
    total = sum(int(m.group(1)) * int(m.group(2)) for m in PATTERN.finditer(puzzle_list))
    print(total)
    return total



if __name__ == "__main__":
    main()
