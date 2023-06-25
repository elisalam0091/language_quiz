from tkinter import *
from functools import partial

# prevents unwanted windows


class Converter:
    def __init__(self):

        # initialise variables (such as feedback)
        self.var_feedback = StringVar()
        self.var_feedback.set("")

        self.var_has_error = StringVar()
        self.var_has_error.set("no")

        self.all_calculations = []

        # format for buttons
        # arial size 14 bold, with white text
        button_font = ("Arial", "14", "bold")
        button_fg = "#080808"

        # set up GUI Frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame,
                                  text="Tuvaluan Language Quiz",
                                  font=("Arial", "14", "bold")
                                  )
        self.temp_heading.grid(row=0)

        # convert, help and history / export buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        self.to_help_button = Button(self.button_frame,
                                     text="Help / Info",
                                     bg="#FFD966",
                                     fg=button_fg,
                                     font=button_font, width=12,
                                     command=self.to_help)
        self.to_help_button.grid(row=1, column=0, padx=5, pady=5)

# opens help box
    def to_help(self):
        DisplayHelp(self)


class DisplayHelp:

    def __init__(self, partner):
        background = "#FFF2CC"

        self.help_box = Toplevel()
        # disable help button
        partner.to_help_button.config(state=DISABLED)

        # if users press cross at the top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        self.help_frame = Frame(self.help_box, width=300, height=200, bg=background)

        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame, bg=background, text="Help / Info",
                                        font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        help_text = "Talofa! Need some help? This is a multi-choice language quiz on 'Te gana Tuvalu' " \
                    "(The Tuvaluan language). \n\n" \
                    "Choose how many rounds you prefer. You have the option to answer questions in " \
                    "Tuvaluan or English. The questions are multi-choice.\n\n" \
                    "A word in Tuvaluan or English will appear at the top of the frame. " \
                    "Select one answer - one of the three will be correct. " \
                    "If the button is red and showing an 'X', your answer was incorrect. " \
                    "If the answer is correct, the button will turn green with an additional tick. \n\n" \
                    "Happy learning! " \

        self.help_text_label = Label(self.help_frame, bg=background,
                                     text=help_text, wraplength=350, justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame, font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#FFD966", fg="#080808",
                                     command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

        # closes help dialogue (used by button x at the top of dialogue)
    def close_help(self, partner):
        # puts help button back to normal
        partner.to_help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Tuvaluan Language Quiz")
    Converter()
    root.mainloop()
