from tkinter import *
from tkinter import PhotoImage
import requests
import random
import html
score = 0
def get_question():
    data = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
    data.raise_for_status()
    question_set = data.json()["results"]
    select_question = random.choice(question_set)
    return select_question




BACKGROUND_COLOR ="#ece2e1"
window = Tk()
window.title("Quiz")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
def start():
    canvas.config(bg="black")
    selected_question = get_question()
    question1 = html.unescape(selected_question["question"])
    canvas.itemconfig(question, text=question1)


def check_right():
    global score
    dis = "True"

    selected_question = get_question()
    question = selected_question["question"]
    ans = selected_question["correct_answer"]
    if ans == dis:
        score+=1
        score_label.config(text=f"Score:{score}")
        canvas.config(bg="green")
        window.after(300,func=start)
    else:
        canvas.config(bg="red")
        window.after(300,func=start)

def check_wrong():
    global score
    dis = "False"

    selected_question = get_question()
    question = selected_question["question"]
    ans = selected_question["correct_answer"]
    if ans == dis:
        score += 1
        score_label.config(text=f"Score:{score}")
        canvas.config(bg="green")
        window.after(300,func=start)
    else:
        canvas.config(bg="red")
        window.after(300,func=start)





score_label = Label(text="Score:0",bg=BACKGROUND_COLOR, fg="black", font=("Arial",20,"italic"))
score_label.grid(column=1,row=0)
#question show box
canvas = Canvas(width=450, height=300, bg="black")
canvas.grid(column=0,row=1,columnspan=2, pady=50)
question = canvas.create_text(225,150,width=280, text="welcome to quiz app", fill="white", font=("Arial",10,"bold"))

right_image = PhotoImage(file="right.png")
right_button = Button(image=right_image, command=check_right)
right_button.grid(column=1,row=2)

wrong_image = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_image, command=check_right)
wrong_button.grid(column=0,row=2)

start()
window.mainloop()