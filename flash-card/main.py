from tkinter import*
import pandas
from random import randint, choice
# from analyze_data import generate_eng_word
BACKGROUND_COLOR = "#B1DDC6"
current_word = {}
to_learn = {}
try:
    
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    
    to_learn = data.to_dict(orient="records")
flip_timer = ""


def generate():
    global flip_timer,current_word
    window.after_cancel(flip_timer)
    current_word = choice(to_learn)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_word["French"], fill="black")
    canvas.itemconfig(image_flip, image=card_front_img)
    flip_timer = window.after(3000, flip)

def flip():
    global current_word
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_word["English"], fill="white")
    canvas.itemconfig(image_flip, image=new_image)
    
def is_known():
    to_learn.remove(current_word)
    
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    generate()
    
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip)


canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
new_image = PhotoImage(file="images/card_back.png")
image_flip = canvas.create_image(400,263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263,  text="word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=generate)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
known_button.grid(row=1, column=1)


generate()


window.mainloop()