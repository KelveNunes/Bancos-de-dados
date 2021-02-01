# removendo banco caso ele exista
import os

os.remove('bda.db') if os.path.exists('pythonProject\Tabelas.py') else None

# importando, conectando e criando o cursor do banco
import sqlite3

conn = sqlite3.connect('bda.db')
curs = conn.cursor()


# criando função para criar uma tabela
def create_table():
    curs.execute('CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, ' \
                 'prod_name TEXT, valor REAL)')


# criando função para inserir na tabela
def insert_row():
    curs.execute("INSERT INTO produtos VALUES(10, '2020-05-02 14:32:11', 'Teclado', 90 )")
    conn.commit()
    curs.close()
    conn.close()


# chamando as funções

create_table()


import time
import datetime
import random


# usando variaveis para inserir dados

def data_insert_var():
    new_date = datetime.datetime.now()
    new_product_name = 'monitor'
    new_valor = random.randrange(50, 100)
    curs.execute("INSERT INTO produtos (date, prod_name, valor) VALUES (?, ?, ?)", (new_date, new_product_name, new_valor))
    conn.commit()


data_insert_var()

#for i in range(10):
    #data_insert_var()
    #time.sleep(1)




# Leitura de dados
def leitura_todos_dados():
    curs.execute("SELECT * FROM PRODUTOS")
    for linha in curs.fetchall():
        print(linha)


# Leitura de registros específicos
def leitura_registros():
    curs.execute("SELECT * FROM PRODUTOS WHERE valor > 60.0")
    for linha in curs.fetchall():
        print(linha)

# Leitura de colunas específicos


def leitura_colunas():
    curs.execute("SELECT * FROM PRODUTOS")
    for linha in curs.fetchall():
        print(linha[3])

#update
def atualiza_dados():
    curs.execute('UPDATE produtos SET valor = 70 WHERE valor = 80')
    conn.commit()

def delete_dados():
    curs.execute('DELETE FROM produtos WHERE valor = 60')
    conn.commit()

atualiza_dados()
delete_dados()
curs.close()
conn.close()