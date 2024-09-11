from tkinter import *
import math

# ---------------------------- CONSTANTS ----------------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK_MARK = "✔"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0


# ---------------------------- TIMER RESET --------------------------------------- #

# ---------------------------- TIMER MECHANISM ----------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        print(reps)
        count_down(work_sec)
        reps += 1

    elif reps % 7 == 0:
        print(reps)
        count_down(long_break_sec)
        reps += 1

    elif reps % 2 != 0:
        print(reps)
        count_down(short_break_sec)
        reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if len(str(seconds)) == 1:
        seconds = '0' + str(seconds)
    time_left = f"{minutes}:{seconds}"
    # canvas updaite is writen like this:
    canvas.itemconfig(timer_text, text=time_left)
    if count > 0:
        # print(time_left)
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------------------ #
window = Tk()
window.title("Pomodoro")
window.config(padx=60, pady=30, bg=YELLOW)

# Picture
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 111, image=tomato)
timer_text = canvas.create_text(103, 140, text="00:00", font=("Arial", 24, "bold"), fill="white")
canvas.grid(column=1, row=1)

# Labels
title = Label(text="Pomodoro timer", font=("Arial", 24, "bold"), bg=YELLOW, fg=GREEN)
title.grid(column=1, row=0)

checkmarks = Label(text=CHECK_MARK, font=("Arial", 24, "bold"), bg=YELLOW, fg=GREEN)
checkmarks.grid(column=1, row=3)

# Buttons
start = Button(text="Start", command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", bg="white")
reset.grid(column=2, row=2)

window.mainloop()
