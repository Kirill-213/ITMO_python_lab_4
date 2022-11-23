from generation import key_generation
import tkinter as tk

# функция для обработки нажатия кнопки
def click_button():
    txt.delete(0, 30)
    p = str(key_generation())
    txt.insert(0, p)

window = tk.Tk()
window.title("DOTA 2 key generator")
window.geometry('772x436')
window.resizable(width=False, height=False)
window.image = tk.PhotoImage(file="dota.png")
bg_logo = tk.Label(window, image=window.image)
bg_logo.grid(row=0, column=0)

bg_logo = tk.Label(window, image=window.image)
bg_logo.grid(row=0, column=0)
txt = tk.Entry(window, width=30)
txt.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
label = tk.Label(text="Ваш ключ:")
label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
btn = tk.Button(window, text="Сгенерировать ключ", command=click_button)
btn.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
window.mainloop()
