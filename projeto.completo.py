from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import PostgreSQL
import MySQL
from Lojas import Lojas
from Caracteristicas import Caracteristica
from Produto import Produto
from login import login
from DML import DML

L = Lojas(0, 0, 0, 0, 0)
C = Caracteristica(0, 0, 0, 0, 0)
P = Produto(0, 0, 0, 0)
l = login(0, 0)
D = DML(0, 0)


def SGBD():
    tela_2.show()
    tela.close()
    tela_3.close()
    tela_4.close()
    tela_5.close()
    tela_6.close()
    tela_7.close()
    tela_9.close()
    tela_4.label_4.setText(" ")
    tela_3.label_4.setText(" ")


def m_MySQL():
    try:
        con = MySQL.Connection()
        cursor = con.cursor
        database = open("DATABASE.txt", 'r')
        use = open("use.txt", 'r')
        tab_login = open("tab_login.txt", "w+")
        tab_login.write("CREATE TABLE IF NOT EXISTS login("
                        "login varchar(200) unique,"
                        "senha varchar(200) unique);")
        tab_login.seek(0)
        Login = open("login.txt", 'r')
        cursor.execute(database.read())
        cursor.execute(use.read())
        cursor.execute(tab_login.read())
        cursor.execute(Login.read())
        database.close()
        use.close()
        tab_login.close()
        Login.close()
        con.commit()
        cursor.close()
        con.close()
    except Exception as erro:
        print(erro)

    tela_3.show()
    tela_2.close()
    tela_5.close()
    tela_6.close()
    tela_7.close()
    tela_8.close()
    tela_13.close()
    tela_14.close()
    tela_15.close()
    tela_19.close()
    tela_20.close()
    tela_21.close()
    tela_25.close()


def p_PostgreSQL():
    tela_4.show()
    tela_2.close()
    tela_9.close()
    tela_10.close()
    tela_11.close()
    tela_12.close()
    tela_16.close()
    tela_17.close()
    tela_18.close()
    tela_22.close()
    tela_23.close()
    tela_24.close()
    tela_26.close()


def opcao():
    l.set_login(tela_3.lineEdit.text())
    l.set_senha(tela_3.lineEdit_2.text())
    try:
        tela_3.lineEdit.setText("")
        tela_3.lineEdit_2.setText("")
        con = MySQL.Connection()
        cursor = con.cursor
        cursor.execute("use projeto;")
        cursor.execute(f'SELECT senha FROM login WHERE login = "{l.get_login()}"')
        m = cursor.fetchone()
        cursor.execute(f'SELECT MD5("{l.get_senha()}")')
        s = cursor.fetchone()
        cursor.execute(f'SELECT login FROM login WHERE senha = MD5("{l.get_senha()}")')
        lo = cursor.fetchone()
        if s == m:
            tela_5.label_2.setText("CONEXÃO ESTABELECIDA")
            tela_5.show()
            tela_3.close()
            tela_6.close()
            tela_7.close()
            tela_8.close()
            tela_13.close()
            tela_14.close()
            tela_15.close()
            tela_19.close()
            tela_20.close()
            tela_21.close()
            tela_25.close()
            tela_3.label_4.setText(" ")
        elif s != m or s == ' ':
            tela_3.label_4.setText(" ")
            tela_3.label_4.setText("SENHA OU LOGIN INCORRETO")
        elif l.get_login() != lo or l.get_login() == ' ':
            tela_3.label_4.setText(" ")
            tela_3.label_4.setText("SENHA OU LOGIN INCORRETO")
        con.commit()
        cursor.close()
        con.close()
    except Exception as erro:
        print("ERRO: ", erro)


def opcao_2():
    l.set_login(tela_4.lineEdit.text())
    l.set_senha(tela_4.lineEdit_2.text())
    try:
        tela_4.lineEdit.setText("")
        tela_4.lineEdit_2.setText("")
        conn = PostgreSQL.Connection()
        cursor = conn.cursor
        cursor.execute(f"SELECT senha FROM login WHERE login = '{l.get_login()}'")
        passw = cursor.fetchone()
        cursor.execute(f"SELECT MD5('{l.get_senha()}')")
        password = cursor.fetchone()
        cursor.execute(f"SELECT login FROM login WHERE senha = MD5('{l.get_senha()}')")
        lo = cursor.fetchone()
        if passw == password:
            tela_9.label_2.setText("CONEXÃO ESTABELECIDA")
            tela_9.show()
            tela_4.close()
            tela_10.close()
            tela_11.close()
            tela_12.close()
            tela_16.close()
            tela_17.close()
            tela_18.close()
            tela_22.close()
            tela_23.close()
            tela_24.close()
            tela_26.close()
            tela_4.label_4.setText(" ")
        elif passw != password or passw == ' ':
            tela_4.label_4.setText(" ")
            tela_4.label_4.setText("SENHA OU LOGIN INCORRETO")
        elif l.get_login() != lo or l.get_login() == ' ':
            tela_4.label_4.setText(" ")
            tela_4.label_4.setText("SENHA OU LOGIN INCORRETO")
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as erro:
        print(erro)


def produto():
    tela_6.show()
    tela_5.close()
    tela_7.close()
    tela_8.close()
    try:
        con = MySQL.Connection()
        cursor = con.cursor
        cursor.execute("use projeto;")
        cursor.execute('CREATE TABLE IF NOT EXISTS produto( '
                       'codigo int primary key, '
                       'produto varchar(100), '
                       'marca varchar(100),'
                       'modelo varchar(100));')
        prod = open("prod.txt", 'r')
        prod.seek(0)
        for linha in prod:
            cursor.execute(f"{linha}")
        prod.close()
        cursor.execute("SELECT * FROM produto")
        p = cursor.fetchall()
        tela_6.tableWidget.setRowCount(len(p))
        tela_6.tableWidget.setColumnCount(len(p[0]))
        for i in range(0, len(p)):
            for j in range(0, len(p[0])):
                tela_6.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(p[i][j])))
        con.commit()
        con.close()
        con.close()
    except Exception as erro:
        print(erro)


