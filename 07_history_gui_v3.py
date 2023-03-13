from tkinter import *
from functools import partial


class Converter:

    def __init__(self):

        # format for buttons
        # arial size 14 bold, with white text
        button_font = ("Arial", "14", "bold")
        button_fg = "#FFFFFF"

        # Five item list
        self.all_calculations = ['0 F° is -18°', '0 C° is 32 F°',
                                 '30 F° is -1 C°', '30° C° is 86 F°',
                                 '40 F° is 4 C°']

        # six item list
        # self.all_calculations = ['0 F° is -18°', '0 C° is 32 F°',
        # '30 F° is -1 C°', '30° C° is 86 F°',
        # '40 F° is 4 C°', '100 C° is 212 F°']

        # set up GUI Frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.button_frame = Frame(padx=30, pady=30)
        self.button_frame.grid(row=0)

        self.to_history_button = Button(self.button_frame,
                                        text="History / Export",
                                        bg="#004C99",
                                        fg=button_fg,
                                        font=button_font, width=12,
                                        state=DISABLED,
                                        command=lambda: self.to_history(self.all_calculations))
        self.to_history_button.grid(row=1, column=1, padx=5, pady=5)

        # remove when integrating !!!
        self.to_history_button.config(state=NORMAL)

# opens help box
    def to_history(self, all_calculations):
        HistoryExport(self, all_calculations)


class HistoryExport:

    def __init__(self, partner, calc_list):

        # set maximum number of calculation to 5
        # this can be changed if we want to show fewer
        # more calculations
        max_calcs = 5
        self.var_max_calcs = IntVar()
        self.var_max_calcs.set(max_calcs)

        # function converts contents of calculation lists into string
        calc_string_text = self.get_calc_string(calc_list)

        # sets up dialogue box and background colour
        self.history_box = Toplevel()

        # disable help button
        partner.to_history_button.config(state=DISABLED)

        # if users press cross at the top, closes help and 'releases' help button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        self.history_frame = Frame(self.history_box, width=300, height=200)

        self.history_frame.grid()

        self.dismiss_button = Button(self.history_frame,
                                     font=("Arial", "14", "bold"),
                                     text="Dismiss", bg="#666666",
                                     fg="#FFFFFF",
                                     command=partial(self.close_history, partner))

        self.dismiss_button.grid(row=2, padx=10, pady=10)

        self.history_heading_label = Label(self.history_frame,
                                           text="History / Export",
                                           font=("Arial", "14", "bold"))
        self.history_heading_label.grid(row=0)

        # customise text and background colour for calculation area
        # depending on whether all or only some calc are shown.

        num_calcs = len(calc_list)

        if num_calcs > max_calcs:
            calc_background = "#FFE6CC"
            showing_all = " Here are your recent calculations " \
                          "({}/{} calculations shown). Please export your " \
                          "calculations to see your full calculation history".format(max_calcs, num_calcs)

        else:
            calc_background = "#B4FACB"
            showing_all = "Below is your calculation history"

        history_text = "{} \n\nAll calculations are shown " \
                       "to the nearest degree".format(showing_all)

        self.text_instruction_label = Label(self.history_frame,
                                           text=history_text, width=45,
                                           justify="left", wraplength=300,
                                           padx=10, pady=10)
        self.text_instruction_label.grid(row=1)

        self.all_calcs_label = Label(self.history_frame,
                                     text=calc_string_text,
                                     padx=10, pady=10, bg="#ffe6cc",
                                     width=40, justify="left")
        self.all_calcs_label.grid(row=2)

        # instructions for saving files
        save_text = "Either choose a custom file name (and push " \
                    "<Export>) or simply push <export> to save your" \
                    "calculations in a text file. If the filename" \
                    "already exists, it will be overwritten!"

        self.text_instruction_label = Label(self.history_frame,
                                            text=save_text, wraplength=300,
                                            justify="left", width=40,
                                            padx=10, pady=10)

        self.text_instruction_label.grid(row=3)

        # file name entry widget, white background to start
        self.filename_entry = Entry(self.history_frame,
                                    font=("Arial", "14"), bg="#ffffff", width=25)
        self.filename_entry.grid(row=4, padx=10, pady=10)

        self.filename_error_label = Label(self.history_frame, text="Filename error goes here",
                                          fg="#9C0000", font=("Arial", "14", "bold"))
        self.filename_error_label.grid(row=5)

        self.button_frame = Frame(self.history_frame)
        self.button_frame.grid(row=6)

        self.export_button = Button(self.button_frame,
                                    font=("Arial", "14", "bold"),
                                    text="Export", bg="#004C99",
                                    fg="#FFFFFF", width=12)
        self.export_button.grid(row=0, column=0, padx=0, pady=10)

        self.dismiss_button = Button(self.button_frame, font=("Arial", "14", "bold"),
                              text="Dismiss", bg="#666666",
                              fg="#FFFFFF", width=12,
                              command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1, padx=10, pady=10)

        # closes help dialogue (used by button x at the top of dialogue)

    def get_calc_string(self, var_calculations):
        # get maximum calc to display (was set __init__ func)
        max_calcs = self.var_max_calcs.get()
        calc_string = ""

        # workout how many times we need to loop to output
        # either the last five calcs or all the cals
        if len(var_calculations) >= max_calcs:
            stop = max_calcs

        else:
            stop = len(var_calculations)

        # iterate to all but last item,
        # adding item and line break to calc string
        for item in range(0, stop - 1):
            calc_string += var_calculations[len(var_calculations) - item - 1]

            calc_string += "\n"

        # add final item without an extra line break ie: last item will be fifth from the end!
        calc_string += var_calculations[-max_calcs]

        return calc_string

    def close_history(self, partner):
        # puts help button back to normal
        partner.to_history_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
