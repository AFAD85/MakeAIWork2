"""
TKINTER OEFENINGEN 

CODE FOLLOWS PEP 8 STYLE




"""



import tkinter as tk

class RunGui:
    def __init__(self):
        
        # initialises the window when class is called
        self.root = tk.Tk()
        # set the dimensions of the window
        self.root.geometry("800x500")
        # sets the title of the window
        self.root.title("RUNtitel?")
        # sets the background color of the window (default = light grey)
        self.root.configure(bg="grey")
        
        # places a label (text) in the window
        self.label = tk.Label(self.root, text="RUNplx", font = "Bahnschrift 20 bold")
        # set the location of the label
        self.label.pack(padx=100, pady=100)

        # initializes the textbox (but doesn't place it in the window)
        self.textbox = tk.Text(self.root, height=1, font="Bahnschrift 20 bold")
        # stores text in self.text, useless for now, will later be used to converse with chatbot
        self.text = self.textbox.get("1.0", "end-1c")
        # initializes the variable used to keep the text in memory... I think...
        self.my_entry = tk.Entry(self.root)
        # I believe it puts the textbox in the window... loadbearing in any event... 
        self.my_entry.pack()

        # initializes the button, as of right now it does nothing
        self.button = tk.Button(self.root, text="EXIT", font="Bahnschrift 20 bold")
        # sets the location of the button
        self.button.pack(padx=200, pady=100)


        # dropdown menu with options (does not work yet)
        # a list where the options that should be available in the first dropdown menu are stored
        self.OPTIES = ["CNN own design (based on paper)", "CNN mobile net transfer learning", "CNN Squeezenet (unfinished)"]
        self.tk_var = tk.StringVar(self.root)
        self.option_menu = tk.OptionMenu(self.root, variable = self.tk_var, value = self.OPTIES)

        self.root.mainloop()
# run the window
RunGui()



