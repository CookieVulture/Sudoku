# Sudoku
 Sudoku solver using backtracking algorithm in Python

Sudoku is very common mathematical problem.
Algorithm - Backtracking

The approach is try to find valid solution for sudoku.
Steps - 1) Pick empty square
        2) Try all numbers and find the correct one that works
        3) Repeat for all squares
        4) If number is wrong, backtrack (There is no possible square for that value)

Functions-

isvalid => Check each column just like each element in row and is it equal to whatever the number is that we just added
            in . When we are checking through board if it's position we just inserted we ignore that position but if it's
            any other position that's gonna matter because that means there are two of same numbers in that row.
