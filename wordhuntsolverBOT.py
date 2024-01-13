import argparse
import trie

parser = argparse.ArgumentParser()
parser.add_argument('letters', metavar='lets', type=str)
args = parser.parse_args()
string_input = args.letters
file_path = '/Users/albertluo/wordhuntbot/scrabDictionary.txt'

NEIGHBORS = [(-1, -1), (-1, 0), (-1, 1),(0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

positions = {num: char for num, char in zip(range(1, 17), string_input)}

def load_dict(file_path):
    with open(file_path, 'r') as file:
        dictionary = set(word.strip().lower() for word in file)
    return dictionary

dictionary = load_dict(file_path)


def generate_grid(string):
    if len(string) != 16:
        print("Invalid string length. Please provide a string of exactly 16 characters.")
        return None

    array_4x4 = [[0] * 4 for _ in range(4)]
    index = 0

    for i in range(4):
        for j in range(4):
            array_4x4[i][j] = string[index]
            index += 1

    return array_4x4

grid = generate_grid(string_input)

def in_grid(grid, x, y):
    return y >= 0 and y < len(grid) and x >= 0 and x < len(grid[y])

def get_words(grid, words, trie, current, y, x, used):
    found = []
    if not trie.does_word_exist(current):
        return found
    if current in dictionary:
        found.append(current)
    for dy, dx in NEIGHBORS:
        ny, nx, = y + dy, x + dx
        if in_grid(grid, ny, nx) and (ny, nx) not in used:
            used.add((ny, nx))
            found.extend(get_words(grid, words, trie,current + grid[ny][nx], ny, nx, used))
            used.remove((ny, nx))

    return list(set(found))

def solve(grid):
    results = []
    root = trie.Trie()
    for n in dictionary:
        root.add_word(n)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            results += get_words(grid, dictionary, root, grid[y][x], y, x, set([(y, x)]))

    return set(results)


sorted = sorted(solve(grid), key=len, reverse=True)
print(sorted)
