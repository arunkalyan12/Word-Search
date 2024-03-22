# Word Search Solver

This Python program is designed to solve word search puzzles. It allows users to input a word search puzzle, specify the words they want to find, and then highlights the found words in the puzzle. The program uses a depth-first search (DFS) algorithm to locate the words by scanning the grid in all 8 potential directions.

## Features

- **Find Word Functionality:** The program can find and highlight multiple words in the word search grid.
- **Directional Search:** Utilizes a depth-first search algorithm to search for words in all 8 potential directions.
- **Case Insensitive Search:** Converts the input text to lowercase for case-insensitive search.

## Files

- **wordSearchSolver.py:** Contains the main functionality for solving the word search puzzle.
- **output.txt:** Text file containing the initial word search from the image, preprocessed into the correct format.
- **output2.txt:** Text file containing the output of the `convertToLower()` function in `wordSearchSolver.py`.
- **Screenshot 2024-03-23 015203.png:** Image of the word search puzzle processed through OCR.

## OCR Used

[OnlineOCR](https://www.onlineocr.net/) - Used for processing the image of the word search puzzle.

## Usage

1. Run `wordSearchSolver.py`.
2. The program will prompt you to enter the file path containing the word search puzzle.
3. Enter the number of words you want to find.
4. Enter each word one by one.
5. The program will display the word search grid with the found words highlighted.

Make sure to have the `output.txt` file in the same directory as the `wordSearchSolver.py` file for the program to work correctly.
