def find_word(wordsearch, word):
    for i in range(len(wordsearch)):
        for j in range(len(wordsearch[i])):
            if wordsearch[i][j] == word[0]:
                if search_dir(wordsearch, word, (i, j)):
                    print(f"Word '{word}' found at position ({i}, {j})")
                    return
    print(f"Word '{word}' not found")

def search_dir(wordsearch, word, start_pos):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

    for dir in directions:
        found = True
        positions = [start_pos]

        for i in range(1, len(word)):
            x, y = positions[-1][0] + dir[0], positions[-1][1] + dir[1]

            if 0 <= x < len(wordsearch) and 0 <= y < len(wordsearch[x]):
                if wordsearch[x][y] == word[i]:
                    positions.append((x, y))
                else:
                    found = False
                    break
            else:
                found = False
                break

        if found:
            for i in range(len(wordsearch)):
                line = ""
                for j in range(len(wordsearch[i])):
                    if (i, j) in positions:
                        line += " " + wordsearch[i][j]
                    else:
                        line += " -"
                print(line)
            return True

    return False

# Example usage:
wordsearch = [
    "sunwanpua",
    "usbaeiplh",
    "nhttwclso",
    "beneueaat",
    "llwrrdynn",
    "olnbotsdf",
    "cambeachu",
    "kuwavescn",
    "pineapple"
]

word_to_find = "sun"
find_word(wordsearch, word_to_find)

