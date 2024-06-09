import sqlite3
from tkinter import messagebox

# Função para conectar ao banco de dados e criar a tabela se ela não existir
def inicializar_banco():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# Função para cadastrar um novo usuário
def cadastrar_usuario(nome, email, senha):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
        INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)
        ''', (nome, email, senha))
        conn.commit()
        messagebox.showinfo(title="Cadastro", message="Usuário cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        messagebox.showerror(title="Erro", message="Email já cadastrado!")
    finally:
        conn.close()

# Função para verificar login
def verificar_login(email, senha):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
        SELECT * FROM usuarios WHERE email=? AND senha=?
        ''', (email, senha))
        usuario = cursor.fetchone()
        conn.close()
        if usuario:
            return True
        else:
            return False
    except sqlite3.Error as e:
        messagebox.showerror(title="Erro", message=f"Erro ao verificar login: {e}")
        return False
    finally:
        conn.close()
