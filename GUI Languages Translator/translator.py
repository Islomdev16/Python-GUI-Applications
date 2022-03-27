from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from googletrans import Translator

root = Tk()
root.title("🌐 Google Translator")
root.geometry("1250x650")
root.resizable(False, False)
root.configure(background="white")

def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000, label_change)

def translate_now():
    text_ = text1.get(1.0, END)
    t1 = Translator()
    trans_text = t1.translate(text_, src=combo1.get(), dest=combo2.get())
    trans_text = trans_text.text

    text2.delete(1.0, END)
    text2.insert(END, trans_text)

# icon section
image_icon = PhotoImage(file="google.png")
root.iconphoto(False, image_icon)

# Arrow section
arrow_image = PhotoImage(file="arrow.png")
image_label = Label(root, image=arrow_image, width=150)
image_label.place(x=548, y=40)

language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()

# first combobox section
combo1 = ttk.Combobox(root, values=languageV, font=("Roboto", 14), state="r")
combo1.place(x=143, y=30)
combo1.set("SELECT LANGUAGE")

label1 = Label(root, text="ENGLISH", font=("segoe", 30, "bold"), bg="white", width=18, bd=5, fg="#31ADB9", relief=GROOVE)
label1.place(x=15, y=60)

# second combobox section
combo2 = ttk.Combobox(root, values=languageV, font=("Roboto", 14), state="r")
combo2.place(x=850, y=30)
combo2.set("SELECT LANGUAGE")

label2 = Label(root, text="ENGLISH", font=("segoe", 30, "bold"), bg="white", width=18, bd=5, fg="#31ADB9", relief=GROOVE)
label2.place(x=720, y=60)

# first frame section
f = Frame(root, bg="black", bd=5, relief=RIDGE)
f.place(x=21, y=130, width=500, height=460)

text1 = Text(f, font=("Roboto", 20), bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=475, height=450)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# second frame section
f1 = Frame(root, bg="black", bd=5, relief=RIDGE)
f1.place(x=727, y=130, width=500, height=460)

text2 = Text(f1, font=("Roboto", 20), bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=475, height=450)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right", fill="y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# translate button section
translate = Button(root, text="TRANSLATE", font=("Roboto", 15), activebackground="#31ADB9", cursor="hand2", bd=5, width=10, height=2, bg="#31ADB9", fg="white", command=translate_now)
translate.place(x=541, y=250)

label_change()

root.mainloop()
