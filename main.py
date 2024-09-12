from tkinter import *
import math

# ---------------------------- CONSTANTS ----------------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 0
timer = None


# ---------------------------- TIMER RESET --------------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Pomodoro timer")
    checkmarks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ----------------------------------- #
def start_timer():
    global reps

    # calculate time in seconds
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # determine the timer type, based on reps
    # if reps == 8:
    #     quit()
    reps += 1
    if reps % 8 == 0:
        count_down(long_break_sec)
        title.config(text="Long break", fg=RED)
    elif reps % 2 != 0:
        count_down(work_sec)
        title.config(text="Work", fg=GREEN)
    else:
        count_down(short_break_sec)
        title.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = '0' + str(seconds)
    time_left = f"{minutes}:{seconds}"
    # canvas updaite is writen like this:
    canvas.itemconfig(timer_text, text=time_left)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)  # WINDOW REFRESH SETTING <-------------------------------------
    else:
        start_timer()
        check_marks = "".join("✔" for item in range(0, reps) if item > 0 and item % 2 != 0)
        checkmarks.config(text=check_marks)


# ---------------------------- UI SETUP ------------------------------------------ #
window = Tk()
window.title("Pomodoro")
window.config(padx=60, pady=30, bg=YELLOW)

# Picture
canvas = Canvas(width=260, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(130, 111, image=tomato)
timer_text = canvas.create_text(130, 140, text="00:00", font=("Arial", 24, "bold"), fill="white")
canvas.grid(column=1, row=1)

# Labels
title = Label(text="Pomodoro timer", font=("Arial", 24, "bold"), bg=YELLOW, fg=GREEN)
title.grid(column=1, row=0)

checkmarks = Label(font=("Arial", 24, "bold"), bg=YELLOW, fg=GREEN)
checkmarks.grid(column=1, row=3)

# Buttons
start = Button(text="Start", command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", bg="white", command=reset_timer)
reset.grid(column=2, row=2)

window.mainloop()
