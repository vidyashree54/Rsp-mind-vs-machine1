import tkinter as tk
from tkinter import messagebox
import random

game_history = []

def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins"

def create_game(user_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    winner = get_winner(user_choice, computer_choice)
    game_record = {
        "id": len(game_history) + 1,
        "user": user_choice,
        "computer": computer_choice,
        "winner": winner
    }
    game_history.append(game_record)
    messagebox.showinfo("Game Result",
                        f"Game Created!\n\nYou: {user_choice}\nComputer: {computer_choice}\nResult: {winner}")
    read_games()

def read_games():
    history_text.delete("1.0", tk.END)
    if not game_history:
        history_text.insert(tk.END, "No game history yet.\n")
    else:
        for game in game_history:
            history_text.insert(tk.END, f"ID: {game['id']} | You: {game['user']} | "
                                        f"Computer: {game['computer']} | Winner: {game['winner']}\n")

def update_game():
    try:
        game_id = int(update_id_entry.get())
        new_user_choice = update_move_var.get()
        if new_user_choice not in ["rock", "paper", "scissors"]:
            messagebox.showerror("Error", "Invalid choice!")
            return
        for game in game_history:
            if game["id"] == game_id:
                winner = get_winner(new_user_choice, game["computer"])
                game["user"] = new_user_choice
                game["winner"] = winner
                messagebox.showinfo("Update", f"Game {game_id} updated!")
                read_games()
                return
        messagebox.showerror("Error", "Game ID not found.")
    except ValueError:
        messagebox.showerror("Error", "Invalid Game ID.")

def delete_game():
    try:
        game_id = int(delete_id_entry.get())
        global game_history
        original_length = len(game_history)
        game_history = [game for game in game_history if game["id"] != game_id]
        if len(game_history) == original_length:
            messagebox.showerror("Error", "Game ID not found.")
            return
        messagebox.showinfo("Delete", f"Game {game_id} deleted!")
        read_games()
    except ValueError:
        messagebox.showerror("Error", "Invalid Game ID.")

# ----------------- GUI -----------------
root = tk.Tk()
root.title("🎮 RPS Mind vs Machine 🎮")
root.geometry("600x500")

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Choose your move:").grid(row=0, column=0, columnspan=3)

tk.Button(frame, text="Rock", width=10, command=lambda: create_game("rock")).grid(row=1, column=0, padx=5)
tk.Button(frame, text="Paper", width=10, command=lambda: create_game("paper")).grid(row=1, column=1, padx=5)
tk.Button(frame, text="Scissors", width=10, command=lambda: create_game("scissors")).grid(row=1, column=2, padx=5)

# Update Section
update_frame = tk.LabelFrame(root, text="Update Game", padx=10, pady=10)
update_frame.pack(pady=10, fill="x", padx=20)

tk.Label(update_frame, text="Game ID:").grid(row=0, column=0, sticky="w")
update_id_entry = tk.Entry(update_frame, width=10)
update_id_entry.grid(row=0, column=1, sticky="w", padx=5)

tk.Label(update_frame, text="New Move:").grid(row=0, column=2, sticky="w")
update_move_var = tk.StringVar(value="rock")
update_move_menu = tk.OptionMenu(update_frame, update_move_var, "rock", "paper", "scissors")
update_move_menu.grid(row=0, column=3, sticky="w", padx=5)

tk.Button(update_frame, text="Update Game", command=update_game).grid(row=0, column=4, padx=10)

# Delete Section
delete_frame = tk.LabelFrame(root, text="Delete Game", padx=10, pady=10)
delete_frame.pack(pady=10, fill="x", padx=20)

tk.Label(delete_frame, text="Game ID:").grid(row=0, column=0, sticky="w")
delete_id_entry = tk.Entry(delete_frame, width=10)
delete_id_entry.grid(row=0, column=1, sticky="w", padx=5)

tk.Button(delete_frame, text="Delete Game", command=delete_game).grid(row=0, column=2, padx=10)

# History display
tk.Label(root, text="Game History:").pack()
history_text = tk.Text(root, height=15, width=70)
history_text.pack()

read_games()

root.mainloop()