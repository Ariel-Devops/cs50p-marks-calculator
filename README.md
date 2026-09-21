# Marks Calculator

A small Python program that calculates the average of your marks, shows your best and worst subjects, and gives you a grade.

Made while learning **CS50P (Harvard's Introduction to Programming with Python)**, after Lecture 2 on loops. This is a personal practice project, not a CS50 problem set solution.

## What it does

1. Asks for a subject name, then a mark between 0 and 20.
2. Asks again if the mark is not between 0 and 20.
3. Repeats until you type `done`.
4. Shows every subject with its mark, then the average, the highest mark, the lowest mark and a grade.

| Average | Grade |
|---|---|
| below 10 | Fail |
| 10 to 11.99 | Pass |
| 12 to 13.99 | Fairly Good |
| 14 to 15.99 | Good |
| 16 and above | Very Good |

## How to run

You need Python 3 installed.

```
python average.py
```

## Example

```
Subject (or done): python
Enter your mark (0-20): 15
Subject (or done): networks
Enter your mark (0-20): 25
Invalid mark. Please enter a mark between 0 and 20.
Enter your mark (0-20): 12
Subject (or done): done

python: 15.0
networks: 12.0

Average: 13.5
Highest mark: python (15.0)
Lowest mark: networks (12.0)
Grade: Fairly Good
```

## What I practiced

- `while` loops with `break`, to keep asking until the user is done
- Input validation with a loop
- Dictionaries (subject → mark) and looping over them with `for`
- `len()` and `sum()`
- Splitting a program into functions with `return`

## Known limitation

The program crashes if you type text instead of a number for a mark. I will fix this after Lecture 3 (Exceptions) using `try` / `except`.

## Planned improvements

- Handle invalid input with `try` / `except`
- Accept marks written with a comma (`14,5`)
- Add a small `#` bar chart of the marks

## Note on how it was built

I built this while learning, with guidance from an AI tutor (Claude). I wrote the main logic step by step and the tutor helped with the project idea, structure and feedback.
