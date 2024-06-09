from tkinter import PhotoImage, RIGHT
from turtle import right
import customtkinter


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("700x400")
janela.title("Sistema de login")
janela.iconbitmap("icon.ico")
janela.resizable(False, False)


img = PhotoImage(file="login.png")
label_img = customtkinter.CTkLabel(master=janela, image=img)
label_img.place(x=25, y=65)

label_tt = customtkinter.CTkLabel(master=janela, text="Entrar com seu login e senha", font=("Roboto", 18), text_color="white")
label_tt.place(x=60, y=10)

frame = customtkinter.CTkFrame(master=janela, width=350, height=396)
frame.pack(side=RIGHT)

label = customtkinter.CTkLabel(master=frame, text="Sistema de Login", font=("Roboto", 20))
label.place(x=35, y=5)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Nome de usuário", width=300, font=("Roboto", 14))
entry1.place(x=25, y=105)

label1 = customtkinter.CTkLabel(master=frame, text="O campo usuário é de caráter obrigatório!", text_color="green", font=("Roboto", 12))
label1.place(x=25, y=135)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Senha de usuário", width=300, font=("Roboto", 14))
entry2.place(x=25, y=175)

label2 = customtkinter.CTkLabel(master=frame, text="O campo Senha é de caráter obrigatório!", text_color="green", font=("Roboto", 12))
label2.place(x=25, y=205)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Lembrar-se do login sempre").place(x=25, y=235)

button = customtkinter.CTkButton(master=frame, text="LOGIN", width=300).place(x=25, y=285)

janela.mainloop()