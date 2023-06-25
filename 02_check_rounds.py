from tkinter import *

class Rounds:
    def __init__(self):

        self.var_feedback = StringVar()
        self.var_feedback.set("")

        self.var_has_error = StringVar()
        self.var_has_error.set("no")

        button_font = ("Arial", "14", "bold")
        button_fg = "#FFFFFF"

        # set up GUI Frame
        self.gui_tuv = Frame(padx=10, pady=10)
        self.gui_tuv.grid()

        self.heading = Label(self.gui_tuv,
                             text="Tuvaluan Language Quiz",
                             font=("Arial", "14", "bold")
                             )
        self.heading.grid(row=0)

        instructions = "Choose how many rounds you want to complete"
        self.tuv_instruction = Label(self.gui_tuv,
                                     text=instructions,
                                     wrap=250, width=40,
                                     justify="center")

        self.tuv_instruction.grid(row=1)

        self.num_entry = Entry(self.gui_tuv,
                               font=("Arial", "14")
                               )
        self.num_entry.grid(row=2, padx=10, pady=10)

        # error message
        error = "please enter a number"
        self.output_label = Label(self.gui_tuv, text=error,
                                  fg="#9C0000")
        self.output_label.grid(row=3)

        # convert, help and history / export buttons
        self.button_frame = Frame(self.gui_tuv)
        self.button_frame.grid(row=4)

        self.info_button = Button(self.button_frame,
                                  text="Info",
                                  bg="#7EA6E0",
                                  fg=button_fg,
                                  font=button_font, width=12)
        self.info_button.grid(row=0, column=0, padx=5, pady=5)

        self.facts_button = Button(self.button_frame,
                                   text="Funfacts",
                                   bg="#7EA6E0",
                                   fg=button_fg,
                                   font=button_font, width=12)
        self.facts_button.grid(row=0, column=1, padx=5, pady=5)

    def check_rounds(self, min_value):
        has_error = "no"
        error = "Please enter a number that is more " \
                "than {}".format(min_value)

        # checks user has entered valid number
        response = self.num_entry.get()
        try:

            response = float(response)

            if response < min_value:
                has_error = "yes"

        except ValueError:
            has_error = "yes"

        # set var_has_error so that entry box and labels can be correctly formatted by forming function
        if has_error == "yes":
            self.var_has_error.set("yes")
            self.var_feedback.set(error)
            return "invalid"


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Tuvaluan Language Quiz")
    Rounds()
    root.mainloop()
