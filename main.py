from tkinter import *
import pandas
import random


# ------------ CONSTANTS ------------------
BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 60, "bold")
timer = None

# We create the window with its configuration
window = Tk()
window.title("Flashy")
# window.minsize(width=900, height=700)
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

# ---------------------- DATA -----------------------------
data = pandas.read_csv("data/french_words.csv")
data_dict = data.to_dict(orient="records")


# ---------------------- Functions -------------------------
def random_word():
    global timer
    if timer is None:
        word_dict = random.choice(data_dict)
        french_word = word_dict["French"]
        english_word = word_dict["English"]
        canvas.itemconfig(canvas_image, image=front_image)
        canvas.itemconfig(title_text, text="French", fill="black")
        canvas.itemconfig(word_text, text=french_word, fill="black")
        # We trigger a 3s timer to automatically generate a new card
        timer = window.after(3000, turn_card, english_word)
    else:
        window.after_cancel(timer)
        timer = None
        random_word()


def turn_card(word):
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=word, fill="white")


# ------------------------ UI --------------------------------
# We create the Canvas and insert the front image and Texts
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=False)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_image)
title_text = canvas.create_text(400, 150, text="", font=FONT_TITLE)
word_text = canvas.create_text(400, 263, text="", font=FONT_WORD)
canvas.grid(column=0, row=0, columnspan=2)

# We create the buttons
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightbackground=BACKGROUND_COLOR, command=random_word)
right_button.grid(column=1, row=1)
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightbackground=BACKGROUND_COLOR, command=random_word)
wrong_button.grid(column=0, row=1)

# So that the title and words are initialized with actual data from the csv file
random_word()

window.mainloop()
