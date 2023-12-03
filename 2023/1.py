import re

def read_input(filename: str) -> list[str]:
    with open(filename) as f:
        lines = f.readlines()
    return lines


# Still not working :(
# NOTE: one way of debugging may be to remove all lines that does not contain letter numbers
def sanitize_line(line: str) -> str:
    replace_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    "EDGE TEST CASE onefxtprsml8fqptvmfthreesix2jbeightwor 12"

    # Find and replace first left match
    matches = re.findall(r"one|two|three|four|five|six|seven|eight|nine", line)
    if len(matches) > 0:
        line = line.replace(matches[0], replace_map[matches[0]])


    # Find and replace first right match
    reverse_line = line[::-1]
    matches = re.findall(r"enin|thgie|neves|xis|evif|ruof|eerht|owt|eno", reverse_line)
    if len(matches) > 0:
        reverse_line = reverse_line.replace(matches[0], replace_map[matches[0][::-1]])

    return reverse_line.replace('\n', '')[::-1]

def process_line(original_line: str) -> int:
    """Process a line of input and return the concatenated first and last number (min, max)"""

    line = sanitize_line(original_line)

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


    result = int(first + last)

    print(original_line.replace("\n", ""), line, result)
    print("")

    return result


def main(filename: str):
    return sum(process_line(line) for line in read_input(filename))


if __name__ == "__main__":
    print(main("./1_part2.input.txt"))
