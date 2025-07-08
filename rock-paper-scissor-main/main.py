import tkinter as tk
from PIL import Image, ImageTk
import random
import os
from colorama import Fore, Style, init

# Initialize colorama for console output (e.g., error messages)
init(autoreset=True)

# --- Configuration for Images ---
IMAGE_FOLDER = "images"
ROCK_IMAGE_NAME = "rock1.jpg"
PAPER_IMAGE_NAME = "paper2.png"
SCISSORS_IMAGE_NAME = "scissors1.png"

ROCK_IMAGE_PATH = os.path.join(IMAGE_FOLDER, ROCK_IMAGE_NAME)
PAPER_IMAGE_PATH = os.path.join(IMAGE_FOLDER, PAPER_IMAGE_NAME)
SCISSORS_IMAGE_PATH = os.path.join(IMAGE_FOLDER, SCISSORS_IMAGE_NAME)

# --- Game Logic Mappings ---
choices_map = {
    0: "Rock",
    1: "Paper",
    2: "Scissors"
}

# --- GUI Application Class ---
class RockPaperScissorsGUI:
    def __init__(self, master):
        self.master = master
        master.title("Rock, Paper, Scissors!")
        master.geometry("600x750")
        master.resizable(False, False)

        self.scores = {'user': 0, 'computer': 0}

        self.rock_img_tk = self._load_image(ROCK_IMAGE_PATH)
        self.paper_img_tk = self._load_image(PAPER_IMAGE_PATH)
        self.scissors_img_tk = self._load_image(SCISSORS_IMAGE_PATH)

        if not all([self.rock_img_tk, self.paper_img_tk, self.scissors_img_tk]):
            print(f"{Fore.RED}Error: One or more game images could not be loaded. Please ensure they are in the '{IMAGE_FOLDER}' folder and are valid image files. Application will close.{Style.RESET_ALL}")
            master.destroy()
            return

        self.display_frame = tk.Frame(master, bd=2, relief="groove", padx=10, pady=10)
        self.display_frame.pack(pady=10, fill="x", padx=20)

        self.user_choice_label = tk.Label(self.display_frame, text="Your Choice:", font=("Arial", 14, "bold"))
        self.user_choice_label.grid(row=0, column=0, pady=5)

        self.user_image_label = tk.Label(self.display_frame, relief="ridge", bd=1)
        self.user_image_label.grid(row=1, column=0, padx=10, pady=10)

        self.computer_choice_label = tk.Label(self.display_frame, text="Computer's Choice:", font=("Arial", 14, "bold"))
        self.computer_choice_label.grid(row=0, column=1, pady=5)

        self.computer_image_label = tk.Label(self.display_frame, relief="ridge", bd=1)
        self.computer_image_label.grid(row=1, column=1, padx=10, pady=10)

        self.result_label = tk.Label(master, text="Make your choice to start!", font=("Arial", 18, "bold"), pady=15)
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(master, text=f"Score: You {self.scores['user']} - Computer {self.scores['computer']}", font=("Arial", 14), pady=5)
        self.score_label.pack(pady=5)

        self.button_frame = tk.Frame(master, bd=2, relief="raised", padx=10, pady=10)
        self.button_frame.pack(pady=20)

        self.rock_button = tk.Button(self.button_frame, text="Rock", command=lambda: self._play_game(0),
                                      font=("Arial", 14), width=12, height=2, bg="#add8e6", activebackground="#87ceeb")
        self.rock_button.grid(row=0, column=0, padx=10, pady=10)

        self.paper_button = tk.Button(self.button_frame, text="Paper", command=lambda: self._play_game(1),
                                       font=("Arial", 14), width=12, height=2, bg="#90ee90", activebackground="#6be06b")
        self.paper_button.grid(row=0, column=1, padx=10, pady=10)

        self.scissors_button = tk.Button(self.button_frame, text="Scissors", command=lambda: self._play_game(2),
                                         font=("Arial", 14), width=12, height=2, bg="#ffcccb", activebackground="#ff9999")
        self.scissors_button.grid(row=0, column=2, padx=10, pady=10)

        self.quit_button = tk.Button(master, text="Quit Game", command=self._quit_game,
                                      font=("Arial", 14), width=15, bg="#d9534f", fg="white", activebackground="#c9302c")
        self.quit_button.pack(pady=20)

    def _load_image(self, path, size=(200, 200)):
        try:
            img = Image.open(path)
            img = img.resize(size, Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(img)
        except FileNotFoundError:
            print(f"{Fore.RED}Error: Image file not found at: {path}{Style.RESET_ALL}")
            return None
        except Exception as e:
            print(f"{Fore.RED}Error loading image {path}: {e}{Style.RESET_ALL}")
            return None

    def _display_choice_image(self, choice_value, label_widget):
        if choice_value == 0:
            label_widget.config(image=self.rock_img_tk)
        elif choice_value == 1:
            label_widget.config(image=self.paper_img_tk)
        elif choice_value == 2:
            label_widget.config(image=self.scissors_img_tk)
        label_widget.image = label_widget.cget("image")

    def _play_game(self, user_choice):
        computer_choice = random.randint(0, 2)

        self.user_choice_label.config(text=f"Your Choice: {choices_map[user_choice]}")
        self.computer_choice_label.config(text=f"Computer's Choice: {choices_map[computer_choice]}")

        self._display_choice_image(user_choice, self.user_image_label)
        self._display_choice_image(computer_choice, self.computer_image_label)

        # Store the plain text for the GUI label
        gui_result_text = ""
        # Store the colored text for the console output
        console_result_text = ""

        if user_choice == computer_choice:
            gui_result_text = "It's a tie!"
            console_result_text = f"{Fore.YELLOW}It's a tie!{Style.RESET_ALL}"
        elif (user_choice == 0 and computer_choice == 2) or \
             (user_choice == 1 and computer_choice == 0) or \
             (user_choice == 2 and computer_choice == 1):
            gui_result_text = "You win!"
            console_result_text = f"{Fore.GREEN}You win!{Style.RESET_ALL}"
            self.scores['user'] += 1
        else:
            gui_result_text = "Computer wins!"
            console_result_text = f"{Fore.RED}Computer wins!{Style.RESET_ALL}"
            self.scores['computer'] += 1

        # Update the result label on the GUI with the plain text
        self.result_label.config(text=gui_result_text)
        self.score_label.config(text=f"Score: You {self.scores['user']} - Computer {self.scores['computer']}")

        # Optionally print the colored result to the console for debugging/extra feedback
        print(console_result_text)

    def _quit_game(self):
        print(f"{Fore.MAGENTA}Thanks for playing! Final Score: You - {self.scores['user']}, Computer - {self.scores['computer']}{Style.RESET_ALL}")
        self.master.destroy()

if __name__ == "__main__":
    if not os.path.exists(IMAGE_FOLDER):
        os.makedirs(IMAGE_FOLDER)
        print(f"{Fore.YELLOW}WARNING: The '{IMAGE_FOLDER}' folder was not found and has been created.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Please place your '{ROCK_IMAGE_NAME}', '{PAPER_IMAGE_NAME}', and '{SCISSORS_IMAGE_NAME}' files inside this '{IMAGE_FOLDER}' folder.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}You may need to run the program again after adding the images.{Style.RESET_ALL}")

    root = tk.Tk()
    game_gui = RockPaperScissorsGUI(root)
    root.mainloop()