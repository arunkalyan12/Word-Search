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


def convertToLower():
    input_txt_path = 'output.txt'
    output_txt_path = 'output2.txt'

    try:
        with open(input_txt_path, 'r') as input_file:
            content = input_file.read()

            lowercase = content.lower()

            with open(output_txt_path, 'w') as output_file:
                output_file.write(lowercase)
        print(f"Successfully converted text to lowercase.")

    except FileNotFoundError:
        print(f'Error: File {input_txt_path} not found.')


# convertToLower()
# import wordsearch
print('')
file = input('What file contains the word search that you want to solve: ')
wordsearch = open(file).read().splitlines()
print(wordsearch)

num_words = int(input('How many words do you ant to find: '))
word_list = []

for i in range(num_words):
    word = input("Enter a word: ")
    word_list.append(word)
print(word_list)
for word in word_list:
    find_word(wordsearch, word)
