import mysql.connector 

# Dados da ligação 
HOST = "62.28.39.135"
USER = "efa0125"
PASSWORD = "123.Abc"
DATABASE = "efa0125_25_formacao_crud"

# Função para ligar a base de dados
def ligar_bd():
    return mysql.connector.connect(
        host = HOST,
        user = USER, 
        password = PASSWORD,
        database = DATABASE
    )

# Create - Inserir Utilizador
def inserir_utilizador():
    nome = input("Nome: ")
    email = input("E-mail: ")

    cnx = ligar_bd()
    cursor = cnx.cursor()

    sql = "INSERT INTO utilizadores (nome, email) VALUES (%s, %s)"
    cursor.execute(sql, (nome, email))
    cnx.commit()

    print("Utilizador inserido com sucesso!")

    cursor.close()
    cnx.close()


# READ - Listar utilizadores
def listar_utilizadores():
    cnx = ligar_bd()
    cursor = cnx.cursor() 

    sql = "SELECT id, nome, email, created_at FROM utilizadores"
    cursor.execute(sql)

    resultados = cursor.fetchall()

    print("\n --- LISTA DE UTILIZADORES --")
    for linha in resultados: 
        # linha = (id, nome, email, created_at)
        print(linha)

    cursor.close()
    cnx.close()

# UPDATE - Atualizar utilizador
def atualizar_utilizador():
    id_utilizador = input("Qual o ID do utilizador deseja atualizar? ")
    nome_utilizador = input("Novo nome: ")
    email_utilizador = input("Novo e-mail: ")

    cnx = ligar_bd()
    cursor = cnx.cursor()

    sql = "UPDATE utilizadores SET nome = %s, email = %s WHERE id = %s"
    cursor.execute(sql, (nome_utilizador, email_utilizador, id_utilizador))
    cnx.commit()

    print("Utilizador ATUALIZADO com sucesso!")

    cursor.close()
    cnx.close()

# DELETE - Apagar utilizador
def apagar_utilizador(): # =============== PROBLEMA AQUI =============
    id_utilizador = input("Qual ID do utilizador que você deseja DELETAR?")
            
    cnx = ligar_bd()
    cursor = cnx.cursor()

    sql = "DELETE FROM utilizadores WHERE id = %s"
    cursor.execute(sql, (id_utilizador))
    cnx.commit()

    print("Utilizador APAGADO com sucesso!")

    cursor.close()
    cnx.close()

# MENU PRINCIPAL
def menu():
    while True:
        print("\n===== MENU CRUD =====")
        print("1 - Inserir utilizador")
        print("2 - Listar utilizadores")
        print("3 - Atualizar utilizador")
        print("4 - Apagar utilizador")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1": 
            inserir_utilizador()
        elif opcao == "2":
            listar_utilizadores()
        elif opcao == "3":
            atualizar_utilizador()
        elif opcao == "4": 
            apagar_utilizador()
        elif opcao == "0":
            print("A sair...")
            break
        else: 
            print("Opção inválida!")


# Arranque do programa
menu()