def registro_produto():
    P.set_codigo(tela_6.lineEdit.text())
    P.set_tipo(tela_6.lineEdit_2.text())
    P.set_marca(tela_6.lineEdit_3.text())
    P.set_modelo(tela_6.lineEdit_4.text())
    try:
        con = MySQL.Connection()
        cursor = con.cursor
        prod = open("prod.txt", 'a+')
        cursor.execute("use projeto;")
        prod.write("INSERT IGNORE INTO produto(codigo,produto,marca,modelo)"
                   "VALUES('" + P.get_codigo() + "','" + P.get_tipo() + "','" + P.get_marca() + "','"
                   + P.get_modelo() + "');\n")
        prod.seek(0)
        for linha in prod:
            cursor.execute(f"{linha}")
        prod.close()
        cursor.execute(f"SELECT * FROM produto WHERE codigo = {P.get_codigo()}")
        p = cursor.fetchone()
        confirm = QMessageBox.question(AVISO, "AVISO", "Tem Certeza Disso?", QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            con.commit()
            con.close()
            con.close()
            tela_6.lineEdit.setText("")
            tela_6.lineEdit_2.setText("")
            tela_6.lineEdit_3.setText("")
            tela_6.lineEdit_4.setText("")
            tela_6.label_6.setText("DADOS INSERIDOS")
            tela_6.label_9.setText(f'{p[0]}')
            tela_6.label_13.setText(f'{p[1]}')
            tela_6.label_11.setText(f'{p[2]}')
            tela_6.label_15.setText(f'{p[3]}')
    except Exception as erro:
        print(erro)


def registro_produto_consulta():
    try:
        con = MySQL.Connection()
        cursor = con.cursor
        cursor.execute("use projeto;")
        cursor.execute("SELECT * FROM produto")
        p = cursor.fetchall()
        tela_6.tableWidget.setRowCount(len(p))
        tela_6.tableWidget.setColumnCount(len(p[0]))
        for i in range(0, len(p)):
            for j in range(0, len(p[0])):
                tela_6.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(p[i][j])))
        con.commit()
        con.close()
        con.close()
    except Exception as erro:
        print(erro)


def produto_2():
    tela_10.show()
    tela_9.close()
    tela_11.close()
    tela_12.close()
    try:
        conn = PostgreSQL.Connection()
        cursor = conn.cursor
        cursor.execute("SELECT * FROM produto")
        p = cursor.fetchall()
        tela_10.tableWidget.setRowCount(len(p))
        tela_10.tableWidget.setColumnCount(len(p[0]))
        for i in range(0, len(p)):
            for j in range(0, len(p[0])):
                tela_10.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(p[i][j])))
        conn.close()
    except Exception as erro:
        print(erro)


def registro_produto_2():
    P.set_codigo(tela_10.lineEdit.text())
    P.set_tipo(tela_10.lineEdit_2.text())
    P.set_marca(tela_10.lineEdit_3.text())
    P.set_modelo(tela_10.lineEdit_4.text())
    try:
        conn = PostgreSQL.Connection()
        cursor = conn.cursor
        cursor.execute('CREATE TABLE IF NOT EXISTS produto( '
                       'codigo int primary key, '
                       'produto varchar(100), '
                       'marca varchar(100),'
                       'modelo varchar(100));')
        cursor.execute("INSERT INTO produto(codigo,produto,marca,modelo)"
                       "VALUES('" + P.get_codigo() + "','" + P.get_tipo() + "','" + P.get_marca() + "','"
                       + P.get_modelo() + "');")
        cursor.execute(f"SELECT * FROM produto WHERE codigo = {P.get_codigo()}")
        p = cursor.fetchone()
        conn.commit()
        conn.close()
        tela_10.lineEdit.setText("")
        tela_10.lineEdit_2.setText("")
        tela_10.lineEdit_3.setText("")
        tela_10.lineEdit_4.setText("")
        tela_10.label_9.setText(f'{p[0]}')
        tela_10.label_11.setText(f'{p[1]}')
        tela_10.label_13.setText(f'{p[2]}')
        tela_10.label_15.setText(f'{p[3]}')
        tela_10.label_6.setText("DADOS INSERIDOS")
    except Exception as erro:
        print(erro)


def registro_produto_2_consulta():
    try:
        conn = PostgreSQL.Connection()
        cursor = conn.cursor
        cursor.execute("SELECT * FROM loja")
        p = cursor.fetchall()
        tela_10.tableWidget.setRowCount(len(p))
        tela_10.tableWidget.setColumnCount(len(p[0]))
        for i in range(0, len(p)):
            for j in range(0, len(p[0])):
                tela_10.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(p[i][j])))
        conn.close()
    except Exception as erro:
        print(erro)


def loja():
    tela_7.show()
    tela_6.close()
    tela_8.close()
    try:
        con = MySQL.Connection()
        cursor = con.cursor
        cursor.execute("use projeto;")
        cursor.execute("SELECT * FROM loja")
        lj = cursor.fetchall()
        tela_7.tableWidget.setRowCount(len(lj))
        tela_7.tableWidget.setColumnCount(len(lj[0]))
        for i in range(0, len(lj)):
            for j in range(0, len(lj[0])):
                tela_7.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(lj[i][j])))
        con.close()
    except Exception as erro:
        print(erro)


