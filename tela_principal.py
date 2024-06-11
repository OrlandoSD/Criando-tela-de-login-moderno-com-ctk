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
        
        pesquisar_radio_button = ctk.CTkButton(master=self.janela, text="Pesquisar Rádio", width=200, command=self.janela_pesquisar_radio)
        pesquisar_radio_button.pack(pady=10)


        # Treeview para exibir resultados de pesquisa
        self.treeview_pesquisa = ttk.Treeview(self.janela, columns=("Nome", "Serial", "Local", "Status"))
        self.treeview_pesquisa.heading("#0", text="ID")
        self.treeview_pesquisa.heading("Nome", text="Nome")
        self.treeview_pesquisa.heading("Serial", text="Serial")
        self.treeview_pesquisa.heading("Local", text="Local")
        self.treeview_pesquisa.heading("Status", text="Status")

        def mostrar_tabela_pesquisa(self):
            # Limpar tabela antes de preencher com novos resultados
            self.treeview_pesquisa.delete(*self.treeview_pesquisa.get_children())

            # Preencher a tabela com os resultados da pesquisa
            conn = sqlite3.connect('Sistema.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM radios')
            for row in cursor.fetchall():
                self.treeview_pesquisa.insert('', 'end', text=row[0], values=(row[1], row[2], row[3], row[4]))
            conn.close()

            # Mostrar a tabela na tela principal
            self.treeview_pesquisa.pack(pady=10, fill=tk.BOTH, expand=True)

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
                conn = sqlite3.connect('Sistema.db')
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

    def mostrar_frame_pesquisa(self):
        # Limpar a Treeview antes de preencher com novos resultados
        self.treeview_pesquisa.delete(*self.treeview_pesquisa.get_children())
        
        # Preencher a Treeview com os resultados da pesquisa
        conn = sqlite3.connect('Sistema.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM radios')
        for row in cursor.fetchall():
            self.treeview_pesquisa.insert('', 'end', text=row[0], values=(row[1], row[2], row[3], row[4]))
        conn.close()
        
        self.frame_cadastro.pack_forget()
        self.frame_pesquisa.pack(fill=ctk.BOTH, expand=true)
        self.frame_pesquisa.update()
        self.janela_pesquisar_radio()

    def janela_pesquisar_radio(self):
        pesquisar_radio_janela = ctk.CTkToplevel(self.janela)
        pesquisar_radio_janela.geometry("400x470")
        pesquisar_radio_janela.title("Pesquisar Rádio")

        title_label = ctk.CTkLabel(master=pesquisar_radio_janela, text="Pesquisar Rádio", font=("Roboto", 18), text_color="white")
        title_label.pack(pady=20)

        self.serial_pesquisa_entry = ctk.CTkEntry(master=pesquisar_radio_janela, placeholder_text="Serial do Rádio", width=300, font=("Roboto", 14))
        self.serial_pesquisa_entry.pack(pady=5)

        def search_radio():
            serial_pesquisa = self.serial_pesquisa_entry.get()
            if serial_pesquisa:
                conn = sqlite3.connect('Sistema.db')
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT * FROM radios WHERE serialRadio=?
                ''', (serial_pesquisa,))
                radio = cursor.fetchone()
                conn.close()
                if radio:
                    resultado_label = ctk.CTkLabel(master=pesquisar_radio_janela, text=f"Nome: {radio[1]}\nSerial: {radio[2]}\nLocal: {radio[3]}\nStatus: {radio[4]}", font=("Roboto", 14), text_color="white")
                    resultado_label.pack(pady=10)
                    
                    editar_button = ctk.CTkButton(master=pesquisar_radio_janela, text="Editar", width=100, command=lambda: self.janela_editar_radio(radio[0]))
                    editar_button.pack(pady=5)
                    
                    excluir_button = ctk.CTkButton(master=pesquisar_radio_janela, text="Excluir", width=100, command=lambda: self.excluir_radio(radio[0], pesquisar_radio_janela))
                    excluir_button.pack(pady=5)
                    
                else:
                    messagebox.showerror(title="Erro", message="Rádio não encontrado!")
            else:
                messagebox.showerror(title="Erro", message="Preencha o campo de serial!")

        pesquisar_button = ctk.CTkButton(master=pesquisar_radio_janela, text="Pesquisar", width=200, command=search_radio)
        pesquisar_button.pack(pady=10)

    def janela_editar_radio(self, radio_id):
        editar_radio_janela = ctk.CTkToplevel(self.janela)
        editar_radio_janela.geometry("400x300")
        editar_radio_janela.title("Editar Rádio")

        conn = sqlite3.connect('Sistema.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM radios WHERE id=?
        ''', (radio_id,))
        radio = cursor.fetchone()
        conn.close()

        title_label = ctk.CTkLabel(master=editar_radio_janela, text="Editar Rádio", font=("Roboto", 18), text_color="white")
        title_label.pack(pady=20)

        self.nome_radio_entry = ctk.CTkEntry(master=editar_radio_janela, placeholder_text="Nome do Rádio", width=300, font=("Roboto", 14))
        self.nome_radio_entry.insert(0, radio[1])
        self.nome_radio_entry.pack(pady=5)

        self.serial_radio_entry = ctk.CTkEntry(master=editar_radio_janela, placeholder_text="Serial do Rádio", width=300, font=("Roboto", 14))
        self.serial_radio_entry.insert(0, radio[2])
        self.serial_radio_entry.pack(pady=5)

        self.local_radio_entry = ctk.CTkEntry(master=editar_radio_janela, placeholder_text="Local do Rádio", width=300, font=("Roboto", 14))
        self.local_radio_entry.insert(0, radio[3])
        self.local_radio_entry.pack(pady=5)

        self.status_radio_entry = ctk.CTkEntry(master=editar_radio_janela, placeholder_text="Status do Rádio", width=300, font=("Roboto", 14))
        self.status_radio_entry.insert(0, radio[4])
        self.status_radio_entry.pack(pady=5)

        def update_radio():
            nome_radio = self.nome_radio_entry.get()
            serial_radio = self.serial_radio_entry.get()
            local_radio = self.local_radio_entry.get()
            status_radio = self.status_radio_entry.get()

            if nome_radio and serial_radio and local_radio and status_radio:
                conn = sqlite3.connect('Sistema.db')
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE radios SET nomeRadio=?, serialRadio=?, localRadio=?, status=? WHERE id=?
                ''', (nome_radio, serial_radio, local_radio, status_radio, radio_id))
                conn.commit()
                conn.close()
                messagebox.showinfo(title="Atualização", message="Rádio atualizado com sucesso!")
                editar_radio_janela.destroy()
            else:
                messagebox.showerror(title="Erro", message="Preencha todos os campos!")

        salvar_button = ctk.CTkButton(master=editar_radio_janela, text="Salvar", width=200, command=update_radio)
        salvar_button.pack(pady=10)

    def excluir_radio(self, radio_id, janela):
        conn = sqlite3.connect('Sistema.db')
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM radios WHERE id=?
        ''', (radio_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo(title="Exclusão", message="Rádio excluído com sucesso!")
        janela.destroy()

# Executar apenas se este arquivo for o principal
if __name__ == "__main__":
    Application()
