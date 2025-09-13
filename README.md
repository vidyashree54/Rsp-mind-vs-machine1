# Rsp-mind-vs-machine1
# Description:
This project is a GUI-based Rock-Paper-Scissors game built using Python and Tkinter. It allows a user to play the classic game against the computer, view a history of all games played, and even update or delete specific game entries using their Game ID.

# Features:
🧩 **Core Features in This Project**
🎮 1. **Game Mechanics (Rock-Paper-Scissors)**
          User chooses a move: rock, paper, or scissors.
          Computers randomly choose a move.
          Game logic determines the winner based on standard RPS rules.

📦 2. **CRUD Functionality**
         Action	Description
         Create:	When a user plays a game, a new record is created and stored in memory (game_history).
         Read:	All games are displayed in a text area showing ID, user move, computer move, and winner.
         Update:	Users can update the move for a specific game ID. The winner is recalculated based on the old computer move.
         Delete:	Users can delete a game by its ID. The game is removed from the history list.
         
🧠 3. **Game Logic**
         The get_winner(user, computer) function determines the outcome.
         The logic checks for win/tie/loss conditions using conditionals.

🧰 4. **GUI with Tkinter**
         Buttons (Rock, Paper, Scissors) to play the game.
         Input fields and dropdowns to update or delete games.
         Label, Button, Entry, Text, and OptionMenu widgets.
         GUI organized using Frames and LabelFrames for clarity.
         Use of grid() and pack() for layout management.

📋 5. **Dynamic Text Display**
        The game history is displayed using a Text widget.
        Auto-refreshes on each game played, updated, or deleted.

📤 6. **User Feedback via Message Boxes**
        messagebox.showinfo() for success notifications (e.g., game created, updated).
        messagebox.showerror() for error handling (e.g., invalid ID or move).

🗂️ 7. **In-Memory Data Storage**
        Games are stored in a Python list (game_history).
        Each game is a dictionary with:
        {
  "id": 1,
  "user": "rock",
  "computer": "paper",
  "winner": "Computer wins"
}

# Steps to Run the Code:

1️⃣ Make sure Python is installed
        Open your terminal or command prompt and run:
            python --version
        If it shows a version (like Python 3.x.x), you're good!
        If not, download Python and install it.

2️⃣ Create a new Python file
        Open a folder or your desktop.
        Create a file and name it:
            rps_game.py
        Copy and paste the full code into this file.

3️⃣ Run the code
✅ Option A: Using Terminal
        Open your terminal or command prompt.
        Go to the folder where your file is saved:
            cd path/to/your/folder
        Run the file:
            python rps_game.py

✅ Option B: Double-click (Windows)
          If Python is properly installed, you can also double-click the file to run it.

4️⃣ Play the Game
       A window will open with buttons:
         Click Rock, Paper, or Scissors to play.
      Update or delete previous games using the input fields.
      View game history in the box below.

# Example code with output:
import tkinter as tk
from tkinter import messagebox
import random

def play(user_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result = "You win!"
    else:
        result = "Computer wins!"
    
    messagebox.showinfo("Result",
                        f"You chose: {user_choice}\n"
                        f"Computer chose: {computer_choice}\n"
                        f"{result}")
# GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x200")

tk.Label(root, text="Choose your move:", font=("Arial", 14)).pack(pady=10)

tk.Button(root, text="Rock", width=10, command=lambda: play("rock")).pack(pady=5)
tk.Button(root, text="Paper", width=10, command=lambda: play("paper")).pack(pady=5)
tk.Button(root, text="Scissors", width=10, command=lambda: play("scissors")).pack(pady=5)

root.mainloop()

# output:
You chose: rock
Computer chose: scissors
You win!



