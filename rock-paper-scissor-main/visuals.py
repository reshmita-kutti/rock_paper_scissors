import tkinter as tk
from PIL import Image, ImageTk
import random
from colorama import Fore, Style, init # Import init to make colorama work on Windows

# Initialize colorama
init(autoreset=True)

# --- Image Paths (Modify these to your actual image paths) ---
IMAGE_FOLDER = "images" # Create a subfolder named 'images' and put your images there
ROCK_IMAGE_PATH = f"rock_paper_scissors/images/rock1.png"
PAPER_IMAGE_PATH = f"rock_paper_scissors/images/paper2.png"
SCISSORS_IMAGE_PATH = f"rock_paper_scissors/images/scissors1.png"

# --- Game Logic (Simplified for demonstration) ---
choices_map = {
    0: "Rock",
    1: "Paper",
    2: "Scissors"
}

# --- GUI Setup ---
class RockPaperScissorsGUI:
    def __init__(self, master):
        self.master = master
        master.title("Rock, Paper, Scissors!")

        self.scores = {'user': 0, 'computer': 0}

        # Load images
        self.rock_img_tk = self.load_image(ROCK_IMAGE_PATH)
        self.paper_img_tk = self.load_image(PAPER_IMAGE_PATH)
        self.scissors_img_tk = self.load_image(SCISSORS_IMAGE_PATH)

        if not all([self.rock_img_tk, self.paper_img_tk, self.scissors_img_tk]):
            print(f"{Fore.RED}Error: One or more images could not be loaded. Please check paths and file names.")
            master.destroy() # Close the window if images are missing
            return

        # Labels for displaying choices and scores
        self.user_choice_label = tk.Label(master, text="Your Choice:", font=("Arial", 14))
        self.user_choice_label.pack(pady=5)

        self.user_image_label = tk.Label(master)
        self.user_image_label.pack(pady=10)

        self.computer_choice_label = tk.Label(master, text="Computer's Choice:", font=("Arial", 14))
        self.computer_choice_label.pack(pady=5)

        self.computer_image_label = tk.Label(master)
        self.computer_image_label.pack(pady=10)

        self.result_label = tk.Label(master, text="Make your choice!", font=("Arial", 16, "bold"))
        self.result_label.pack(pady=20)

        self.score_label = tk.Label(master, text=f"Score: You {self.scores['user']} - Computer {self.scores['computer']}", font=("Arial", 12))
        self.score_label.pack(pady=10)

        # Buttons for user input
        self.rock_button = tk.Button(master, text="Rock", command=lambda: self.play_game(0), font=("Arial", 12), width=10)
        self.rock_button.pack(side=tk.LEFT, padx=10, pady=20)

        self.paper_button = tk.Button(master, text="Paper", command=lambda: self.play_game(1), font=("Arial", 12), width=10)
        self.paper_button.pack(side=tk.LEFT, padx=10, pady=20)

        self.scissors_button = tk.Button(master, text="Scissors", command=lambda: self.play_game(2), font=("Arial", 12), width=10)
        self.scissors_button.pack(side=tk.LEFT, padx=10, pady=20)

        self.quit_button = tk.Button(master, text="Quit", command=self.quit_game, font=("Arial", 12), width=10, bg="red", fg="white")
        self.quit_button.pack(side=tk.RIGHT, padx=10, pady=20)

    def load_image(self, path, size=(150, 150)):
        try:
            img = Image.open(path)
            img = img.resize(size, Image.Resampling.LANCZOS) # Use LANCZOS for high quality downsampling
            return ImageTk.PhotoImage(img)
        except FileNotFoundError:
            print(f"{Fore.RED}Image not found: {path}")
            return None
        except Exception as e:
            print(f"{Fore.RED}Error loading image {path}: {e}")
            return None

    def display_choice_image(self, choice_value, label_widget):
        if choice_value == 0: # Rock
            label_widget.config(image=self.rock_img_tk)
        elif choice_value == 1: # Paper
            label_widget.config(image=self.paper_img_tk)
        elif choice_value == 2: # Scissors
            label_widget.config(image=self.scissors_img_tk)
        label_widget.image = self.rock_img_tk # Keep a reference to prevent garbage collection

    def play_game(self, user_choice):
        computer_choice = random.randint(0, 2)

        # Display user's choice image
        self.user_choice_label.config(text=f"Your Choice: {choices_map[user_choice]}")
        self.display_choice_image(user_choice, self.user_image_label)

        # Display computer's choice image
        self.computer_choice_label.config(text=f"Computer's Choice: {choices_map[computer_choice]}")
        self.display_choice_image(computer_choice, self.computer_image_label)

        # Determine winner
        result = ""
        if user_choice == computer_choice:
            result = f"{Fore.YELLOW}It's a tie!"
        elif (user_choice == 0 and computer_choice == 2) or \
             (user_choice == 1 and computer_choice == 0) or \
             (user_choice == 2 and computer_choice == 1):
            result = f"{Fore.GREEN}You win!"
            self.scores['user'] += 1
        else:
            result = f"{Fore.RED}Computer wins!"
            self.scores['computer'] += 1

        self.result_label.config(text=result)
        self.score_label.config(text=f"Score: You {self.scores['user']} - Computer {self.scores['computer']}")

    def quit_game(self):
        print(f"{Fore.MAGENTA}Thanks for playing! Final Score: You - {self.scores['user']}, Computer - {self.scores['computer']}{Style.RESET_ALL}")
        self.master.destroy()

# Main execution
if __name__ == "__main__":
    # Create the 'images' folder if it doesn't exist
    import os
    if not os.path.exists('rock_paper_scissors/images'):
        os.makedirs('rock_paper_scissors/images')
        print(f"{Fore.YELLOW}Created 'rock_paper_scissors/images' folder. Please place 'rock1.png', 'paper2.png', and 'scissors1.png' inside it.")
        # You might want to exit here or provide dummy images for initial testing

    root = tk.Tk()
    game_gui = RockPaperScissorsGUI(root)
    root.mainloop()