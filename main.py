import time
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
checkmark = "✔"
checkmark_text = ""
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer_is_on = True

# ---------------------------- TIMER RESET ------------------------------- #


def timer_refresh(text="00:00"):
    canvas.itemconfigure(canvas_text_id, text=text)
    window.update()


def timer_stop():
    global timer_is_on, checkmark_text
    timer_is_on = False
    timer_refresh()
    checkmark_text = ""


# ---------------------------- TIMER MECHANISM ------------------------------- #


def timer_mechanism(minutes):
    global timer_is_on
    while minutes > 0 and timer_is_on:
        seconds = 5
        minutes -= 1
        while seconds > 0 and timer_is_on:
            time.sleep(1)
            seconds -= 1
            text = f"{minutes}:{seconds if seconds > 9 else '0' + str(seconds)}"
            timer_refresh(text=text)


def change_title(text):
    if text == "Break":
        timer_label.config(text=text, fg=PINK)
    elif text == "Timer":
        timer_label.config(text=text, fg=GREEN)
    elif text == "Work":
        timer_label.config(text=text, fg=GREEN)


def add_check_label():
    global checkmark_text
    checkmark_text += checkmark
    check_label.config(text=checkmark_text)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def timer_start():
    global timer_is_on
    for cycle in range(4):
        if not timer_is_on:
            break
        change_title(text="Work")
        timer_mechanism(WORK_MIN)
        add_check_label()
        if cycle == 3:
            change_title(text="Break")
            timer_mechanism(LONG_BREAK_MIN)
        else:
            change_title(text="Break")
            timer_mechanism(SHORT_BREAK_MIN)
    timer_is_on = True
    change_title(text="Timer")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas_text_id = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", font=(FONT_NAME, 18, "bold"), command=timer_start)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", font=(FONT_NAME, 18, "bold"), command=timer_stop)
reset_button.grid(row=2, column=2)

check_label = Label(text=checkmark_text, font=(FONT_NAME, 30, "bold"), bg=YELLOW, fg=GREEN)
check_label.grid(row=3, column=1)

window.mainloop()
