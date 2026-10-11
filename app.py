from datetime import datetime
from pathlib import Path
import os
import secrets
import sqlite3

from flask import Flask, flash, redirect, render_template, request, url_for


BASE_DIR = Path(__file__).resolve().parent
CAMINHO_BANCO = BASE_DIR / "ecoponto.db"
CAMINHO_SCHEMA = BASE_DIR / "database" / "schema.sql"
CAMINHO_DADOS = BASE_DIR / "database" / "dados_iniciais.sql"


app = Flask(__name__)

# O segredo de sessão pode ser definido no ambiente em uma implantação.
# Para uso acadêmico local, gera-se uma chave temporária por execução.
app.secret_key = os.environ.get("ECOPONTO_SECRET_KEY") or secrets.token_hex(32)


def conectar_banco():
    conexao = sqlite3.connect(CAMINHO_BANCO)
    conexao.row_factory = sqlite3.Row

    # Ativa o uso de chaves estrangeiras no SQLite
    conexao.execute("PRAGMA foreign_keys = ON")

    return conexao


def inicializar_banco():
    conexao = conectar_banco()

    # Cria as tabelas definidas no schema SQL
    with open(CAMINHO_SCHEMA, "r", encoding="utf-8") as arquivo:
        conexao.executescript(arquivo.read())

    total_pontos = conexao.execute(
        "SELECT COUNT(*) FROM pontos_coleta"
    ).fetchone()[0]

    # Insere os dados demonstrativos somente se o banco estiver vazio
    if total_pontos == 0:
        with open(CAMINHO_DADOS, "r", encoding="utf-8") as arquivo:
            conexao.executescript(arquivo.read())

    conexao.commit()
    conexao.close()


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/pontos")
def pontos():
    termo = request.args.get("busca", "").strip()
    conexao = conectar_banco()

    consulta_base = """
        SELECT
            p.id,
            p.nome,
            p.endereco,
            p.bairro,
            p.cidade,
            GROUP_CONCAT(m.nome, ', ') AS materiais
        FROM pontos_coleta p
        LEFT JOIN ponto_material pm
            ON pm.ponto_id = p.id
        LEFT JOIN materiais m
            ON m.id = pm.material_id
    """

    if termo:
        param = f"%{termo}%"

        consulta = consulta_base + """
            WHERE p.nome LIKE ?
               OR p.endereco LIKE ?
               OR p.bairro LIKE ?
               OR p.cidade LIKE ?
               OR EXISTS (
                    SELECT 1
                    FROM ponto_material pm_busca
                    INNER JOIN materiais m_busca
                        ON m_busca.id = pm_busca.material_id
                    WHERE pm_busca.ponto_id = p.id
                      AND m_busca.nome LIKE ?
               )
            GROUP BY
                p.id,
                p.nome,
                p.endereco,
                p.bairro,
                p.cidade
            ORDER BY p.nome
        """

        pontos_coleta = conexao.execute(
            consulta,
            (param, param, param, param, param)
        ).fetchall()

    else:
        consulta = consulta_base + """
            GROUP BY
                p.id,
                p.nome,
                p.endereco,
                p.bairro,
                p.cidade
            ORDER BY p.nome
        """

        pontos_coleta = conexao.execute(consulta).fetchall()

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
            flash(
                "Por favor, preencha todos os campos do formulário.",
                "danger"
            )
            return redirect(url_for("sugestoes"))

        data_hora = datetime.now().strftime("%d/%m/%Y às %H:%M")

        conexao = conectar_banco()

        conexao.execute("""
            INSERT INTO sugestoes (
                nome,
                email,
                mensagem,
                data_envio
            )
            VALUES (?, ?, ?, ?)
        """, (
            nome,
            email,
            mensagem,
            data_hora
        ))

        conexao.commit()
        conexao.close()

        flash(
            "Sua mensagem foi enviada com sucesso! Obrigado pela colaboração.",
            "success"
        )

        return redirect(url_for("sugestoes"))

    return render_template("sugestoes.html")


if __name__ == "__main__":
    inicializar_banco()
    # O depurador interativo não deve ficar ativado por padrão.
    app.run(debug=False)