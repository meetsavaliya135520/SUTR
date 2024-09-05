import random
import tkinter as tk
from tkinter import messagebox
from nltk.corpus import wordnet


# Function to compute scrabble score
def scrabble_score(word):
    score_dict = {
        1: "AEIOULNRST",
        2: "DG",
        3: "BCMP",
        4: "FHVWY",
        5: "K",
        8: "JX",
        10: "QZ"
    }

    score = 0
    for letter in word.upper():
        for points, letters in score_dict.items():
            if letter in letters:
                score += points
                break
    return score


# Function to validate the word from dictionary (mocked with a sample list)
def is_valid_word(word):
    return wordnet.synsets(word)


# Countdown function
def countdown(time_sec):
    global countdown_running

    mins, secs = divmod(time_sec, 60)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    timer_label.config(text=f"Time left: {timeformat}")
    if time_sec > 0:
        countdown_running = root.after(1000, countdown, time_sec - 1)  # Wait 1 second before the next call
    else:
        countdown_running = None
        messagebox.showinfo("Time's Up", "You took too long! The game will now exit.")
        root.quit()  # Close the application


# Function to handle the game logic
def play_game():
    word = entry.get().strip()
    if not countdown_running:  # Stop if the countdown is finished
        return

    # Stop the countdown for this word
    root.after_cancel(countdown_running)

    if len(word) != word_length:
        messagebox.showerror("Invalid Input", f"Please enter a word with exactly {word_length} letters.")
        start_new_round()  # Restart round
        return

    if not word.isalpha():
        messagebox.showerror("Invalid Input", "Please enter alphabets only.")
        start_new_round()  # Restart round
        return

    if not is_valid_word(word):
        messagebox.showerror("Invalid Input", "Not a valid word. Please try again.")
        start_new_round()  # Restart round
        return

    score = scrabble_score(word)
    global total_score
    total_score += score
    score_label.config(text=f"Your score for '{word}' is {score}. Total Score: {total_score}")

    global rounds
    rounds += 1
    if rounds >= 10:
        messagebox.showinfo("Game Over", f"10 rounds completed! Your total score is {total_score}.")
        root.quit()
    else:
        start_new_round()


# Function to start a new round
def start_new_round():
    global word_length, countdown_running
    word_length = random.randint(3, 7)
    prompt_label.config(text=f"Enter a word with exactly {word_length} letters:")
    entry.delete(0, tk.END)

    if countdown_running:
        root.after_cancel(countdown_running)  # Cancel the previous timer if it exists

    countdown_running = True
    countdown(15)


# Initialize the GUI
root = tk.Tk()
root.title("Scrabble Game")

total_score = 0
rounds = 0
word_length = random.randint(3, 7)
countdown_running = None

prompt_label = tk.Label(root, text=f"Enter a word with exactly {word_length} letters:")
prompt_label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

submit_button = tk.Button(root, text="Submit", command=play_game)
submit_button.pack(pady=10)

score_label = tk.Label(root, text="Total Score: 0")
score_label.pack(pady=10)

timer_label = tk.Label(root, text="Time left: 00:15")
timer_label.pack(pady=10)

# Start the first round
start_new_round()

# Run the GUI main loop
root.mainloop()