def registro_loja():
    L.set_cnpj(tela_7.lineEdit.text())
    L.set_nome(tela_7.lineEdit_2.text())
    L.set_local(tela_7.lineEdit_3.text())
    L.set_cod(tela_7.lineEdit_4.text())
    L.set_preco(tela_7.lineEdit_6.text())
    try:
        con = MySQL.Connection()
        cursor = con.cursor
        cursor.execute("use projeto;")
        cursor.execute('CREATE TABLE IF NOT EXISTS loja('
                       'cnpj char(14) primary key,'
                       'nome varchar(100),'
                       'localizacao varchar(100),'
                       'cod_produto int,'
                       'preco decimal(7,2),'
                       'foreign key(cod_produto) references produto(codigo));')
        cursor.execute("INSERT INTO loja(cnpj,nome,localizacao,cod_produto,preco)"
                       "VALUES('" + L.get_cnpj() + "','" + L.get_nome() + "','" + L.get_local() + "','"
                       + L.get_cod() + "','" + L.get_preco() + "');")
        cursor.execute(f"SELECT * FROM loja WHERE cnpj = '{L.get_cnpj()}'")
        lj = cursor.fetchone()
        con.commit()
        con.close()
        tela_7.lineEdit.setText("")
        tela_7.lineEdit_2.setText("")
        tela_7.lineEdit_3.setText("")
        tela_7.lineEdit_4.setText("")
        tela_7.lineEdit_6.setText("")
        tela_7.label_9.setText(f'{lj[0]}')
        tela_7.label_13.setText(f'{lj[1]}')
        tela_7.label_11.setText(f'{lj[2]}')
        tela_7.label_20.setText(f'{lj[3]}')
        tela_7.label_17.setText(f'{lj[4]}')
        tela_7.label_14.setText("DADOS INSERIDOS")
    except Exception as erro:
        print(erro)


def registro_loja_consulta():
    try:
        con = MySQL.Connection()
        cursor = con.cursor
        cursor.execute("use projeto;")
        cursor.execute("SELECT * FROM loja")
        lj = cursor.fetchall()
        tela_7.tableWidget.setRowCount(len(lj))
        tela_7.tableWidget.setColumnCount(len(lj[0]))
        for i in range(0, len(lj)):
            for j in range(0, len(lj[0])):
                tela_7.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(lj[i][j])))
        con.close()
    except Exception as erro:
        print(erro)


def loja_2():
    tela_11.show()
    tela_10.close()
    tela_9.close()
    tela_12.close()
    try:
        conn = PostgreSQL.Connection()
        cursor = conn.cursor
        cursor.execute("SELECT * FROM loja")
        lj = cursor.fetchall()
        tela_11.tableWidget.setRowCount(len(lj))
        tela_11.tableWidget.setColumnCount(len(lj[0]))
        for i in range(0, len(lj)):
            for j in range(0, len(lj[0])):
                tela_11.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(lj[i][j])))
        conn.close()
    except Exception as erro:
        print(erro)


def registro_loja_2():
    L.set_cnpj(tela_11.lineEdit.text())
    L.set_nome(tela_11.lineEdit_2.text())
    L.set_local(tela_11.lineEdit_3.text())
    L.set_cod(tela_11.lineEdit_4.text())
    L.set_preco(tela_11.lineEdit_6.text())
    try:
        conn = PostgreSQL.Connection()
        cursor = conn.cursor
        cursor.execute('CREATE TABLE IF NOT EXISTS loja('
                       'cnpj char(14) primary key,'
                       'nome varchar(100),'
                       'localizacao varchar(100),'
                       'cod_produto int,'
                       'preco decimal(7,2),'
                       'foreign key(cod_produto) references produto(codigo));')
        cursor.execute("INSERT INTO loja(cnpj,nome,localizacao,cod_produto,preco)"
                       "VALUES('" + L.get_cnpj() + "','" + L.get_nome() + "','" + L.get_local() + "','"
                       + L.get_cod() + "','" + L.get_preco() + "');")
        cursor.execute(f"SELECT * FROM loja WHERE cnpj = '{L.get_cnpj()}'")
        lj = cursor.fetchone()
        conn.commit()
        conn.close()
        tela_11.lineEdit.setText("")
        tela_11.lineEdit_2.setText("")
        tela_11.lineEdit_3.setText("")
        tela_11.lineEdit_4.setText("")
        tela_11.lineEdit_6.setText("")
        tela_11.label_9.setText(f'{lj[0]}')
        tela_11.label_13.setText(f'{lj[1]}')
        tela_11.label_11.setText(f'{lj[2]}')
        tela_11.label_20.setText(f'{lj[3]}')
        tela_11.label_17.setText(f'{lj[4]}')
        tela_11.label_14.setText("DADOS INSERIDOS")
    except Exception as erro:
        print(erro)


def registro_loja_2_consulta():
    try:
        conn = PostgreSQL.Connection()
        cursor = conn.cursor
        cursor.execute("SELECT * FROM loja")
        lj = cursor.fetchall()
        tela_11.tableWidget.setRowCount(len(lj))
        tela_11.tableWidget.setColumnCount(len(lj[0]))
        for i in range(0, len(lj)):
            for j in range(0, len(lj[0])):
                tela_11.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(lj[i][j])))
        conn.close()
    except Exception as erro:
        print(erro)


def caracteristica():
    tela_8.show()
    tela_7.close()
    tela_6.close()
    try:
        con = MySQL.Connection()
        cursor = con.cursor
        cursor.execute("use projeto;")
        cursor.execute("SELECT * FROM caracteristica")
        c = cursor.fetchall()
        tela_8.tableWidget.setRowCount(len(c))
        tela_8.tableWidget.setColumnCount(len(c[0]))
        for i in range(0, len(c)):
            for j in range(0, len(c[0])):
                tela_8.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(c[i][j])))
        con.close()
    except Exception as erro:
        print(erro)


def registro_caracteristica():
    C.set_processador(tela_8.lineEdit.text())
    C.set_ram(tela_8.lineEdit_2.text())
    C.set_interna(tela_8.lineEdit_3.text())
    C.set_expansivel(tela_8.lineEdit_4.text())
    C.set_cod(tela_8.lineEdit_5.text())
    try:
        con = MySQL.Connection()
        cursor = con.cursor
        cursor.execute("use projeto;")
        cursor.execute('create table if not exists caracteristica('
                       'ID int primary key auto_increment,'
                       'processador varchar(200),'
                       'ram varchar(200),'
                       'm_interna varchar(200),'
                       'm_expansivel varchar(200),'
                       'cod_produto int,'
                       'foreign key(cod_produto) references produto(codigo)'
                       ');')
        cursor.execute("INSERT INTO caracteristica(processador,ram,m_interna,m_expansivel,cod_produto)"
                       "Values('" + C.get_processador() + "','" + C.get_ram() + "','" + C.get_interna() + "','"
                       + C.get_expansivel() + "','" + C.get_cod() + "');")
        cursor.execute("SELECT * FROM caracteristica WHERE ID =(SELECT MAX(ID) FROM caracteristica) ")
        c = cursor.fetchone()
        con.commit()
        con.close()
        tela_8.lineEdit.setText("")
        tela_8.lineEdit_2.setText("")
        tela_8.lineEdit_3.setText("")
        tela_8.lineEdit_4.setText("")
        tela_8.lineEdit_5.setText("")
        tela_8.label_8.setText(f'{c[1]}')
        tela_8.label_10.setText(f'{c[2]}')
        tela_8.label_12.setText(f'{c[3]}')
        tela_8.label_14.setText(f'{c[4]}')
        tela_8.label_16.setText(f'{c[5]}')
        tela_8.label_19.setText("DADOS INSERIDOS")
    except Exception as erro:
        print(erro)


