import sqlite3
from tkinter import messagebox

# Função para conectar ao banco de dados e criar a tabela se ela não existir
def inicializar_banco():
   
    conn = sqlite3.connect('Sistema.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS radios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nomeRadio TEXT NOT NULL,
            serialRadio TEXT NOT NULL,
            localRadio TEXT NOT NULL,
            status TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    
def save_radio(nomeRadio, serialRadio, localRadio, status):
    conn = sqlite3.connect('Sistema.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO radios (nomeRadio, serialRadio, localRadio, status) VALUES (?, ?, ?, ?)", (nomeRadio, serialRadio, localRadio, status))
        conn.commit()
    except sqlite3.Error as e:
        print("Erro ao inserir rádio:", e)
    finally:
        conn.close()
        
# Função para cadastrar um novo usuário
def cadastrar_usuario(nome, email, senha, cSenha):
    conn = sqlite3.connect('Sistema.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
        INSERT INTO usuarios (nome, email, senha, cSenha) VALUES (?, ?, ?,?)
        ''', (nome, email, senha, cSenha))
        conn.commit()
        messagebox.showinfo(title="Cadastro", message="Usuário cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        messagebox.showerror(title="Erro", message="Email já cadastrado!")
    finally:
        conn.close()

# Função para verificar login
def verificar_login(nome, senha):
    conn = sqlite3.connect('Sistema.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
        SELECT * FROM usuarios WHERE nome=? AND senha=?
        ''', (nome, senha))
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
