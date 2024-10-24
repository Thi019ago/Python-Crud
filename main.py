from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry

from view import *

# cores
black = "#f0f3f5"  # Preta co0
white = "#feffff"  # branca co1
green = "#4fa882"  # verde co2
value = "#38576b"  # valor co3
letter = "#403d3d"   # letra co4
profit = "#e06636"   # - profit co5
blue = "#038cfc"   # azul co6
red = "#ef5350"   # vermelha co7
greenPlus = "#263238"   # + verde co8
skyBlue = "#e9edf5"   # sky blue co9

window = Tk()
window.title('')
window.geometry('1043x453')
window.configure(background=skyBlue)
window.resizable(width=FALSE, height=FALSE)

frame_title = Frame(window, width =310, height=50, bg=green, relief='flat')
frame_title.grid(row=0, column=0)

frame_input = Frame(window, width =310, height=403, bg=white, relief='flat')
frame_input.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_output = Frame(window, width =588, height=403, bg=white, relief='flat')
frame_output.grid(row=0, column=1, rowspan=2, padx=1,pady=0, sticky=NSEW)

app_name = Label(frame_title,text='Cadastro Alunos', anchor=NW, font=('Ivy 13 bold'), bg=green, fg=white, relief='flat')
app_name.place(x=10, y=20)

# variavel tree global
global tree

def insert_info():
    nome = e_name.get()
    email = e_email.get()
    tel = e_tel.get()
    birth = e_birth.get()
    team = e_class.get()
    grade = e_grade.get()

    data = [nome, email, tel, birth, team, grade]

    if data =='':
        messagebox.showerror('Erro', 'preencha todos os campos pro favor.')
    else:
        Insert(data)
        messagebox.showinfo('Sucesso', 'Aluno foi cadastrado com sucesso.')

        e_name.delete(0, 'end')
        e_email.delete(0, 'end')
        e_tel.delete(0, 'end')
        e_birth.delete(0, 'end')
        e_class.delete(0, 'end')
        e_grade.delete(0, 'end')
    
    for widget in frame_output.winfo_children():
        widget.destroy()

    Display()

def update_info():
    try:
        treev_data = tree.focus()
        treev_dicionario = tree.item(treev_data)
        tree_lista = treev_dicionario['values']

        valor_id = tree_lista[0]

        e_name.delete(0, 'end')
        e_email.delete(0, 'end')
        e_tel.delete(0, 'end')
        e_birth.delete(0, 'end')
        e_class.delete(0, 'end')
        e_grade.delete(0, 'end')

        e_name.insert(0, tree_lista[1])
        e_email.insert(0, tree_lista[2])
        e_tel.insert(0, tree_lista[3])
        e_birth.insert(0, tree_lista[4])
        e_class.insert(0, tree_lista[5])
        e_grade.insert(0, tree_lista[6])

        # Desabilitar o botão "Cadastrar" enquanto o "Confirmar" está ativo
        b_insert.place_forget()
        b_delete.place_forget()
        b_read.place_forget()
        b_update.place_forget()


        def update_insert():
            nome = e_name.get()
            email = e_email.get()
            tel = e_tel.get()
            birth = e_birth.get()
            team = e_class.get()
            grade = e_grade.get()

            data = [nome, email, tel, birth, team, grade, valor_id]

            if data == '':
                messagebox.showerror('Erro', 'Preencha todos os campos por favor.')
            else:
                Update(data)
                messagebox.showinfo('Sucesso', 'Os dados do(a) aluno(a) foram atualizados.')

                # Limpar os campos
                e_name.delete(0, 'end')
                e_email.delete(0, 'end')
                e_tel.delete(0, 'end')
                e_birth.delete(0, 'end')
                e_class.delete(0, 'end')
                e_grade.delete(0, 'end')

                # Atualizar a exibição da lista
                for widget in frame_output.winfo_children():
                    widget.destroy()

                Display()

                # Esconder os botões "Confirmar" e "Cancelar"
                b_confirm.place_forget()
                b_cancel.place_forget()

                # Reexibir os botões originais
                b_insert.place(x=15, y=330)
                b_update.place(x=105, y=330)
                b_delete.place(x=195, y=330)
                b_read.place(x=105, y=365)


        def cancel_update():
            # Esconder os botões "Confirmar" e "Cancelar"
            b_confirm.place_forget()
            b_cancel.place_forget()

            # Limpar os campos
            e_name.delete(0, 'end')
            e_email.delete(0, 'end')
            e_tel.delete(0, 'end')
            e_birth.delete(0, 'end')
            e_class.delete(0, 'end')
            e_grade.delete(0, 'end')

            # Reexibir os botões originais
            b_insert.place(x=15, y=330)
            b_update.place(x=105, y=330)
            b_delete.place(x=195, y=330)
            b_read.place(x=105, y=365)

        # Criar e exibir o botão de confirmar
        b_confirm = Button(frame_input, command=update_insert, text='Confirmar', width=10, font=('Ivy 9 bold'), bg=green, fg=white, relief='raised', overrelief='ridge')
        b_confirm.place(x=15, y=330)

        # Criar e exibir o botão de cancelar
        b_cancel = Button(frame_input, command=cancel_update, text='Cancelar', width=10, font=('Ivy 9 bold'), bg=red, fg=white, relief='raised', overrelief='ridge')
        b_cancel.place(x=195, y=330)

    except IndexError:
        messagebox.showerror('Erro', 'Por favor, selecione um dos dados da tabela.')


