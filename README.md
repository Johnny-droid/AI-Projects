# AI Projects

## Project 1: Board Game - Wana

### Description

Wana is a board game played by two players. The game is played on the board represented. Each player has 8 pieces.
The pieces are placed on the board in the following way:

![Wana Board](/Project1/doc/wana_board.jpeg)

The objective of the game is to block one of the opponent's pieces in all directions. The game ends when one of the players manages to block one of the opponent's pieces.

Keep in mind that the pieces can move in all directions (up, down, left, right), and this includes following the circle lines to the opposite position, as well as exiting the board through the end lines and appearing at the opposite side.

Our objective was to build a working **Wana** game in python, that can be played by two players. These players can be either human or AI players.

The AI uses a **minimax** algorithm with **alpha-beta pruning** to find the best move. There are multiple levels of difficulty, determined by the heuristic used as well as the depth of the minimax algorithm.

### How to run

To run the game, simply move to the `Project1` and run the `wana.py` file with the following command:

```bash
python3 wana.py 
```

Make sure you have all the following libraries installed:
- pygame
- pygame_menu
- numpy

They are required to run the game.


