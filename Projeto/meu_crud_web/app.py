# ---------------------------------------------------
# Imports
# ---------------------------------------------------
from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector
import os


# ---------------------------------------------------
# Função para ligar à base de dados MySQL
# ---------------------------------------------------
def ligar_bd():
    """
    Cria e retorna a conexão com o servidor MySQL.
    """
    return mysql.connector.connect(
        host="192.168.64.80",
        user="formando",
        password="123",
        database="projeto_crud"
    )


# ---------------------------------------------------
# Inicialização do Flask
# ---------------------------------------------------
app = Flask(__name__)


# ---------------------------------------------------
# Rota principal (lista utilizadores)
# ---------------------------------------------------
@app.route("/")
def index():
    # Proteger a página: só permite acesso se o utilizador estiver logado
    if "user_id" not in session:
        return redirect(url_for("login"))

    # Conectar à base de dados
    cnx = ligar_bd()
    cursor = cnx.cursor(dictionary=True)

    # Buscar todos os utilizadores
    cursor.execute("SELECT id, nome, email, created_at FROM utilizador ORDER BY id DESC")
    utilizadores = cursor.fetchall()

    # Fechar cursor e conexão
    cursor.close()
    cnx.close()

    # Renderizar o template com os utilizadores
    return render_template("index.html", utilizadores=utilizadores)


# ---------------------------------------------------
# Rota para criar novo utilizador
# ---------------------------------------------------
@app.route("/novo", methods=["GET", "POST"])
def novo():
    # Proteger a página
    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        # Receber dados do formulário
        nome = request.form["nome"]
        email = request.form["email"]

        # Inserir no banco
        cnx = ligar_bd()
        cursor = cnx.cursor()
        cursor.execute(
            "INSERT INTO utilizador (nome, email) VALUES (%s, %s)", 
            (nome, email)
        )
        cnx.commit()

        cursor.close()
        cnx.close()

        # Redirecionar para a página principal
        return redirect("/")

    # Se GET, exibir formulário vazio
    return render_template("form.html", titulo="Novo utilizador", utilizador=None)


# ---------------------------------------------------
# Rota para criar novo Login // PRECISO TERMINAR
# ---------------------------------------------------

@app.route("/register", methods=["GET", "POST"])
def novo():
    # Proteger a página
    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        # Receber dados do formulário
        username = request.form["username"]
        password = request.form["password"]

        # Inserir no banco
        cnx = ligar_bd()
        cursor = cnx.cursor()
        cursor.execute(
            "INSERT INTO utilizador (username, password) VALUES (%s, %s)", 
            (username, password)
        )
        cnx.commit()

        cursor.close()
        cnx.close()

        # Redirecionar para a página principal
        return redirect("/")

    # Se GET, exibir formulário vazio
    return render_template("form.html", titulo="Novo utilizador", utilizador=None)



# ---------------------------------------------------
# Rota para editar utilizador
# ---------------------------------------------------
@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar_utilizador(id):
    # Proteger a página
    if "user_id" not in session:
        return redirect(url_for("login"))

    cnx = ligar_bd()
    cursor = cnx.cursor(dictionary=True)

    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]

        # Atualizar dados no banco
        cursor2 = cnx.cursor()
        cursor2.execute(
            "UPDATE utilizador SET nome = %s, email = %s WHERE id = %s", 
            (nome, email, id)
        )
        cnx.commit()
        cursor2.close()

        cursor.close()
        cnx.close()
        return redirect("/")

    # Se GET, buscar dados do utilizador para preencher o formulário
    cursor.execute("SELECT id, nome, email FROM utilizador WHERE id = %s", (id,))
    utilizador = cursor.fetchone()

    cursor.close()
    cnx.close()

    return render_template("form.html", titulo="Editar utilizador", utilizador=utilizador)


# ---------------------------------------------------
# Rota para apagar utilizador
# ---------------------------------------------------
@app.route("/apagar/<int:id>", methods=["POST"])
def deleta_utilizador(id):
    # Proteger a página
    if "user_id" not in session:
        return redirect(url_for("login"))

    cnx = ligar_bd()
    cursor = cnx.cursor()

    # Apagar pelo ID
    cursor.execute("DELETE FROM utilizador WHERE id = %s", (id,))
    cnx.commit()

    cursor.close()
    cnx.close()

    return redirect("/")


# ---------------------------------------------------
# Login
# ---------------------------------------------------
app.secret_key = os.urandom(24)  # Chave secreta para a sessão

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        cnx = ligar_bd()
        cursor = cnx.cursor(dictionary=True)

        # Verificar se o utilizador existe
        cursor.execute(
            "SELECT id, username, password FROM login WHERE username = %s", (username,)
        )
        user = cursor.fetchone()

        cursor.close()
        cnx.close()

        # Validar senha
        if user and user["password"] == password:
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            return redirect(url_for("index"))
        else:
            flash("Username ou password incorretos.")
            return redirect(url_for("login"))

    # Se GET, exibir formulário de login
    return render_template("login.html")


# ---------------------------------------------------
# Logout
# ---------------------------------------------------
@app.route("/logout")
def logout():
    session.clear()  # Limpar sessão
    return redirect(url_for("login"))


# ---------------------------------------------------
# Iniciar o servidor Flask
# ---------------------------------------------------
app.run(debug=True)