def registro_caracteristica_consulta():
    try:
        con = MySQL.Connection()
        cursor = con.cursor
        cursor.execute("use projeto;")
        cursor.execute("SELECT * FROM caracteristica")
        c = cursor.fetchall()
        tela_8.tableWidget.setRowCount(len(c))
        tela_8.tableWidget.setColumnCount(len(c[0]))
        for i in range(0, len(c)):
            for j in range(0, len(c[0])):
                tela_8.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(c[i][j])))
        con.close()
    except Exception as erro:
        print(erro)


def caracteristica_2():
    tela_12.show()
    tela_10.close()
    tela_11.close()


def registro_caracteristica_2():
    try:
        conn = PostgreSQL.Connection()
        cursor = conn.cursor
        cursor.execute()
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as erro:
        print(erro)


def registro_caracteristica_2_consulta():
    try:
        conn = PostgreSQL.Connection()
        cursor = conn.cursor
        cursor.execute("SELECT * FROM caracteristica")
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as erro:
        print(erro)


def update_produto():
    tela_13.show()
    tela_5.close()
    tela_14.close()
    tela_15.close()
    try:
        con = MySQL.Connection()
        cursor = con.cursor
        cursor.execute("use projeto;")
        cursor.execute("SELECT * FROM produto")
        p = cursor.fetchall()
        tela_13.tableWidget.setRowCount(len(p))
        tela_13.tableWidget.setColumnCount(len(p[0]))
        for i in range(0, len(p)):
            for j in range(0, len(p[0])):
                tela_13.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(p[i][j])))
        con.close()
    except Exception as erro:
        print(erro)


def update_produto_up():
    D.set_coluna_U(tela_13.lineEdit.text())
    D.set_dado_U(tela_13.lineEdit_2.text())
    D.set_coluna(tela_13.lineEdit_3.text())
    D.set_dado(tela_13.lineEdit_4.text())
    try:
        con = MySQL.Connection()
        cursor = con.cursor
        cursor.execute("use projeto;")
        cursor.execute("UPDATE produto SET " + D.get_coluna_U() + " = '" + D.get_dado_U() + "' WHERE "
                       + D.get_coluna() + " = '" + D.get_dado() + "';")
        cursor.execute("SELECT * FROM produto WHERE " + D.get_coluna() + " = '" + D.get_dado() + "';")
        p_u = cursor.fetchone()
        con.commit()
        con.close()
        tela_13.lineEdit.setText("")
        tela_13.lineEdit_2.setText("")
        tela_13.lineEdit_3.setText("")
        tela_13.lineEdit_4.setText("")
        tela_13.label_6.setText("DADOS ATUALIZADOS")
        tela_13.label_9.setText(f'{p_u[0]}')
        tela_13.label_11.setText(f'{p_u[1]}')
        tela_13.label_13.setText(f'{p_u[2]}')
        tela_13.label_15.setText(f'{p_u[3]}')
    except Exception as erro:
        print(erro)


def update_produto_consulta():
    try:
        con = MySQL.Connection()
        cursor = con.cursor
        cursor.execute("use projeto;")
        cursor.execute("SELECT * FROM produto")
        p = cursor.fetchall()
        tela_13.tableWidget.setRowCount(len(p))
        tela_13.tableWidget.setColumnCount(len(p[0]))
        for i in range(0, len(p)):
            for j in range(0, len(p[0])):
                tela_13.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(p[i][j])))
        con.close()
    except Exception as erro:
        print(erro)


def update_produto_2():
    tela_16.show()
    tela_9.close()
    tela_17.close()
    tela_18.close()


def update_produto_2_up():
    tela_16.show()
    tela_9.close()
    tela_17.close()
    tela_18.close()
    try:
        conn = PostgreSQL.Connection()
        cursor = conn.cursor
        cursor.execute()
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as erro:
        print(erro)


def update_produto_2_consulta():
    tela_16.show()
    tela_9.close()
    tela_17.close()
    tela_18.close()
    try:
        conn = PostgreSQL.Connection()
        cursor = conn.cursor
        cursor.execute("SELECT * FROM produto")
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as erro:
        print(erro)


def update_lojas():
    tela_14.show()
    tela_13.close()
    tela_15.close()
    try:
        con = MySQL.Connection()
        cursor = con.cursor
        cursor.execute("use projeto;")
        cursor.execute("SELECT * FROM loja")
        lj = cursor.fetchall()
        tela_14.tableWidget.setRowCount(len(lj))
        tela_14.tableWidget.setColumnCount(len(lj[0]))
        for i in range(0, len(lj)):
            for j in range(0, len(lj[0])):
                tela_14.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(lj[i][j])))
        con.close()
    except Exception as erro:
        print(erro)


