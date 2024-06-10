import customtkinter as ctk
from tkinter import messagebox
import database

class Application():
    def __init__(self):
        self.janela = ctk.CTk()
        self.tema()
        self.tela()
        self.janela_principal()
        self.janela.mainloop()

    def tema(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def tela(self):
        self.janela.geometry("800x600")
        self.janela.title("Sistema Principal")
        self.janela.resizable(False, False)

    def janela_principal(self):
        title_label = ctk.CTkLabel(master=self.janela, text="Bem-vindo ao Sistema Principal", font=("Roboto", 18), text_color="white")
        title_label.pack(pady=20)

        cadastrar_radio_button = ctk.CTkButton(master=self.janela, text="Cadastrar Rádio", width=200, command=self.janela_cadastrar_radio)
        cadastrar_radio_button.pack(pady=10)

    def janela_cadastrar_radio(self):
        cadastrar_radio_janela = ctk.CTkToplevel(self.janela)
        cadastrar_radio_janela.geometry("400x300")
        cadastrar_radio_janela.title("Cadastrar Rádio")

        title_label = ctk.CTkLabel(master=cadastrar_radio_janela, text="Cadastro de Rádio", font=("Roboto", 18), text_color="white")
        title_label.pack(pady=20)

        self.nome_radio_entry = ctk.CTkEntry(master=cadastrar_radio_janela, placeholder_text="Nome do Rádio", width=300, font=("Roboto", 14))
        self.nome_radio_entry.pack(pady=5)

        self.serial_radio_entry = ctk.CTkEntry(master=cadastrar_radio_janela, placeholder_text="Serial do Rádio", width=300, font=("Roboto", 14))
        self.serial_radio_entry.pack(pady=5)

        self.local_radio_entry = ctk.CTkEntry(master=cadastrar_radio_janela, placeholder_text="Local do Rádio", width=300, font=("Roboto", 14))
        self.local_radio_entry.pack(pady=5)

        self.status_radio_entry = ctk.CTkEntry(master=cadastrar_radio_janela, placeholder_text="Status do Rádio", width=300, font=("Roboto", 14))
        self.status_radio_entry.pack(pady=5)

        def save_radio():
            nome_radio = self.nome_radio_entry.get()
            serial_radio = self.serial_radio_entry.get()
            local_radio = self.local_radio_entry.get()
            status_radio = self.status_radio_entry.get()

            if nome_radio and serial_radio and local_radio and status_radio:
                # Salvando no banco de dados
                conn = sqlite3.connect('usuarios.db')
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO radios (nomeRadio, serialRadio, localRadio, status)
                    VALUES (?, ?, ?, ?)
                ''', (nome_radio, serial_radio, local_radio, status_radio))
                conn.commit()
                conn.close()
                messagebox.showinfo(title="Cadastro", message="Rádio cadastrado com sucesso!")
                cadastrar_radio_janela.destroy()
            else:
                messagebox.showerror(title="Erro", message="Preencha todos os campos!")

        salvar_button = ctk.CTkButton(master=cadastrar_radio_janela, text="Salvar", width=200, command=save_radio)
        salvar_button.pack(pady=10)

# Executar apenas se este arquivo for o principal
if __name__ == "__main__":
    Application()

