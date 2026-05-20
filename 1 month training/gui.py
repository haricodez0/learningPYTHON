import tkinter as tk


root = tk.Tk()
root.title("My App")

label = tk.Label(root, text="Hello, 2026!")
label.pack()

button = tk.Button(root, text="Click Me", command=lambda: print("Clicked!"))
button.pack()

root.mainloop()
