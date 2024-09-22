import tkinter as tk
from tkinter import messagebox

def check_winner():
    global winner
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            winner = True
            for i in combo:
                buttons[i].config(bg="green")
            # Show winner message and then update the score
            show_winner_message(f"Player {buttons[combo[0]]['text']} wins!", buttons[combo[0]]['text'])
            return
    if all(button["text"] != "" for button in buttons):
        show_winner_message("It's a draw!", None)
        
def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        if not winner:
            toggle_player()

def toggle_player():
    global current_player
    current_player = "x" if current_player == "o" else "o"
    label.config(text=f"Player {current_player}'s turn")

def update_score(player):
    global x_score, o_score, draw_score
    if player == "x":
        x_score += 1
    elif player == "o":
        o_score += 1
    else:  # If it's a draw, increment draw_score
        draw_score += 1
    score_label.config(text=f"X: {x_score} \t O: {o_score} \t Draw: {draw_score}")

def reset_game():
    global winner
    winner = False
    for button in buttons:
        button.config(text="", bg="SystemButtonFace")
    toggle_player()

def show_winner_message(message, player):
    # Create a pop-up window to show the winner message
    winner_popup = tk.Toplevel(root)
    winner_popup.title("Game Result")
    winner_label = tk.Label(winner_popup, text=message, font=("normal", 16))
    winner_label.pack(padx=20, pady=10)
    winner_popup.after(1500, lambda: [winner_popup.destroy(), reset_game()])  # Close pop-up after 1.5 seconds

    # Update the score: player can be "x", "o", or None (for draw)
    update_score(player)

def quit_game():
    # Show final score in a messagebox
    final_score_message = f"Final Score:\nX: {x_score}\nO: {o_score}\nDraw: {draw_score}"
    messagebox.showinfo("Final Score", final_score_message)
    root.quit()

# Code starts from here
root = tk.Tk()
root.title("Tic Tac Toe")

buttons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2, command=lambda i=i: button_click(i)) for i in range(9)]
for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

current_player = "x"
winner = False
x_score = 0
o_score = 0
draw_score = 0  # Variable to keep track of draw score

label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

score_label = tk.Label(root, text="X: 0 \t O: 0 \t Draw: 0", font=("normal", 14))
score_label.grid(row=4, column=0, columnspan=3)

quit_button = tk.Button(root, text="Quit", font=("normal", 14), command=quit_game)
quit_button.grid(row=5, column=0, columnspan=3)

root.mainloop()