def delete_info():
    try:
        treev_data = tree.focus()
        treev_dicionario = tree.item(treev_data)
        tree_lista = treev_dicionario['values']

        valor_id = [tree_lista[0]]

        Delete(valor_id)

        messagebox.showinfo('Sucessos', 'Os dados do(a) aluno(a) foram deletados')

        for widget in frame_output.winfo_children():
            widget.destroy()
        
        Display()
    except IndexError:
        messagebox.showerror('Erro', 'Por favor selecione um dos dados da tabela.')

def read_info():
    try:
        treev_data = tree.focus()
        treev_dicionario = tree.item(treev_data)
        tree_lista = treev_dicionario['values']

        valor_id = tree_lista[0]

        e_name.delete(0, 'end')
        e_email.delete(0, 'end')
        e_tel.delete(0, 'end')
        e_birth.delete(0, 'end')
        e_class.delete(0, 'end')
        e_grade.delete(0, 'end')

        e_name.insert(0, tree_lista[1])
        e_email.insert(0, tree_lista[2])
        e_tel.insert(0, tree_lista[3])
        e_birth.insert(0, tree_lista[4])
        e_class.insert(0, tree_lista[5])
        e_grade.insert(0, tree_lista[6])

    except IndexError:
        messagebox.showerror('Erro', 'Por favor selecione um(a) aluno(a).')


l_name = Label(frame_input,text='Nome', anchor=NW, font=('Ivy 10 bold'), bg=white, fg=letter, relief='flat')
l_name.place(x=10, y=10)
e_name = Entry(frame_input, width=45, justify='left', relief='solid')
e_name.place(x=15, y=40)

l_email = Label(frame_input,text='Email', anchor=NW, font=('Ivy 10 bold'), bg=white, fg=letter, relief='flat')
l_email.place(x=10, y=70)
e_email = Entry(frame_input, width=45, justify='left', relief='solid')
e_email.place(x=15, y=100)

l_tel = Label(frame_input,text='Telefone', anchor=NW, font=('Ivy 10 bold'), bg=white, fg=letter, relief='flat')
l_tel.place(x=10, y=130)
e_tel = Entry(frame_input, width=45, justify='left', relief='solid')
e_tel.place(x=15, y=160)

l_birth = Label(frame_input,text='Data de Nascimento', anchor=NW, font=('Ivy 10 bold'), bg=white, fg=letter, relief='flat')
l_birth.place(x=15, y=190)
e_birth = DateEntry(frame_input, width=12, background='darkblue', foreground='white', borderwidth=2)
e_birth.place(x=15, y=220)

l_class = Label(frame_input,text='Turma', anchor=NW, font=('Ivy 10 bold'), bg=white, fg=letter, relief='flat',)
l_class.place(x=180, y=190)
e_class = Entry(frame_input, width=15, justify='left', relief='solid')
e_class.place(x=180, y=220)

l_grade = Label(frame_input,text='Nota', anchor=NW, font=('Ivy 10 bold'), bg=white, fg=letter, relief='flat')
l_grade.place(x=15, y=260)
e_grade = Entry(frame_input, width=20, justify='left', relief='solid')
e_grade.place(x=15, y=290)

# botoes CRUD
b_insert = Button(frame_input, command=insert_info,  text='Cadastrar', width=10, font=('Ivy 9 bold'), bg=blue, fg=white, relief='raised', overrelief='ridge')
b_insert.place(x=15, y=330)

b_update = Button(frame_input, command=update_info, text='Atualizar', width=10, font=('Ivy 9 bold'), bg=green, fg=white, relief='raised', overrelief='ridge')
b_update.place(x=105, y=330)

b_delete = Button(frame_input, command=delete_info, text='Deletar', width=10, font=('Ivy 9 bold'), bg=red, fg=white, relief='raised', overrelief='ridge')
b_delete.place(x=195, y=330)

b_read = Button(frame_input, command=read_info, text='Consultar', width=10, font=('Ivy 9 bold'), bg=greenPlus, fg=white, relief='raised', overrelief='ridge')
b_read.place(x=105, y=365)

#Frame Output
def Display():

    global tree

    lista = Read()

    list_header = ['ID', 'Nome', 'Email', 'Telefone', 'Data de Nascimento', 'Turma', 'Nota']

    tree = ttk.Treeview(frame_output, selectmode="extended",
                        columns=list_header, show="headings")
    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_output, orient="vertical", command=tree.yview)

    tree.configure(yscrollcommand=vsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')

    frame_output.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","nw","center","center","center"]
    h=[30,170,140,100,120,50,100]
    n=0

    for col in list_header:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n], anchor=hd[n])

        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)

Display()

window.mainloop()
