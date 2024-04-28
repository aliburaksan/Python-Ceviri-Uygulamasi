### Designed by SHiROU     ###
##  LinkedIn:aliburaksan45 ##
#   YouTube MP3 Indirici   #

import customtkinter
from tkinter import *
import googletrans
from googletrans import Translator


# Uygulama
app = customtkinter.CTk()
app.geometry("1065x410+400+300")
app.title("Çeviri Programı")
app.resizable(width=False, height=False)


# Uygulama Teması
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


# Uygulama Başlık
title = customtkinter.CTkLabel(app, text="Çeviri Programı", font=customtkinter.CTkFont(family='Arial', size=20, weight='bold', slant='italic'))
title.pack(padx=10, pady=10)


def label_change():
    c1 = combo1.get()
    c2 = combo2.get()

    label1.configure(text=c1)
    label2.configure(text=c2)
    app.after(1000, label_change)


# Çeviri işlemini gerçekleştirir
def translate_now():
    text = text1.get(1.0, customtkinter.END)
    t1 = Translator()
    trans_text = t1.translate(text, src=combo1.get(), dest=combo2.get())
    trans_text = trans_text.text
    text2.delete(1.0, customtkinter.END)
    text2.insert(customtkinter.END, trans_text)


# Pencere içeriğini temizler
def clear_button():
    text1.delete(1.0, customtkinter.END)
    text2.delete(1.0, customtkinter.END)



languages = googletrans.LANGUAGES
languageV = list(languages.values())


combo1 = customtkinter.CTkComboBox(app, values=languageV)
combo1.place(x=150, y=20)
combo1.set('English')


label1 = customtkinter.CTkLabel(app, text='Turkish')
label1.place(x=155, y=60)


label3 = customtkinter.CTkLabel(app, text='Seçilen Dil: ')
label3.place(x=86, y=60)


label4 = customtkinter.CTkLabel(app, text='Çevirilecek Dil: ')
label4.place(x=668, y=60)


f1 = customtkinter.CTkFrame(app, width=440, height=210, border_width=3)
f1.place(x=10, y=118)


text1 = customtkinter.CTkTextbox(f1, wrap=WORD, width=220, height=210, border_width=2)
text1.place(x=0, y=0)


combo2 = customtkinter.CTkComboBox(app, values=languageV)
combo2.place(x=750, y=20)
combo2.set('Turkish')


label2 = customtkinter.CTkLabel(app, text='English')
label2.place(x=755, y=60)


f2 = customtkinter.CTkFrame(app, width=440, height=210, border_width=3)
f2.place(x=620, y=118)


text2 = customtkinter.CTkTextbox(f2, wrap=WORD, width=220, height=210, border_width=2)
text2.place(x=0, y=0)


translate_button = customtkinter.CTkButton(app, text='Çevir', font=customtkinter.CTkFont(weight='bold', size=14),command=translate_now)
translate_button.place(x=465, y=170)

clear_button = customtkinter.CTkButton(app, text='Temizle', font=customtkinter.CTkFont(weight='bold', size=14),command=clear_button)
clear_button.place(x=465, y=250)

label_change()
app.mainloop()