def update_lojas_up():
    D.set_coluna_U(tela_14.lineEdit.text())
    D.set_dado_U(tela_14.lineEdit_2.text())
    D.set_coluna(tela_14.lineEdit_3.text())
    D.set_dado(tela_14.lineEdit_4.text())
    try:
        con = MySQL.Connection()
        cursor = con.cursor
        cursor.execute("use projeto;")
        cursor.execute("UPDATE loja SET " + D.get_coluna_U() + " = '" + D.get_dado_U() + "' WHERE "
                       + D.get_coluna() + " = '" + D.get_dado() + "';")
        cursor.execute("SELECT * FROM loja WHERE " + D.get_coluna() + " = '" + D.get_dado() + "';")
        l_u = cursor.fetchone()
        con.commit()
        con.close()
        tela_14.lineEdit.setText("")
        tela_14.lineEdit_2.setText("")
        tela_14.lineEdit_3.setText("")
        tela_14.lineEdit_4.setText("")
        tela_14.label_9.setText(f'{l_u[0]}')
        tela_14.label_11.setText(f'{l_u[1]}')
        tela_14.label_13.setText(f'{l_u[2]}')
        tela_14.label_20.setText(f'{l_u[3]}')
        tela_14.label_17.setText(f'{l_u[4]}')
        tela_14.label_5.setText("DADOS ATUALIZADOS")
    except Exception as erro:
        print(erro)


def update_lojas_consulta():
    try:
        con = MySQL.Connection()
        cursor = con.cursor
        cursor.execute("use projeto;")
        cursor.execute("SELECT * FROM loja")
        lj = cursor.fetchall()
        tela_14.tableWidget.setRowCount(len(lj))
        tela_14.tableWidget.setColumnCount(len(lj[0]))
        for i in range(0, len(lj)):
            for j in range(0, len(lj[0])):
                tela_14.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(lj[i][j])))
        con.close()
    except Exception as erro:
        print(erro)


def update_lojas_2():
    tela_17.show()
    tela_16.close()
    tela_18.close()


def update_lojas_2_up():
    tela_17.show()
    tela_16.close()
    tela_18.close()
    try:
        conn = PostgreSQL.Connection()
        cursor = conn.cursor
        cursor.execute()
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as erro:
        print(erro)


def update_lojas_2_consulta():
    tela_17.show()
    tela_16.close()
    tela_18.close()
    try:
        conn = PostgreSQL.Connection()
        cursor = conn.cursor
        cursor.execute("SELECT * FROM loja")
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as erro:
        print(erro)


def update_caracteristica():
    tela_15.show()
    tela_5.close()
    tela_13.close()
    tela_14.close()
    try:
        con = MySQL.Connection()
        cursor = con.cursor
        cursor.execute("use projeto;")
        cursor.execute("SELECT * FROM caracteristica")
        c = cursor.fetchall()
        tela_15.tableWidget.setRowCount(len(c))
        tela_15.tableWidget.setColumnCount(len(c[0]))
        for i in range(0, len(c)):
            for j in range(0, len(c[0])):
                tela_15.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(c[i][j])))
        con.close()
    except Exception as erro:
        print(erro)


def update_caracteristica_up():
    D.set_coluna_U(tela_15.lineEdit.text())
    D.set_dado_U(tela_15.lineEdit_2.text())
    D.set_coluna(tela_15.lineEdit_3.text())
    D.set_dado(tela_15.lineEdit_4.text())
    try:
        con = MySQL.Connection()
        cursor = con.cursor
        cursor.execute("use projeto;")
        cursor.execute("UPDATE caracteristica SET " + D.get_coluna_U() + " = '" + D.get_dado_U() + "' WHERE "
                       + D.get_coluna() + " = '" + D.get_dado() + "';")
        cursor.execute("SELECT * FROM caracteristica WHERE " + D.get_coluna() + " = '" + D.get_dado() + "';")
        c = cursor.fetchone()
        con.commit()
        con.close()
        tela_15.lineEdit.setText("")
        tela_15.lineEdit_2.setText("")
        tela_15.lineEdit_3.setText("")
        tela_15.lineEdit_4.setText("")
        tela_15.label_8.setText(f'{c[1]}')
        tela_15.label_10.setText(f'{c[2]}')
        tela_15.label_12.setText(f'{c[3]}')
        tela_15.label_14.setText(f'{c[4]}')
        tela_15.label_16.setText(f'{c[5]}')
        tela_15.label_6.setText("DADOS ATUALIZADOS")
    except Exception as erro:
        print(erro)


def update_caracteristica_consulta():
    try:
        con = MySQL.Connection()
        cursor = con.cursor
        cursor.execute("use projeto;")
        cursor.execute("SELECT * FROM caracteristica")
        c = cursor.fetchall()
        tela_15.tableWidget.setRowCount(len(c))
        tela_15.tableWidget.setColumnCount(len(c[0]))
        for i in range(0, len(c)):
            for j in range(0, len(c[0])):
                tela_15.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(c[i][j])))
        con.close()
    except Exception as erro:
        print(erro)


def update_caracteristica_2():
    tela_18.show()
    tela_9.close()
    tela_17.close()
    tela_16.close()


def update_caracteristica_2_up():
    tela_18.show()
    tela_9.close()
    tela_17.close()
    tela_16.close()
    try:
        conn = PostgreSQL.Connection()
        cursor = conn.cursor
        cursor.execute()
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as erro:
        print(erro)


def update_caracteristica_2_consulta():
    tela_18.show()
    tela_9.close()
    tela_17.close()
    tela_16.close()
    try:
        conn = PostgreSQL.Connection()
        cursor = conn.cursor
        cursor.execute("SELECT * FROM caracteristica")
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as erro:
        print(erro)


def delete_produto():
    tela_19.show()
    tela_5.close()
    tela_20.close()
    tela_21.close()
    try:
        con = MySQL.Connection()
        cursor = con.cursor
        cursor.execute("use projeto;")
        cursor.execute("SELECT * FROM produto")
        p = cursor.fetchall()
        tela_19.tableWidget.setRowCount(len(p))
        tela_19.tableWidget.setColumnCount(len(p[0]))
        for i in range(0, len(p)):
            for j in range(0, len(p[0])):
                tela_19.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(p[i][j])))
        con.close()
    except Exception as erro:
        print(erro)


