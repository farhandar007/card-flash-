import tkinter
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
new_word = None
right_button_press = False

def random_word():
    global new_word, timer, data_dict
    window.after_cancel(id=timer)
    timer = window.after(3000, func=flip)
    new_word = random.choice(data_dict)
    french_word = new_word["French"]
    canvas.itemconfig(canvas_text, text="French", fill="black")
    canvas.itemconfig(canvas_new_text, text=french_word, fill="black")

def known_word():
    global new_word
    data_dict.remove(new_word)
    new_data = pandas.DataFrame(data_dict)
    new_data.to_csv("./data/words_to_learn.csv", index=False)
    random_word()
def flip():
    english_word = new_word["English"]
    canvas.itemconfig(canvas_text, text="English", fill="white")
    canvas.itemconfig(canvas_new_text, text=english_word, fill="white")
    canvas.itemconfig(bg_img, image=flip_img)




# creating window
window = tkinter.Tk()
window.title("flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
# creating canvas
canvas = tkinter.Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = tkinter.PhotoImage(file="./images/card_front.png")
bg_img = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
# canvas label
canvas_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
canvas_new_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
# creating buttons
# wrong button
image = tkinter.PhotoImage(file="./images/wrong.png")
wrong_button = tkinter.Button(image=image, highlightthickness=0, command=random_word)
wrong_button.grid(row=1, column=0)
# right button
my_image = tkinter.PhotoImage(file="./images/right.png")
right_button = tkinter.Button(image=my_image, highlightthickness=0, command=known_word)
right_button.grid(row=1, column=1)
# flipping the card
flip_img = tkinter.PhotoImage(file="./images/card_back.png")
timer = window.after(3000, func=flip)

# notes-here when the timer runs then immediately after random_word() is executed ,which cancels the above timer and at
# the end new timer is set
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
finally:
    data_dict = data.to_dict(orient="records")
    random_word()










window.mainloop()


