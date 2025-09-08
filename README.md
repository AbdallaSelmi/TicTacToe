# 🎮 Tic-Tac-Toe in Python  

A beginner-friendly Python implementation of the classic **Tic-Tac-Toe** game. Built as part of my very first Python programming course, this project demonstrates fundamental coding concepts such as loops, conditionals, functions, and modular design.  

## 📖 Overview  
This project simulates a two-player Tic-Tac-Toe game in the console. Players take turns marking `X` and `O` on a 3x3 board until one wins or the game ends in a draw.  

The repo contains:  
- **`main.py`** → Entry point that runs the game.  
- **`P1.py` & `P2.py`** → Modules handling different parts of the game logic (board rendering, input handling, win/draw checks).  
- **`tictactoe_report_selmi_ghuman.pdf`** → Project documentation/report explaining the design, code structure, and reflections.  

## ✨ Features  
- Simple **command-line interface**.  
- Two-player gameplay (local).  
- Real-time board updates after each move.  
- Input validation (rejects invalid moves).  
- Win/draw detection with game-ending messages.  
- Modularized Python code (separated into multiple files).  

## 🛠️ Installation & Setup  
```bash
# Clone the repo
git clone https://github.com/yourusername/tictactoe-python.git
cd tictactoe-python

# Run the game
python main.py
```
Requirements: **Python 3.8+**

## 🎮 Usage Example  
```text
Welcome to Tic-Tac-Toe!

Player 1 (X), enter your move (row and column): 1 1
Current board:
X | - | -
- | - | -
- | - | -

Player 2 (O), enter your move (row and column): 2 2
...
```

Game ends with either:  
- **"Player X wins!"**  
- **"It’s a draw!"**  

## 📂 Project Structure  
```text
├── main.py          # Game entry point
├── P1.py            # Board setup and display functions
├── P2.py            # Game mechanics (moves, win/draw checks)
└── tictactoe_report_selmi_ghuman.pdf   # Full project write-up
```

## 📜 License  
This project was created in a college introductary python course: **educational purposes**. Free to use and adapt.  
