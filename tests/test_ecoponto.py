
import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import app as ecoponto


class TestesEcoPonto(unittest.TestCase):

    def setUp(self):
        # Cada teste utiliza um banco temporário independente.
        self.pasta_temporaria = tempfile.TemporaryDirectory()
        banco_teste = Path(self.pasta_temporaria.name) / "teste.db"

        self.patch_banco = patch.object(
            ecoponto,
            "CAMINHO_BANCO",
            banco_teste
        )
        self.patch_banco.start()

        ecoponto.app.config.update(TESTING=True)
        ecoponto.inicializar_banco()
        self.cliente = ecoponto.app.test_client()

    def tearDown(self):
        self.patch_banco.stop()
        self.pasta_temporaria.cleanup()

    def test_01_paginas_principais(self):
        paginas = [
            "/",
            "/pontos",
            "/orientacoes",
            "/faq",
            "/sugestoes"
        ]

        for pagina in paginas:
            with self.subTest(pagina=pagina):
                resposta = self.cliente.get(pagina)
                self.assertEqual(resposta.status_code, 200)

    def test_02_tres_pontos_iniciais(self):
        conexao = ecoponto.conectar_banco()
        quantidade = conexao.execute(
            "SELECT COUNT(*) FROM pontos_coleta"
        ).fetchone()[0]
        conexao.close()

        self.assertEqual(quantidade, 3)

    def test_03_pesquisa_pilhas(self):
        resposta = self.cliente.get("/pontos?busca=pilhas")

        self.assertEqual(resposta.status_code, 200)
        self.assertIn(
            b"Ponto de Coleta de Pilhas e Baterias",
            resposta.data
        )

    def test_04_pesquisa_computadores(self):
        resposta = self.cliente.get(
            "/pontos?busca=computadores"
        )

        self.assertEqual(resposta.status_code, 200)
        self.assertIn(
            "Gerência de Meio Ambiente".encode("utf-8"),
            resposta.data
        )

    def test_05_pesquisa_sem_resultado(self):
        resposta = self.cliente.get(
            "/pontos?busca=material_inexistente_999"
        )

        self.assertEqual(resposta.status_code, 200)
        self.assertNotIn(
            b"Ponto de Coleta de Pilhas e Baterias",
            resposta.data
        )

    def test_06_formulario_vazio(self):
        resposta = self.cliente.post(
            "/sugestoes",
            data={
                "nome": "",
                "email": "",
                "mensagem": ""
            },
            follow_redirects=True
        )

        self.assertEqual(resposta.status_code, 200)

        conexao = ecoponto.conectar_banco()
        quantidade = conexao.execute(
            "SELECT COUNT(*) FROM sugestoes"
        ).fetchone()[0]
        conexao.close()

        self.assertEqual(quantidade, 0)

    def test_07_formulario_valido(self):
        resposta = self.cliente.post(
            "/sugestoes",
            data={
                "nome": "Teste Academico",
                "email": "teste@exemplo.com",
                "mensagem": "Teste automatizado do Modulo 4."
            },
            follow_redirects=True
        )

        self.assertEqual(resposta.status_code, 200)

        conexao = ecoponto.conectar_banco()
        registro = conexao.execute(
            "SELECT nome, email, mensagem FROM sugestoes"
        ).fetchone()
        conexao.close()

        self.assertIsNotNone(registro)
        self.assertEqual(registro["nome"], "Teste Academico")
        self.assertEqual(registro["email"], "teste@exemplo.com")

    def test_08_integridade_relacional(self):
        conexao = ecoponto.conectar_banco()

        erros = conexao.execute(
            "PRAGMA foreign_key_check"
        ).fetchall()

        total_relacoes = conexao.execute(
            "SELECT COUNT(*) FROM ponto_material"
        ).fetchone()[0]

        conexao.close()

        self.assertEqual(erros, [])
        self.assertEqual(total_relacoes, 12)


if __name__ == "__main__":
    unittest.main()
