import tkinter as tk

HEIGHT = 500
WIDTH = 700

def format_response():
    final_str = entry.get()
    return final_str

def print_text(text):
    label['text'] = format_response()

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#0066ff')
root.title('Post It')
canvas.pack()

frame = tk.Frame(root, bg='#0066ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Post it!", font=40, command=lambda: print_text(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#0066ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()
