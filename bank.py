# importando SQLite
import sqlite3 as lite

# Criando o banco de dados
con = lite.connect('data.db')

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE alunos(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, telefone TEXT, birthday DATE, turma TEXT, nota INTEGER)")