def delete_produto_D():
    D.set_coluna(tela_19.lineEdit.text())
    D.set_dado(tela_19.lineEdit_2.text())
    try:
        con = MySQL.Connection()
        cursor = con.cursor
        cursor.execute("use projeto;")
        cursor.execute("SELECT * FROM produto WHERE " + D.get_coluna() + " = '" + D.get_dado() + "'; ")
        c = cursor.fetchone()
        cursor.execute("DELETE FROM produto WHERE " + D.get_coluna() + " = '" + D.get_dado() + "';")
        con.commit()
        con.close()
        tela_19.lineEdit.setText("")
        tela_19.lineEdit_2.setText("")
        tela_19.label_9.setText(f'{c[0]}')
        tela_19.label_11.setText(f'{c[1]}')
        tela_19.label_13.setText(f'{c[2]}')
        tela_19.label_15.setText(f'{c[3]}')
        tela_19.label_3.setText("DADOS DELETADOS")
    except Exception as erro:
        print(erro)


def delete_produto_consulta():
    try:
        con = MySQL.Connection()
        cursor = con.cursor
        cursor.execute("use projeto;")
        cursor.execute("SELECT * FROM produto")
        p = cursor.fetchall()
        tela_19.tableWidget.setRowCount(len(p))
        tela_19.tableWidget.setColumnCount(len(p[0]))
        for i in range(0, len(p)):
            for j in range(0, len(p[0])):
                tela_19.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(p[i][j])))
        con.close()
    except Exception as erro:
        print(erro)


def delete_lojas():
    tela_20.show()
    tela_19.close()
    tela_5.close()
    tela_21.close()
    try:
        con = MySQL.Connection()
        cursor = con.cursor
        cursor.execute("use projeto;")
        cursor.execute("SELECT * FROM loja")
        p = cursor.fetchall()
        tela_20.tableWidget.setRowCount(len(p))
        tela_20.tableWidget.setColumnCount(len(p[0]))
        for i in range(0, len(p)):
            for j in range(0, len(p[0])):
                tela_20.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(p[i][j])))
        con.close()
    except Exception as erro:
        print(erro)


def delete_lojas_D():
    D.set_coluna(tela_20.lineEdit.text())
    D.set_dado(tela_20.lineEdit_2.text())
    try:
        con = MySQL.Connection()
        cursor = con.cursor
        cursor.execute("use projeto;")
        cursor.execute("SELECT * FROM loja WHERE " + D.get_coluna() + " = '" + D.get_dado() + "'; ")
        c = cursor.fetchone()
        cursor.execute("DELETE FROM loja WHERE " + D.get_coluna() + " = '" + D.get_dado() + "';")
        con.commit()
        con.close()
        tela_20.lineEdit.setText("")
        tela_20.lineEdit_2.setText("")
        tela_20.label_9.setText(f'{c[0]}')
        tela_20.label_11.setText(f'{c[1]}')
        tela_20.label_13.setText(f'{c[2]}')
        tela_20.label_20.setText(f'{c[3]}')
        tela_20.label_17.setText(f'{c[4]}')
        tela_20.label_2.setText("DADOS DELETADOS")
    except Exception as erro:
        print(erro)


def delete_lojas_consulta():
    try:
        con = MySQL.Connection()
        cursor = con.cursor
        cursor.execute("use projeto;")
        cursor.execute("SELECT * FROM loja")
        p = cursor.fetchall()
        tela_20.tableWidget.setRowCount(len(p))
        tela_20.tableWidget.setColumnCount(len(p[0]))
        for i in range(0, len(p)):
            for j in range(0, len(p[0])):
                tela_20.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(p[i][j])))
        con.close()
    except Exception as erro:
        print(erro)


def delete_caracteristica():
    tela_21.show()
    tela_20.close()
    tela_19.close()
    tela_5.close()
    try:
        con = MySQL.Connection()
        cursor = con.cursor
        cursor.execute("use projeto;")
        cursor.execute("SELECT * FROM caracteristica")
        p = cursor.fetchall()
        tela_21.tableWidget.setRowCount(len(p))
        tela_21.tableWidget.setColumnCount(len(p[0]))
        for i in range(0, len(p)):
            for j in range(0, len(p[0])):
                tela_21.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(p[i][j])))
        con.close()
    except Exception as erro:
        print(erro)


def delete_caracteristica_D():
    D.set_coluna(tela_21.lineEdit.text())
    D.set_dado(tela_21.lineEdit_2.text())
    try:
        con = MySQL.Connection()
        cursor = con.cursor
        cursor.execute("use projeto;")
        cursor.execute("SELECT * FROM caracteristica WHERE " + D.get_coluna() + " = '" + D.get_dado() + "'; ")
        c = cursor.fetchone()
        cursor.execute("DELETE FROM caracteristica WHERE " + D.get_coluna() + " = '" + D.get_dado() + "';")
        con.commit()
        con.close()
        tela_21.lineEdit_2.setText("")
        tela_21.lineEdit.setText("")
        tela_21.label_8.setText(f'{c[1]}')
        tela_21.label_10.setText(f'{c[2]}')
        tela_21.label_12.setText(f'{c[3]}')
        tela_21.label_14.setText(f'{c[4]}')
        tela_21.label_16.setText(f'{c[5]}')
        tela_21.label_2.setText("DADOS DELETADOS")
    except Exception as erro:
        print(erro)


def delete_caracteristica_consulta():
    try:
        con = MySQL.Connection()
        cursor = con.cursor
        cursor.execute("use projeto;")
        cursor.execute("SELECT * FROM caracteristica")
        p = cursor.fetchall()
        tela_20.tableWidget.setRowCount(len(p))
        tela_20.tableWidget.setColumnCount(len(p[0]))
        for i in range(0, len(p)):
            for j in range(0, len(p[0])):
                tela_20.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(p[i][j])))
        con.close()
    except Exception as erro:
        print(erro)


def delete_produto_2():
    tela_22.show()
    tela_9.close()
    tela_23.close()
    tela_24.close()


def delete_produto_D_2():
    tela_22.show()
    tela_9.close()
    tela_23.close()
    tela_24.close()
    try:
        conn = PostgreSQL.Connection()
        cursor = conn.cursor
        cursor.execute()
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as erro:
        print(erro)


def delete_produto_consulta_2():
    tela_22.show()
    tela_9.close()
    tela_23.close()
    tela_24.close()
    try:
        conn = PostgreSQL.Connection()
        cursor = conn.cursor
        cursor.execute("SELECT * FROM produto")
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as erro:
        print(erro)


