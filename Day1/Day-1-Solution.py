from FileReader import read_text_file
import re

def strip_data(file_path):
    input_data = read_text_file(file_path)

    left = []
    right = []

    for line in input_data.strip().split('\n'):
        l, r = map(int, line.split())
        left.append(l)
        right.append(r)

    return left, right

def solve_day1(file_path):

    left, right = strip_data(file_path)

    result = []

    while len(left) > 0 and len(right) > 0:
        smallest_left = min(left)
        smallest_right = min(right)

        difference = abs(smallest_left - smallest_right)

        result.append(difference)

        left.remove(smallest_left)
        right.remove(smallest_right)

    print("Result list:", result)
    print(sum(result))

def solve_day2(file_path):
    left, right = strip_data(file_path)

    remove_left_duplicates = sorted(list(set(left)))

    result = []
    for x in remove_left_duplicates:
        count = right.count(x)
        result.append((x * count))

    print(sum(result))

if __name__ == "__main__":
    solve_day1("day-1-input.txt")
    solve_day2("day-1-input.txt")
