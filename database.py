import sqlite3

def inicializar_banco():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    # Criação da tabela de usuários
    c.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        senha TEXT NOT NULL
    )
    ''')
     # Create radios table if not exists
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS radios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nomeRadio TEXT NOT NULL,
        serialRadio TEXT NOT NULL,
        localRadio TEXT NOT NULL,
        status TEXT NOT NULL,
        observacoes TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def cadastrar_usuario(nome, email, senha):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)', (nome, email, senha))
    conn.commit()
    conn.close()

def verificar_login(email, senha):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM usuarios WHERE email=? AND senha=?', (email, senha))
    resultado = c.fetchone()
    conn.close()
    return resultado is not None
