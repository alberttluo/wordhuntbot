# For GamePigeon Word Hunt, going to implement custom sizing soon.

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('letters', metavar='lets', type=str)
args = parser.parse_args()
string_input = args.letters
file_path = '/Users/albertluo/wordhuntbot/scrabDictionary.txt'

oss_path_dict = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (0, 3),
    5: (1, 0),
    6: (1, 1),
    7: (1, 2),
    8: (1, 3),
    9: (2, 0),
    10: (2, 1),
    11: (2, 2),
    12: (2, 3),
    13: (3, 0),
    14: (3, 1),
    15: (3, 2),
    16: (3, 3)
}

NEIGHBORS = [(-1, -1), (-1, 0), (-1, 1),(0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

positions = {num: char for num, char in zip(range(1, 17), string_input)}

def load_dict(file_path):
    with open(file_path, 'r') as file:
        dictionary = set(word.strip().lower() for word in file)
    return dictionary

dictionary = load_dict(file_path)

def solve(grid):
    results = []
    words = set(word for word in dictionary if len(word) >= 3)
    prefix_set = set(word[:i] for word in words for i in range(1, len(word) + 1))
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            results += get_possible_words(grid, words, prefix_set, grid[y][x], y, x, set([(y, x)]))

    return set(results)



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

def in_grid(grid, y, x):
    return y >= 0 and x >= 0 and y < len(grid) and x < len(grid[y])

poss_paths = []
def get_possible_words(grid, words, prefix_set, current, y, x, used):
    found = []
    curr_path = []
    _get_possible_words_helper(grid, words, prefix_set, current, y, x, used, curr_path, found)
    return list(set(found))

def _get_possible_words_helper(grid, words, prefix_set, current, y, x, used, curr_path, found):
    if current not in prefix_set:
        return
    if current in words:
        found.append(current)
        found_path = curr_path + [(y, x)]  # Create a new list with the current path
        poss_paths.append(found_path)  # Append the found path to poss_paths
    for dy, dx in NEIGHBORS:
        ny, nx = y + dy, x + dx
        if in_grid(grid, ny, nx) and (ny, nx) not in used:
            used.add((ny, nx))
            _get_possible_words_helper(grid, words, prefix_set, current + grid[ny][nx], ny, nx, used, curr_path + [(y, x)], found)
            used.remove((ny, nx))



def get_key_from_value(dict, value):
    for key, val in dict.items():
        if val == value:
            return key
    return None

def is_neighbor(position, neighbor):
    neighbors = {
        1: [2, 5, 6],
        2: [1, 3, 5, 6, 7],
        3: [2, 4, 6, 7, 8],
        4: [3, 7, 8],
        5: [1, 2, 6, 9, 10],
        6: [1, 2, 3, 5, 7, 9, 10, 11],
        7: [2, 3, 4, 6, 8, 10, 11, 12],
        8: [3, 4, 7, 11, 12],
        9: [5, 6, 10, 13, 14],
        10: [5, 6, 7, 9, 11, 13, 14, 15],
        11: [6, 7, 8, 10, 12, 14, 15, 16],
        12: [7, 8, 11, 15, 16],
        13: [9, 10, 14],
        14: [9, 10, 11, 13, 15],
        15: [10, 11, 12, 14, 16],
        16: [11, 12, 15]
    }
    return neighbor in neighbors[position]

def find_duplicate_letters(positions):
    letter_positions = {}  # Dictionary to store the duplicate letters and their positions

    # Iterate over each position and letter in the positions dictionary
    for position, letter in positions.items():
        if letter not in letter_positions:
            letter_positions[letter] = [position]
        else:
            letter_positions[letter].append(position)

    # Filter the dictionary to include only the duplicate letters and their positions
    duplicate_letters = {letter: positions for letter, positions in letter_positions.items() if len(positions) > 1}

    return duplicate_letters

# Example usage:
string_input = args.letters
sorted_array = sorted(solve(grid), key=len, reverse=True)


word_paths = []
word_dragging = []
dups = find_duplicate_letters(positions)
poss = []

def get_sorted_array():
    return sorted_array

for word in sorted_array:
    curr = []
    for let in range(len(word)):
        if word[let] in dups.keys():
            duplicate_positions = dups[word[let]]
            for dup_val in duplicate_positions:
                    curr.append(dup_val)
                    
            else:
                curr.append(get_key_from_value(positions, word[let]))
    
        else: 
            curr.append(get_key_from_value(positions, word[let]))
    word_paths.append(curr)
    poss.append(curr)


    

with open("paths.txt", "w") as file:
    for path in word_paths:
        path_str = ' '.join(map(str, path))
        file.write(path_str + '\n')


def convert_to_coordinates(path, coordinates):
    coordinate_path = [coordinates[num] for num in path]
    return coordinate_path

coordinate_dict = {
    1: [355, 393],
    2: [435, 393],
    3: [515, 393],
    4: [595, 393],
    5: [355, 463],
    6: [435, 463],
    7: [515, 463],
    8: [595, 463],
    9: [355, 533],
    10: [435, 533],
    11: [515, 533],
    12: [595, 533],
    13: [355, 603],
    14: [435, 603],
    15: [515, 603],
    16: [595, 603]
}

letter_dict_with_coords = {
    (0, 0): grid[0][0],
    (0, 1): grid[0][1],
    (0, 2): grid[0][2],
    (0, 3): grid[0][3],
    (1, 0): grid[1][0],
    (1, 1): grid[1][1],
    (1, 2): grid[1][2],
    (1, 3): grid[1][3],
    (2, 0): grid[2][0],
    (2, 1): grid[2][1],
    (2, 2): grid[2][2],
    (2, 3): grid[2][3],
    (3, 0): grid[3][0],
    (3, 1): grid[3][1],
    (3, 2): grid[3][2],
    (3, 3): grid[3][3]
}


coords = []

with open("paths.txt", "r") as file:
    with open("coordinate_paths.txt", "w") as output_file:
        coords = []
        for line in file:
            path = list(map(int, line.strip().split()))
            coordinate_path = convert_to_coordinates(path, coordinate_dict)
            output_file.write(', '.join(map(str, coordinate_path)) + '\n')


used_words = []
coordnums = []
poss_words = []
for paths in poss_paths:
    pcurr = []
    curr_word = ""
    for p in paths:
        pcurr.append(get_key_from_value(oss_path_dict, p))
        curr_word += str(letter_dict_with_coords[p])
    if curr_word not in used_words:
        coordnums.append(pcurr)
        used_words.append(curr_word)
        poss_words.append(curr_word)

for cn in coordnums:
    ppcurr = []
    for c in cn:
        ppcurr.append(coordinate_dict[c])
    coords.append(ppcurr)

sorted_coords = sorted(coords, key=len, reverse=True)


def get_coords():
    return sorted_coords


def get_drags():
    return sorted_array

def get_poss_words():
    return sorted(poss_words, key=len, reverse=True)
