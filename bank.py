# importando SQLite
import sqlite3 as lite

# Criando o banco de dados
con = lite.connect('data.db')

with con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS alunos(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, email TEXT NOT NULL, telefone TEXT, birthday DATE NOT NULL, turma TEXT NOT NULL, nota INTEGER NOT NULL)''')
    con.commit()
