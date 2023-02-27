from tkinter import *


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
        button_fg = "#FFFFFF"

        # set up GUI Frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame,
                                  text="Temperature Converter",
                                  font=("Arial", "14", "bold")
                                  )
        self.temp_heading.grid(row=0)

        # convert, help and history / export buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        self.to_help_button = Button(self.button_frame,
                                     text="Help / Info",
                                     bg="#CC6600",
                                     fg=button_fg,
                                     font=button_font, width=12,
                                     command=self.to_help)
        self.to_help_button.grid(row=1, column=0, padx=5, pady=5)

    @staticmethod
    def to_help():
        DisplayHelp()


class DisplayHelp:

    def __init__(self):
        background = "#ffe6cc"

        self.help_box = Toplevel()

        self.help_frame = Frame(self.help_box, width=300, height=200, bg=background)

        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame, bg=background, text="Help / Info", font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        help_text = "To use the program, simply enter the temperature " \
                    "you wish to convert and then choose to convert " \
                    "to either degrees Celsius (centigrade) or " \
                    "Fahrenheit..  \n\n" \
                    " Note that -273 degrees C, you will get an error message. \n\n To see your calculation history " \
                    "and export it to a text file, please click the 'History / Export' button."
        self.help_text_label = Label(self.help_frame, bg=background, text=help_text, wrap=350, justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame, font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#CC6600", fg="#FFFFFF")
        self.dismiss_button.grid(row=2, padx=10, pady=10)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
