import tkinter as tk
from tkinter import messagebox

class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tic Tac Toe")
        self.geometry("300x300")
        self.configure(bg='#282C34')  # Setting a background color

        self.board = ['' for _ in range(9)]  # Represent the board as a list
        self.current_player = 'X'

        # Create buttons for the board
        self.buttons = [tk.Button(self, font=('normal', 40), width=5, height=2, bg='#45A29E', command=lambda i=i: self.on_click(i))
                        for i in range(9)]

        # Arrange buttons in a 3x3 grid
        for i, button in enumerate(self.buttons):
            row = i // 3
            col = i % 3
            button.grid(row=row, column=col)

    def on_click(self, i):
        if not self.board[i] and not self.check_winner():
            color = '#FE2E2E' if self.current_player == 'X' else '#2E64FE'
            self.buttons[i].config(text=self.current_player, fg=color)
            self.board[i] = self.current_player
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            else:
                # Switch to the other player
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        win_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)  ]             # Diagonals

        for combo in win_combinations:
            if self.board[combo[0]] and self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]:
                return True
        return False

    def reset_game(self):
        self.board = ['' for _ in range(9)]
        for button in self.buttons:
            button.config(text="", fg='black')
        self.current_player = 'X'


if __name__ == "__main__":
    game = TicTacToe()
    game.mainloop()
