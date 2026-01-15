# ---------------------------------------------------
# Imports
# ---------------------------------------------------
from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector
import os
import requests
import json

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
app.secret_key = os.urandom(24)  # Chave secreta para a sessão


@app.route("/")
def base():
    if "user_id" not in session:
        return redirect(url_for("login"))
    
    return render_template("base.html") 

    
# ---------------------------------------------------
# Rota principal (lista utilizadores)
# ---------------------------------------------------
@app.route("/index")
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


@app.route("/metereologia", methods=["GET", "POST"])
def metereologia():
    if "user_id" not in session:
        return redirect(url_for("login"))

    temperature = None
    error = None
    cidade = None

    if request.method == "POST":
        cidade = request.form.get("cidade")

        if cidade:
            API_KEY = "3689129ee7af0fa500cad990971aecd6"
            link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

            requisicao = requests.get(link)
            requisicao_dic = requisicao.json()

            if requisicao_dic.get("cod") != 200:
                error = "Cidade não encontrada"
            else:
                kelvin = requisicao_dic["main"]["temp"]
                temperature = round(kelvin - 273.15, 2)

    return render_template("weather.html", temperature=temperature, cidade=cidade, error=error)


@app.route("/cotacao", methods=["GET", "POST"])
def cotacao():
    if "user_id" not in session:
        return redirect(url_for("login"))

    usd_brl = None
    eur_brl = None
    error = None

    if request.method == "POST":

        link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

        try:
            requisicao = requests.get(link)

            # Verificar se a requisição HTTP retornou com sucesso
            if requisicao.status_code != 200:
                error = "Erro ao contactar API."
            else:
                dados = requisicao.json()

                # Verificando se os dados esperados existem
                if "USDBRL" in dados and "EURBRL" in dados:
                    usd_brl = dados["USDBRL"]["bid"]
                    eur_brl = dados["EURBRL"]["bid"]
                else:
                    error = "Dados não encontrados na resposta da API."

        except Exception as e:
            error = "Erro inesperado ao buscar dados."

    return render_template("money.html", usd_brl=usd_brl, eur_brl=eur_brl, error=error)


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
def registrar_usuario():
    
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            flash("Preencha todos os campos!")
            return redirect(url_for("registrar_usuario"))

        # Conectar ao banco
        cnx = ligar_bd()
        cursor = cnx.cursor()

        # Verificar se o usuário já existe
        cursor.execute(
            "SELECT id FROM login WHERE username = %s", (username,)
        )
        existe = cursor.fetchone()

        if existe:
            flash("Este nome de usuário já está em uso!")
            cursor.close()
            cnx.close()
            return redirect(url_for("registrar_usuario"))

        # Inserir novo usuário
        cursor.execute(
            "INSERT INTO login (username, password) VALUES (%s, %s)",
            (username, password)
        )
        cnx.commit()

        cursor.close()
        cnx.close()

        flash("Conta criada com sucesso! Faça login.")
        return redirect(url_for("login"))

    return render_template("register.html")


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
            return redirect(url_for("base"))
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
