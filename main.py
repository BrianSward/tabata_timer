from tkinter import *
import math

#  CONSTANTS #
FONT_NAME = "Courier"
TOTAL_SETS = 3
SET_LENGTH = 15
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 20
reps = 0
clock = None

# FUNCTIONS #

def reset_clicked():
    """resets timer when clicked, removes all completed reps"""
    global clock
    global reps
    window.after_cancel(clock)
    timer.config(text="00:00")
    my_label1.config(text="Timer", fg="Black")
    checks.config(text="")
    reps = 0


def start_clicked():
    """begins timer"""
    global reps
    reps += 1

    timer_in_seconds = SET_LENGTH
    s_break = SHORT_BREAK_MIN
    l_break = LONG_BREAK_MIN

    if reps % 8 == 0:
        countdown(l_break)
        my_label1.config(text="Long Rest", fg="red")
    elif reps % 2 == 0:
        countdown(s_break)
        my_label1.config(text="Short Rest", fg="red")
    else:
        countdown(timer_in_seconds)
        my_label1.config(text="Exercise", fg="green")


def countdown(count):
    """the clock mechanism itself"""
    global clock
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
        timer.config(text=f"{count_min}:{count_sec}")
    if count > 0:
        clock = window.after(1000, countdown, count - 1)
    else:
        start_clicked()
        sets = ""
        for _ in range(math.floor(reps/2)):
            sets += "✓"
        checks.config(text=sets)

# UI SETUP BELOW #


window = Tk()

window.title("Tabata Timer")
window.config(padx=100, pady=50)

timer = Label(text="00:00", font=(FONT_NAME, 30, "bold"))
timer.grid(column=2, row=2, columnspan=2)

my_label1 = Label(text="Timer", fg="black", font=(FONT_NAME, 40, "bold"))
my_label1.grid(column=2, row=0, columnspan=2, rowspan=2, padx=10, sticky="N")

button1 = Button(text="Start", command=start_clicked, font="bold", highlightthickness=0)
button1.grid(column=2, row=3)

button2 = Button(text="Reset", command=reset_clicked, font="bold", highlightthickness=0)
button2.grid(column=3, row=3)

checks = Label(fg="black", font=(FONT_NAME, 20, "bold"), highlightthickness=0)
checks.grid(column=0, row=4, columnspan=3, sticky="W")

# number of sets
total_sets = Label(text="Number of Sets", fg="black", font=(FONT_NAME, 15, "bold"), highlightthickness=0)
total_sets.grid(column=0, row=0, sticky="E", padx=10)

# length of set
set_seconds = Label(text="Set Length (in Seconds)", fg="black", font=(FONT_NAME, 15, "bold"), highlightthickness=0)
set_seconds.grid(column=0, row=1, sticky="E", padx=10)
# length of short rest
sr_lenth = Label(text="Short Rest Length (in Seconds)", fg="black", font=(FONT_NAME, 15, "bold"), highlightthickness=0)
sr_lenth.grid(column=0, row=2, sticky="E", padx=10)
# length of long rest
lr_length = Label(text="Long Rest Length (in Seconds)", fg="black", font=(FONT_NAME, 15, "bold"), highlightthickness=0)
lr_length.grid(column=0, row=3, sticky="E", padx=10)

# number of sets adjuster
def scale_1_used(value):
    global TOTAL_SETS
    TOTAL_SETS = int(value)


sets_slider = Scale(command=scale_1_used, from_=1, to=10, orient=HORIZONTAL)
sets_slider.grid(column=1, row=0, padx=10)

# length of set adjuster
def scale_2_used(value):
    global SET_LENGTH
    SET_LENGTH = int(value)


set_seconds_slider = Scale(command=scale_2_used, from_=5, to=60, orient=HORIZONTAL)
set_seconds_slider.grid(column=1, row=1, padx=10)

# length of short rest adjuster
def scale_3_used(value):
    global SHORT_BREAK_MIN
    SHORT_BREAK_MIN = int(value)


sr_lenth_slider = Scale(command=scale_3_used, from_=5, to=30, orient=HORIZONTAL)
sr_lenth_slider.grid(column=1, row=2, padx=10)

# length of long rest adjuster
def scale_4_used(value):
    global LONG_BREAK_MIN
    LONG_BREAK_MIN = int(value)


lr_length_slider = Scale(command=scale_4_used, from_=20, to=45, orient=HORIZONTAL)
lr_length_slider.grid(column=1, row=3, padx=10)


window.mainloop()
