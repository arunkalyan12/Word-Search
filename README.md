# Word-Search
First it asks for a text file which contains the wordsearch. Then it imports the data into arrays. Then the user will input how many words you want to search for and then askes you to enter each word. Once the word is found it highlights the word so you can clearly see the position. The process of locating the word involves scanning the word search grid to identify the initial letters of the target word, recording their positions in an array. Subsequently, a depth-first algorithm (DFS) is employed to explore each of the identified starting points, traversing through the 8 potential directions to uncover the complete word.

## OCR used
https://www.onlineocr.net/

## Breakdown of files/folders
* readme.md - This readme markdown file
* Screenshot 2023-12-24 143156.jpg - This is the image that wass process through the OCR which I personlly got and them processed and saved in output.txt:
SUNWANPUA USBAE I P LH NHTTWCLSO BENEUEAAT L LWRRDYNN OLNBOTSDF CAMBEACHU KUWAVESCN P INEAPPLE

* output.txt - A text file containing an initial word serch from the image using OCR that is preprocessed into correct format of number of rows and columns. This was made using a free OCR.
* output2.txt - A text file containing the output of the convertToLower() function in the wordSearchSolver.py
* wordSearchSolver.py - This is the python script where it all happens.
