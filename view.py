# importando SQLite
import sqlite3 as lite

con = lite.connect('data.db')


# insert
def Insert(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO alunos (nome, email, telefone, birthday, turma, nota) VALUES ( ?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)

# Read
def Read():
    with con:
        roll = []
        cur = con.cursor()
        query = "SELECT * FROM alunos "
        cur.execute(query)
        info = cur.fetchall()

        for i in info:
            roll.append(i)
    return roll


# Update
def Update(i):
    with con:
        cur = con.cursor()
        query = "UPDATE  alunos  SET nome=?, email=?, telefone=?, birthday=?, turma=?, nota=? WHERE id=?"
        cur.execute(query,i)

# Delete
def Delete(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM alunos WHERE id=?"
        cur.execute(query,i)