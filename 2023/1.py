def read_input() -> list[str]:
    with open('./1.txt') as f:
        lines = f.readlines()
    return lines

def process_line(line: str) -> int:
    """Process a line of input and return the concatenated first and last number (min, max)"""

    first: str | None = None
    last: str | None = None

    for char in line:
        if char.isdigit():
            if first is None:
                first = char
            else:
                last = char

    if first is None:
        first = "0"

    if last is None:
        last = first

    return int(first + last)

def main():
    return sum(process_line(line) for line in read_input())

if __name__ == '__main__':
    print(main())
