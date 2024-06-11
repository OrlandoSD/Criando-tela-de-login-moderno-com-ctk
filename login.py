from tkinter import PhotoImage, RIGHT
from tkinter import messagebox
import customtkinter as ctk
import database  # Importando o arquivo database
import tela_principal  # Importando o arquivo da tela principal

# Inicializar o banco de dados ao iniciar a aplicação
database.inicializar_banco()

janela = ctk.CTk()

class Application():
    def __init__(self):
        self.janela = janela
        self.tema()
        self.tela()
        self.janela_login()
        janela.mainloop()

    def tema(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def tela(self):
        self.janela.geometry("700x400")
        self.janela.title("Sistema de login")
        self.janela.iconbitmap("login.ico")
        self.janela.resizable(False, False)

    def janela_login(self):
        # Trabalhando com a imagem da tela
        img = PhotoImage(file="login.png")
        label_img = ctk.CTkLabel(master=janela, image=img, text=None)
        label_img.place(x=25, y=65)

        title_label = ctk.CTkLabel(master=janela, text="Entrar com seu login e senha", font=("Roboto", 18), text_color="white")
        title_label.place(x=60, y=10)

        # Frame de login
        login_frame = ctk.CTkFrame(master=janela, width=350, height=396)
        login_frame.pack(side=RIGHT)

        # Widgets dentro da frame de tela de login
        label = ctk.CTkLabel(master=login_frame, text="Sistema de Login", font=("Roboto", 20))
        label.place(x=35, y=5)

        self.username_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Nome de usuário", width=300, font=("Roboto", 14))
        self.username_entry.place(x=25, y=105)

        username_label = ctk.CTkLabel(master=login_frame, text="O campo usuário é de caráter obrigatório!", text_color="green", font=("Roboto", 12))
        username_label.place(x=25, y=135)

        self.password_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Senha de usuário", width=300, font=("Roboto", 14), show="*")
        self.password_entry.place(x=25, y=175)

        password_label = ctk.CTkLabel(master=login_frame, text="O campo Senha é de caráter obrigatório!", text_color="green", font=("Roboto", 12))
        password_label.place(x=25, y=205)

        checkbox = ctk.CTkCheckBox(master=login_frame, text="Lembrar-se do login sempre").place(x=25, y=235)

        def login():
            email = self.username_entry.get()
            senha = self.password_entry.get()
            try:
                if database.verificar_login(email, senha):
                    messagebox.showinfo(title="Login", message="Login efetuado com sucesso!")
                    self.janela.destroy()
                    tela_principal.Application()
                else:
                    messagebox.showerror(title="Erro", message="Email ou senha incorretos!")
            except Exception as e:
                messagebox.showerror(title="Erro", message=f"Erro ao verificar login: {e}")

        login_button = ctk.CTkButton(master=login_frame, text="LOGIN", width=300, command=login).place(x=25, y=285)

        def tela_register():
            # Remover o frame de login
            login_frame.pack_forget()

            # Criando a tela de cadastro de usuários
            rg_frame = ctk.CTkFrame(master=janela, width=350, height=396)
            rg_frame.pack(side=RIGHT)

            label = ctk.CTkLabel(master=rg_frame, text="Faça seu Cadastro", font=("Roboto", 20))
            label.place(x=35, y=5)

            span = ctk.CTkLabel(master=rg_frame, text="Por favor preencha todos os Campos corretamente", font=("Roboto", 11), text_color="gray")
            span.place(x=25, y=25)

            self.reg_username_entry = ctk.CTkEntry(master=rg_frame, placeholder_text="Nome de usuário", width=300, font=("Roboto", 14))
            self.reg_username_entry.place(x=25, y=105)

            self.reg_email_entry = ctk.CTkEntry(master=rg_frame, placeholder_text="E-mail de usuário", width=300, font=("Roboto", 14))
            self.reg_email_entry.place(x=25, y=145)

            self.reg_password_entry = ctk.CTkEntry(master=rg_frame, placeholder_text="Senha de usuário", width=300, font=("Roboto", 14), show="*")
            self.reg_password_entry.place(x=25, y=185)

            self.reg_cPassword_entry = ctk.CTkEntry(master=rg_frame, placeholder_text="Confirme a Senha", width=300, font=("Roboto", 14), show="*")
            self.reg_cPassword_entry.place(x=25, y=225)

            checkbox = ctk.CTkCheckBox(master=rg_frame, text="Aceito os Termos e Politicas").place(x=25, y=270)

            def back():
                # Removendo o frame de cadastro
                rg_frame.pack_forget()
                # Retornando ao frame de login
                login_frame.pack(side=RIGHT)

            back_button = ctk.CTkButton(master=rg_frame, text="VOLTAR", width=145, fg_color="gray", hover_color="#000080", command=back).place(x=25, y=315)

            def save_user():
                nome = self.reg_username_entry.get()
                email = self.reg_email_entry.get()
                senha = self.reg_password_entry.get()
                csenha = self.reg_cPassword_entry.get()

                if senha == csenha:
                    try:
                        database.cadastrar_usuario(nome, email, senha)
                        messagebox.showinfo(title="Sucesso", message="Usuário cadastrado com sucesso!")
                    except Exception as e:
                        messagebox.showerror(title="Erro", message=f"Erro ao cadastrar usuário: {e}")
                else:
                    messagebox.showerror(title="Erro", message="As senhas não coincidem!")

            save_button = ctk.CTkButton(master=rg_frame, text="CADASTRAR", width=145, fg_color="green", hover_color="#014B05", command=save_user).place(x=180, y=315)

        register_span = ctk.CTkLabel(master=login_frame, text="se não tem uma conta").place(x=25, y=325)
        register_button = ctk.CTkButton(master=login_frame, text="Cadastre-se", width=150, fg_color="green", hover_color="#2D9334", command=tela_register).place(x=175, y=325)

if __name__ == "__main__":
    database.inicializar_banco()
    app = Application()
