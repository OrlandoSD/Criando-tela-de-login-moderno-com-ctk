import customtkinter as ctk
from tkinter import messagebox
import sqlite3
import tkinter as tk
from tkinter import ttk

class Application:
    def __init__(self):
        self.janela = ctk.CTk()
        self.tema()
        self.tela()
        self.treeview_pesquisa = None  # Initialize treeview for search results
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
        
        pesquisar_radio_button = ctk.CTkButton(master=self.janela, text="Pesquisar Rádio", width=200, command=self.mostrar_frame_pesquisa)
        pesquisar_radio_button.pack(pady=10)

    def janela_cadastrar_radio(self):
        cadastrar_radio_janela = ctk.CTkToplevel(self.janela)
        cadastrar_radio_janela.geometry("400x300")
        cadastrar_radio_janela.title("Cadastrar Rádio")
        cadastrar_radio_janela.grab_set()  # Garante que esta janela esteja na frente da tela principal

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

        self.observacoes_entry = ctk.CTkEntry(master=cadastrar_radio_janela, placeholder_text="Observações", width=300, font=("Roboto", 14))
        self.observacoes_entry.pack(pady=5)

    def save_radio():
        nome_radio = self.nome_radio_entry.get()
        serial_radio = self.serial_radio_entry.get()
        local_radio = self.local_radio_entry.get()
        status_radio = self.status_radio_entry.get()
        observacoes = self.observacoes_entry.get()  # Adicione esta linha para obter as observações

        if nome_radio and serial_radio and local_radio and status_radio and observacoes:  # Correção aqui
            conn = sqlite3.connect('Sistema.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO radios (nomeRadio, serialRadio, localRadio, status, observacoes)
                VALUES (?, ?, ?, ?, ?)
            ''', (nome_radio, serial_radio, local_radio, status_radio, observacoes))
            conn.commit()
            conn.close()
            messagebox.showinfo(title="Cadastro", message="Rádio cadastrado com sucesso!")
            cadastrar_radio_janela.destroy()
        else:
            messagebox.showerror(title="Erro", message="Preencha todos os campos!")



    def mostrar_frame_pesquisa(self):
        if self.treeview_pesquisa is None:
            # Treeview for displaying search results
            self.treeview_pesquisa = ttk.Treeview(self.janela, columns=("Nome", "Serial", "Local", "Status", "Observacoes"))
            self.treeview_pesquisa.heading("#0", text="ID")
            self.treeview_pesquisa.heading("Nome", text="Nome")
            self.treeview_pesquisa.heading("Serial", text="Serial")
            self.treeview_pesquisa.heading("Local", text="Local")
            self.treeview_pesquisa.heading("Status", text="Status")
            self.treeview_pesquisa.heading("Observacoes", text="Observacoes")

        # Clear existing items in the treeview
        for child in self.treeview_pesquisa.get_children():
            self.treeview_pesquisa.delete(child)

        # Fetch data from database and populate the treeview
        conn = sqlite3.connect('Sistema.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM radios')
        for row in cursor.fetchall():
            self.treeview_pesquisa.insert('', 'end', text=row[0], values=(row[1], row[2], row[3], row[4], row[5]))
        conn.close()

        # Display the treeview in the main window
        self.treeview_pesquisa.pack(pady=10, fill=tk.BOTH, expand=True)

        # Bind double-click event to open radio details
        self.treeview_pesquisa.bind("<Double-1>", self.on_treeview_double_click)

        # Button to show all radios
        show_all_button = ctk.CTkButton(master=self.janela, text="Mostrar Todos os Rádios", width=200, command=self.mostrar_todos_os_radios)
        show_all_button.pack(pady=10)

    def mostrar_todos_os_radios(self):
        # Clear existing items in the treeview
        for child in self.treeview_pesquisa.get_children():
            self.treeview_pesquisa.delete(child)

        # Fetch all data from database and populate the treeview
        conn = sqlite3.connect('Sistema.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM radios')
        for row in cursor.fetchall():
            self.treeview_pesquisa.insert('', 'end', text=row[0], values=(row[1], row[2], row[3], row[4], row[5]))
        conn.close()

    def on_treeview_double_click(self, event):
        item = self.treeview_pesquisa.selection()[0]
        radio_id = self.treeview_pesquisa.item(item, "text")
        self.abrir_detalhes_radio(radio_id)

    def abrir_detalhes_radio(self, radio_id):
        detalhes_radio_janela = ctk.CTkToplevel(self.janela)
        detalhes_radio_janela.geometry("400x300")
        detalhes_radio_janela.title("Detalhes do Rádio")
        detalhes_radio_janela.grab_set()

        conn = sqlite3.connect('Sistema.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM radios WHERE id=?', (radio_id,))
        radio = cursor.fetchone()
        conn.close()

        title_label = ctk.CTkLabel(master=detalhes_radio_janela, text="Detalhes do Rádio", font=("Roboto", 18), text_color="white")
        title_label.pack(pady=20)

        nome_label = ctk.CTkLabel(master=detalhes_radio_janela, text=f"Nome: {radio[1]}", font=("Roboto", 14), text_color="white")
        nome_label.pack(pady=5)

        serial_label = ctk.CTkLabel(master=detalhes_radio_janela, text=f"Serial: {radio[2]}", font=("Roboto", 14), text_color="white")
        serial_label.pack(pady=5)

        local_label = ctk.CTkLabel(master=detalhes_radio_janela, text=f"Local: {radio[3]}", font=("Roboto", 14), text_color="white")
        local_label.pack(pady=5)

        status_label = ctk.CTkLabel(master=detalhes_radio_janela, text=f"Status: {radio[4]}", font=("Roboto", 14), text_color="white")
        status_label.pack(pady=5)

        observacoes_label = ctk.CTkLabel(master=detalhes_radio_janela, text="Observações:", font=("Roboto", 14), text_color="white")
        observacoes_label.pack(pady=10)

        observacoes_entry = ctk.CTkEntry(master=detalhes_radio_janela, placeholder_text="Observações", width=300, font=("Roboto", 14))
        observacoes_entry.insert(0, radio[5] if radio[5] else "")
        observacoes_entry.pack(pady=10)

        def salvar_observacoes():
            observacoes = observacoes_entry.get()
            conn = sqlite3.connect('Sistema.db')
            cursor = conn.cursor()
            cursor.execute('UPDATE radios SET observacoes=? WHERE id=?', (observacoes, radio_id))
            conn.commit()
            conn.close()
            messagebox.showinfo(title="Salvo", message="Observações salvas com sucesso!")
            detalhes_radio_janela.destroy()

        salvar_button = ctk.CTkButton(master=detalhes_radio_janela, text="Salvar", width=200, command=salvar_observacoes)
        salvar_button.pack(pady=10)

if __name__ == "__main__":
    app = Application()
