# Programming Snake

A small terminal Snake game built while learning how two-dimensional grids work in Python. Move around the board, eat apples, and avoid the walls and your own tail.

## Play it yourself

Install Python 3, clone this repository, and run it in a terminal:

```sh
python3 game.py
```

Use the arrow keys or **W/A/S/D** to steer, and **Q** to quit. The real-time game uses Python's built-in `curses` terminal interface and works best in a macOS or Linux terminal.

## How it works

`game.py` keeps the snake and apple positions on a grid, redraws the board each turn, and checks for collisions. Eating an apple grows the snake and increases the score. It uses Python's standard library, so no `pip install` step is needed on systems with `curses` available.

## Demo

This version runs inside a terminal, so it does not have a browser-based live demo. [View the source code](https://github.com/Av1Sharma/ProgrammingSnake/blob/main/game.py) and try it locally with the command above. The original inspiration was [Programming Project 5: Snake](https://robertheaton.com/2018/12/02/programming-project-5-snake/).
