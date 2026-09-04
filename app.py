from datetime import datetime
import sqlite3
from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
# Chave de sessão necessária para exibir alertas de feedback (flash messages)
app.secret_key = "ecoponto_chave_secreta_academica_ufms"


def conectar_banco():
    conexao = sqlite3.connect("ecoponto.db")
    conexao.row_factory = sqlite3.Row
    return conexao


def inicializar_banco():
    conexao = conectar_banco()

    # Tabela de pontos de coleta
    conexao.execute("""
        CREATE TABLE IF NOT EXISTS pontos_coleta (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            endereco TEXT NOT NULL,
            bairro TEXT NOT NULL,
            cidade TEXT NOT NULL,
            materiais TEXT NOT NULL
        )
    """)

    # Tabela de sugestões enviadas pelos usuários
    conexao.execute("""
        CREATE TABLE IF NOT EXISTS sugestoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            mensagem TEXT NOT NULL,
            data_envio TEXT NOT NULL
        )
    """)

    total_pontos = conexao.execute(
        "SELECT COUNT(*) FROM pontos_coleta"
    ).fetchone()[0]

    # Preenche com dados iniciais de referência em Sonora - MS se estiver vazio
    if total_pontos == 0:
        conexao.executemany("""
            INSERT INTO pontos_coleta
            (nome, endereco, bairro, cidade, materiais)
            VALUES (?, ?, ?, ?, ?)
        """, [
            (
                "Gerência de Meio Ambiente (Prefeitura)",
                "Av. Marcelo Miranda Soares, 1077",
                "Centro",
                "Sonora - MS",
                "Celulares, computadores, cabos, fontes e placas de circuito"
            ),
            (
                "Secretaria de Obras e Serviços Urbanos",
                "Rua da Saudade, s/n",
                "Centro",
                "Sonora - MS",
                "Monitores, televisores antigos, impressoras e micro-ondas"
            ),
            (
                "Ponto de Coleta de Pilhas e Baterias",
                "Av. Edson Aparecido Fernandes de Campos, 650",
                "Centro",
                "Sonora - MS",
                "Pilhas alcalinas e comuns, baterias de celular e fones portáteis"
            )
        ])

    conexao.commit()
    conexao.close()


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/pontos")
def pontos():
    termo = request.args.get("busca", "").strip()
    conexao = conectar_banco()

    if termo:
        param = f"%{termo}%"
        consulta = """
            SELECT *
            FROM pontos_coleta
            WHERE nome LIKE ? 
               OR endereco LIKE ? 
               OR bairro LIKE ? 
               OR cidade LIKE ? 
               OR materiais LIKE ?
            ORDER BY nome
        """
        pontos_coleta = conexao.execute(
            consulta, (param, param, param, param, param)
        ).fetchall()
    else:
        pontos_coleta = conexao.execute(
            "SELECT * FROM pontos_coleta ORDER BY nome"
        ).fetchall()

    conexao.close()

    return render_template(
        "pontos.html",
        pontos=pontos_coleta,
        termo_busca=termo
    )


@app.route("/orientacoes")
def orientacoes():
    return render_template("orientacoes.html")


@app.route("/faq")
def faq():
    return render_template("faq.html")


@app.route("/sugestoes", methods=["GET", "POST"])
def sugestoes():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip()
        mensagem = request.form.get("mensagem", "").strip()

        if not nome or not email or not mensagem:
            flash("Por favor, preencha todos os campos do formulário.", "danger")
            return redirect(url_for("sugestoes"))

        data_hora = datetime.now().strftime("%d/%m/%Y às %H:%M")

        conexao = conectar_banco()
        conexao.execute("""
            INSERT INTO sugestoes (nome, email, mensagem, data_envio)
            VALUES (?, ?, ?, ?)
        """, (nome, email, mensagem, data_hora))
        conexao.commit()
        conexao.close()

        flash("Sua mensagem foi enviada com sucesso! Obrigado pela colaboração.", "success")
        return redirect(url_for("sugestoes"))

    return render_template("sugestoes.html")


if __name__ == "__main__":
    inicializar_banco()
    app.run(debug=True)