def delete_lojas_2():
    tela_23.show()
    tela_22.close()
    tela_9.close()
    tela_24.close()


def delete_lojas_D_2():
    tela_23.show()
    tela_22.close()
    tela_9.close()
    tela_24.close()
    try:
        conn = PostgreSQL.Connection()
        cursor = conn.cursor
        cursor.execute()
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as erro:
        print(erro)


def delete_lojas_consulta_2():
    tela_23.show()
    tela_22.close()
    tela_9.close()
    tela_24.close()
    try:
        conn = PostgreSQL.Connection()
        cursor = conn.cursor
        cursor.execute("SELECT * FROM loja")
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as erro:
        print(erro)


def delete_caracteristica_2():
    tela_24.show()
    tela_23.close()
    tela_22.close()
    tela_9.close()


def delete_caracteristica_D_2():
    tela_24.show()
    tela_23.close()
    tela_22.close()
    tela_9.close()
    try:
        conn = PostgreSQL.Connection()
        cursor = conn.cursor
        cursor.execute()
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as erro:
        print(erro)


def delete_caracteristica_consulta_2():
    tela_24.show()
    tela_23.close()
    tela_22.close()
    tela_9.close()
    try:
        conn = PostgreSQL.Connection()
        cursor = conn.cursor
        cursor.execute("SELECT * FROM caracteristica")
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as erro:
        print(erro)


def consulta_1():
    tela_5.close()
    tela_25.show()


def consulta():
    D.set_coluna(tela_25.lineEdit.text())
    D.set_dado(tela_25.lineEdit_2.text())
    try:
        con = MySQL.Connection()
        cursor = con.cursor
        cursor.execute("use projeto;")
        cursor.execute \
            ("SELECT produto.*,preco,processador,ram,m_interna,m_expansivel,l.nome,l.localizacao FROM produto "
             "right join loja l on  l.cod_produto = produto.codigo "
             "right join caracteristica c on c.cod_produto = produto.codigo "
             "WHERE " + D.get_coluna() + " = '" + D.get_dado() + "';")
        p = cursor.fetchall()
        tela_25.tableWidget.setRowCount(len(p))
        tela_25.tableWidget.setColumnCount(len(p[0]))
        for i in range(0, len(p)):
            for j in range(0, len(p[0])):
                tela_25.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(p[i][j])))
        con.close()
    except Exception as erro:
        print(erro)


def consulta_2_1():
    tela_9.close()
    tela_26.show()


def consulta_2():
    tela_9.close()
    tela_26.show()
    try:
        conn = PostgreSQL.Connection()
        cursor = conn.cursor
        cursor.execute()
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as erro:
        print(erro)


app = QtWidgets.QApplication([])
tela = uic.loadUi("ABERTURA.ui")
tela_2 = uic.loadUi("SGBD.ui")
tela_3 = uic.loadUi("LOGIN(Mysql).ui")
tela_4 = uic.loadUi("LOGIN(Postgres).ui")
tela_5 = uic.loadUi("Opção.ui")
tela_6 = uic.loadUi("Produto.ui")
tela_7 = uic.loadUi("Lojas.ui")
tela_8 = uic.loadUi("Caractéristicas.ui")
tela_9 = uic.loadUi("Opção_2.ui")
tela_10 = uic.loadUi("Produto_2.ui")
tela_11 = uic.loadUi("Lojas_2.ui")
tela_12 = uic.loadUi("Caractéristicas_2.ui")
tela_13 = uic.loadUi("Produto_up.ui")
tela_14 = uic.loadUi("Lojas_up.ui")
tela_15 = uic.loadUi("Caractéristicas_up.ui")
tela_16 = uic.loadUi("Produto_up_2.ui")
tela_17 = uic.loadUi("Lojas_up_2.ui")
tela_18 = uic.loadUi("Caractéristicas_up_2.ui")
tela_19 = uic.loadUi("Produto_D.ui")
tela_20 = uic.loadUi("Lojas_D.ui")
tela_21 = uic.loadUi("Caractéristicas_D.ui")
tela_22 = uic.loadUi("Produto_D_2.ui")
tela_23 = uic.loadUi("Lojas_D.ui")
tela_24 = uic.loadUi("Caractéristicas_D_2.ui")
tela_25 = uic.loadUi("consulta.ui")
tela_26 = uic.loadUi("consulta_2.ui")
AVISO = uic.loadUi("confirmação.ui")
tela.INICIAR.clicked.connect(SGBD)
tela_2.MYSQL.clicked.connect(m_MySQL)
tela_2.POSTGRESQL.clicked.connect(p_PostgreSQL)

tela_3.CONECTAR.clicked.connect(opcao)
tela_3.pushButton.clicked.connect(SGBD)
tela_3.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

tela_4.pushButton_2.clicked.connect(SGBD)
tela_4.pushButton.clicked.connect(opcao_2)
tela_4.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

tela_5.pushButton_2.clicked.connect(produto)
tela_5.pushButton_4.clicked.connect(update_produto)
tela_5.pushButton_5.clicked.connect(SGBD)
tela_5.pushButton_3.clicked.connect(delete_produto)
tela_5.pushButton.clicked.connect(consulta_1)

tela_6.pushButton_4.clicked.connect(loja)
tela_6.pushButton_3.clicked.connect(caracteristica)
tela_6.pushButton_6.clicked.connect(m_MySQL)
tela_6.pushButton_2.clicked.connect(registro_produto_consulta)
tela_6.pushButton.clicked.connect(registro_produto)

tela_7.pushButton_3.clicked.connect(caracteristica)
tela_7.pushButton_5.clicked.connect(produto)
tela_7.pushButton_6.clicked.connect(m_MySQL)
tela_7.pushButton_2.clicked.connect(registro_loja_consulta)
tela_7.pushButton.clicked.connect(registro_loja)

tela_8.pushButton_5.clicked.connect(produto)
tela_8.pushButton_4.clicked.connect(loja)
tela_8.pushButton_6.clicked.connect(m_MySQL)
tela_8.pushButton_2.clicked.connect(registro_caracteristica_consulta)
tela_8.pushButton.clicked.connect(registro_caracteristica)

