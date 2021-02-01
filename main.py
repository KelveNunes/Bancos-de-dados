#removendo arquivos do BD.
import os

os.remove('escola.db') if os.path.exists('escola.db') else None

#importando modo de acesso ao SQlite.
import sqlite3

#cria a conexão com o BD.
conexao = sqlite3.connect('escola.db')
print(type(conexao))

#criando cursor
curs = conexao.cursor()
print(type(curs))

#criando uma instrução SQL
sql_create = sql_create = 'create table cursos '\
'(id integer primary key, '\
'titulo varchar(100), '\
'categoria varchar(140))'

print(sql_create)

#executa a instrução SQL no cursor
curs.execute(sql_create)

# Criando outra sentença SQL para inserir registros
sql_insert = 'insert into cursos values'

# Dados
setdata = [(1000, 'Ciência de Dados', 'Data Science'),
           (1001, 'Big Data Fundamentos', 'Big Data'),
           (1002, 'Python Fundamentos', 'Análise de Dados')]

# Inserindo os registros
for setd in setdata:
    curs.execute(sql_insert, setd)

# Grava a transação
conexao.commit()

# Criando outra sentença SQL para selecionar registros
sql_select = 'select * from cursos'

# Seleciona todos os registros e recupera os registros
curs.execute(sql_select)
dados = curs.fetchall()

# Mostra os dados
#for row in dados:
    #print('Id: %d, Titulo: %s, Categoria: %s \n' %row)

# Gerando outros registros
setdata = [(1003, 'Gestão de Dados com MongoDB', 'Big Data'),
          (1004, 'R Fundamentos', 'Análise de Dados')]

# Inserindo os registros
for setd in setdata:
    curs.execute(sql_insert, setd)

# Gravando a transação
conexao.commit()

# Seleciona todos os registros
curs.execute('select * from cursos')

# Recupera os resultados
setdata = curs.fetchall()

# Mostra
for rec in setdata:
    print('Curso Id: %d, Título: %s, Categoria: %s \n' % rec)

conexao.close()

