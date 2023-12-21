import tkinter as tk

form = tk.Tk()
form.title("Hello World")
form.geometry("350x500")

def hwbutton():
    hello_world_label=tk.Label(form, text="Hello World").pack()

hello_world_label=tk.Label(form, text="Hello World").pack()
hello_world_button=tk.Button(form, text="Hello World", command=hwbutton).pack()


form.mainloop()