tela_9.pushButton_2.clicked.connect(produto_2)
tela_9.pushButton_5.clicked.connect(SGBD)
tela_9.pushButton_4.clicked.connect(update_produto_2)
tela_9.pushButton_3.clicked.connect(delete_produto_2)
tela_9.pushButton.clicked.connect(consulta_2_1)

tela_10.pushButton_4.clicked.connect(loja_2)
tela_10.pushButton_3.clicked.connect(caracteristica_2)
tela_10.pushButton_6.clicked.connect(p_PostgreSQL)
tela_10.pushButton_2.clicked.connect(registro_produto_2_consulta)
tela_10.pushButton.clicked.connect(registro_produto_2)

tela_11.pushButton_3.clicked.connect(caracteristica_2)
tela_11.pushButton_5.clicked.connect(produto_2)
tela_11.pushButton_6.clicked.connect(p_PostgreSQL)
tela_11.pushButton_2.clicked.connect(registro_loja_2_consulta)
tela_11.pushButton.clicked.connect(registro_loja_2)

tela_12.pushButton_5.clicked.connect(produto_2)
tela_12.pushButton_4.clicked.connect(loja_2)
tela_12.pushButton_6.clicked.connect(p_PostgreSQL)
tela_12.pushButton_2.clicked.connect(registro_caracteristica_2_consulta)
tela_12.pushButton.clicked.connect(registro_caracteristica)

tela_13.pushButton_4.clicked.connect(update_lojas)
tela_13.pushButton_3.clicked.connect(update_caracteristica)
tela_13.pushButton_6.clicked.connect(m_MySQL)
tela_13.pushButton_2.clicked.connect(update_produto_consulta)
tela_13.pushButton.clicked.connect(update_produto_up)

tela_14.pushButton_3.clicked.connect(update_caracteristica)
tela_14.pushButton_5.clicked.connect(update_produto)
tela_14.pushButton_6.clicked.connect(m_MySQL)
tela_14.pushButton_2.clicked.connect(update_lojas_consulta)
tela_14.pushButton.clicked.connect(update_lojas_up)

tela_15.pushButton_5.clicked.connect(update_produto)
tela_15.pushButton_4.clicked.connect(update_lojas)
tela_15.pushButton_6.clicked.connect(m_MySQL)
tela_15.pushButton_2.clicked.connect(update_caracteristica_consulta)
tela_15.pushButton.clicked.connect(update_caracteristica_up)

tela_16.pushButton_4.clicked.connect(update_lojas_2)
tela_16.pushButton_3.clicked.connect(update_caracteristica_2)
tela_16.pushButton_6.clicked.connect(p_PostgreSQL)
tela_16.pushButton_2.clicked.connect(update_produto_2_consulta)
tela_16.pushButton.clicked.connect(update_produto_2_up)

tela_17.pushButton_3.clicked.connect(update_caracteristica_2)
tela_17.pushButton_5.clicked.connect(update_produto_2)
tela_17.pushButton_6.clicked.connect(p_PostgreSQL)
tela_17.pushButton_2.clicked.connect(update_lojas_2_consulta)
tela_17.pushButton.clicked.connect(update_lojas_2_up)

tela_18.pushButton_5.clicked.connect(update_produto_2)
tela_18.pushButton_4.clicked.connect(update_lojas_2)
tela_18.pushButton_6.clicked.connect(p_PostgreSQL)
tela_18.pushButton_2.clicked.connect(update_caracteristica_2_consulta)
tela_18.pushButton.clicked.connect(update_caracteristica_2_up)

tela_19.pushButton.clicked.connect(delete_produto_D)
tela_19.pushButton_2.clicked.connect(delete_produto_consulta)
tela_19.pushButton_4.clicked.connect(delete_lojas)
tela_19.pushButton_3.clicked.connect(delete_caracteristica)
tela_19.pushButton_6.clicked.connect(m_MySQL)

tela_20.pushButton_3.clicked.connect(delete_caracteristica)
tela_20.pushButton_5.clicked.connect(delete_produto)
tela_20.pushButton_6.clicked.connect(m_MySQL)
tela_20.pushButton.clicked.connect(delete_lojas_consulta)
tela_20.pushButton_2.clicked.connect(delete_lojas_D)

tela_21.pushButton_5.clicked.connect(delete_produto)
tela_21.pushButton_4.clicked.connect(delete_lojas)
tela_21.pushButton_6.clicked.connect(m_MySQL)
tela_21.pushButton_2.clicked.connect(delete_caracteristica_consulta)
tela_21.pushButton.clicked.connect(delete_caracteristica_D)

tela_22.pushButton_2.clicked.connect(delete_produto_D_2)
tela_22.pushButton.clicked.connect(delete_produto_consulta_2)
tela_22.pushButton_4.clicked.connect(delete_lojas_2)
tela_22.pushButton_3.clicked.connect(delete_caracteristica_2)
tela_22.pushButton_6.clicked.connect(p_PostgreSQL)

tela_23.pushButton_3.clicked.connect(delete_caracteristica_2)
tela_23.pushButton_5.clicked.connect(delete_produto_2)
tela_23.pushButton_6.clicked.connect(p_PostgreSQL)
tela_23.pushButton_2.clicked.connect(delete_lojas_consulta_2)
tela_23.pushButton.clicked.connect(delete_lojas_D_2)

tela_24.pushButton_5.clicked.connect(delete_produto_2)
tela_24.pushButton_4.clicked.connect(delete_lojas_2)
tela_24.pushButton_6.clicked.connect(p_PostgreSQL)
tela_24.pushButton_2.clicked.connect(delete_caracteristica_consulta_2)
tela_24.pushButton.clicked.connect(delete_caracteristica_D_2)

tela_25.pushButton_6.clicked.connect(m_MySQL)
tela_25.pushButton_2.clicked.connect(consulta)

tela_26.pushButton_6.clicked.connect(p_PostgreSQL)
tela_26.pushButton_2.clicked.connect(consulta_2)

tela.show()
app.exec()
