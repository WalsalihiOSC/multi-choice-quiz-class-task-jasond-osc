from tkinter import *

class CatGUI:
    def __init__(self, parent):
        self.result = StringVar()
        self.result.set("") 

        f1 = Frame(parent)

        Label(f1, text="Question").grid(column=0)
        Label(f1, text="What is the capital of New Zealand").grid(column=1, row=0)

        adjective_list = ["Wellington", "Hamilton", "Auckland", "Christchurch"]

        r = 1
        for i in(adjective_list):
            Radiobutton(f1, text=i, value=i, variable=self.result, command=self.display_choice).grid(column=1, row=r, sticky=W)
            r += 1

        f1.pack()

        self.output_label = Label(parent, text=self.result.get())
        self.output_label.pack()

    def display_choice(self):
        return
    
if __name__ == "__main__":
    root = Tk()
    buttons = CatGUI(root)
    root.mainloop()
