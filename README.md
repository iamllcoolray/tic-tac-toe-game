# Assignment 2: Tic Tac Toe Game

## Description

### Game Type

Two-player, zero-sum, deterministic, perfect-information, sequential game.

### Game Description

Tic Tac Toe is a two-player perfect-information game played on a 3x3 board. Each player takes turns marking an empty cell with their symbol (‘X’ or ‘O’). The first to align three symbols in a row wins. The game ends either with a win or a draw. It is commonly used to introduce Minimax and adversarial search in AI.

### Task Description

In this assignment, you are required to develop a software application or website (a localhost implementation is acceptable) for the game Tic Tac Toe. Your program should support two modes: 1. Allow the user to play Tic Tac Toe directly, i.e., human vs. AI; 2. Allow the user to let the AI take over and play on their behalf, displaying the game progress and outcome step by step. You are expected to test your program from a user’s perspective, addressing and resolving any issues to ensure smooth and logical interaction.

## Requirements

1. Core algorithms (BOTH): Minimax & Alpha-beta pruning

2. A user-friendly interface.

3. Show the performance of two algorithms above. For example, you can add one timer in the game to monitor the time for AI making decisions.

4. Extra points (20 points at most). You may freely add additional, reasonable features to your software or website. The grader will evaluate your implementation and assign extra points based on its performance.

## Deliverables

1.  A short repot/README to explain your assignment. (PDF format)

2.  An executable source code.

3.  Put all files into one folder and compress this folder to submit.

## Setup

**Python Version 3.13+ (3.13.3 - used)**

Fork the Project and the download the repository.

### Create a Virtual Environment

```
python3 -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

```
python3 -m pip install -r requirements.txt
```

### Run the Project

```
python3 app.py
```
