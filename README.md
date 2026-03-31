# Mad Libs Game
The program asks the user to input different types of words (nouns, verbs, etc.) and generates a story based on the selected template.

## Features
Three story templates:
* The Hospital
* The Camping
* The Letter
Input validation
Randomized elements for varied output
Clear structure

## Requirements
Python 3x
No external libraries

## How to Play
1. Start the program.
2. Choose a template by entering 1, 2, or 3.
3. Follow the prompts:
   Enter words (nouns, verbs, adjectives, etc.)
   Enter numbers when requested.
4. The program will generate and display a story.

## Code Structure
* get_word(prompt)
  Ensures the user enters a non-empty word.
* get_number(prompt)
  Ensures the user enters a valid integer.
* madLibs()
  Main function that:
  - Handles template selection
  - Collects user input
  - Generates and prints the story
