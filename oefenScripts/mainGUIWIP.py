# TKINTER OEFENINGEN



import tkinter as tk

class RunGui:
    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("800x500")
        self.root.title("RUNtitel?")
        
        self.label = tk.Label(self.root, text="RUNplx", font = "Bahnschrift 20 bold")
        self.label.pack(padx=100, pady=100)

        self.textbox = tk.Text(self.root, height=1, font="Bahnschrift 20 bold")

        self.my_entry = tk.Entry(self.root)
        self.my_entry.pack()

        self.button = tk.Button(self.root, text="EXIT", font="Bahnschrift 20 bold")
        self.button.pack(padx=200, pady=100)
        
        self.OPTIES = ["CNN own design (based on paper)", "CNN mobile net transfer learning", "CNN Squeezenet (unfinished)"]
        self.tk_var = tk.StringVar(self.root)
        self.option_menu = tk.OptionMenu(self.root, variable = self.tk_var, value = self.OPTIES)

        self.root.mainloop()

RunGui()



