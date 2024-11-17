import sqlite3

def criar_banco_de_dados():
    conn = sqlite3.connect('colaboradores.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS colaboradores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            foto_ref TEXT NOT NULL
        )''')
    conn.commit()
    conn.close()

def cadastrar_colaborador(nome, email, foto_ref):
    conn = sqlite3.connect('colaboradores.db')
    c = conn.cursor()
    c.execute("INSERT INTO colaboradores (nome, email, foto_ref) VALUES (?, ?, ?)",
              (nome, email, foto_ref))
    conn.commit()
    conn.close()