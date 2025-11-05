import tkinter as tk
import logic  
import copy

SIZE = 400
GRID_LEN = 4
GRID_PADDING = 10

BACKGROUND_COLOR_GAME = "#92877d"
BACKGROUND_COLOR_CELL_EMPTY = "#9e948a"
FONT = ("Verdana", 40, "bold")

COLOR_MAP = {
    0: ("#9e948a", "#776e65"),
    2: ("#eee4da", "#776e65"),
    4: ("#ede0c8", "#776e65"),
    8: ("#f2b179", "#f9f6f2"),
    16: ("#f59563", "#f9f6f2"),
    32: ("#f67c5f", "#f9f6f2"),
    64: ("#f65e3b", "#f9f6f2"),
    128: ("#edcf72", "#f9f6f2"),
    256: ("#edcc61", "#f9f6f2"),
    512: ("#edc850", "#f9f6f2"),
    1024: ("#edc53f", "#f9f6f2"),
    2048: ("#edc22e", "#f9f6f2"),
}

class GameGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master.title('2048 Game')
        self.master.bind("<Key>", self.key_press)

        self.pack()

        self.key_lock = False

        self.grid_cells = []
        self.init_grid()

        self.mat = logic.start_game()
        
        self.update_grid_cells()
        

    def init_grid(self):

        background = tk.Frame(self, bg=BACKGROUND_COLOR_GAME, 
                              width=SIZE, height=SIZE)
        background.grid()

        for r in range(GRID_LEN):
            row_cells = []
            for c in range(GRID_LEN):
                cell = tk.Frame(background, 
                                bg=BACKGROUND_COLOR_CELL_EMPTY,
                                width=SIZE / GRID_LEN,
                                height=SIZE / GRID_LEN)
                cell.grid(row=r, column=c, padx=GRID_PADDING, pady=GRID_PADDING)
                
                label = tk.Label(cell, text="", bg=BACKGROUND_COLOR_CELL_EMPTY,
                                 justify=tk.CENTER, font=FONT, width=4, height=2)
                label.pack()
                
                row_cells.append(label)
            self.grid_cells.append(row_cells)

    def update_grid_cells(self):

        for r in range(GRID_LEN):
            for c in range(GRID_LEN):
                num = self.mat[r][c]
                
                bg_color, fg_color = COLOR_MAP.get(num, ("#ffffff", "#000000")) 
                
                self.grid_cells[r][c].configure(bg=bg_color)
                self.grid_cells[r][c]['text'] = str(num) if num != 0 else ""
                self.grid_cells[r][c]['fg'] = fg_color

    def key_press(self, event):

        if self.key_lock:
            return
            
        key = event.char

        mat_old = copy.deepcopy(self.mat)

        if key == 'w':
            self.mat = logic.move_up(self.mat)
        elif key == 's':
            self.mat = logic.move_down(self.mat)
        elif key == 'a':
            self.mat = logic.move_left(self.mat)
        elif key == 'd':
            self.mat = logic.move_right(self.mat)
        else:
            return
            
        if self.mat != mat_old:
            logic.add_new_2(self.mat)
            self.update_grid_cells()

            state = logic.get_current_state(self.mat)
            
            if state == 'WIN':
                self.show_game_over_message("YOU WIN!")
                self.key_lock = True 
            elif state == 'GAME OVER':
                self.show_game_over_message("YOU LOST!")
                self.key_lock = True

    def show_game_over_message(self, message):

        game_over_frame = tk.Frame(self, borderwidth=2, relief="raised")
        game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        tk.Label(game_over_frame, text=message, font=("Verdana", 24, "bold"), 
                 bg="#ff0000", fg="#ffffff").pack(padx=30, pady=30)


if __name__ == "__main__":
    root = tk.Tk()  
    game = GameGUI(master=root)
    root.mainloop()