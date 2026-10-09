import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
BANCO = BASE_DIR / "ecoponto.db"

conexao = sqlite3.connect(BANCO)
cursor = conexao.cursor()


print("=" * 65)
print("ECOPONTO DIGITAL - TABELAS E RELACIONAMENTOS - MÓDULO 3")
print("=" * 65)


print("\n1. TABELAS EXISTENTES")
print("-" * 65)

tabelas = cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
      AND name NOT LIKE 'sqlite_%'
    ORDER BY name
""").fetchall()

for tabela in tabelas:
    print(tabela[0])


input("\nTire o print das tabelas e pressione ENTER para continuar...")


print("\n2. RELACIONAMENTO ENTRE PONTOS E MATERIAIS")
print("-" * 65)

resultados = cursor.execute("""
    SELECT
        p.nome AS ponto_coleta,
        m.nome AS material
    FROM pontos_coleta p
    INNER JOIN ponto_material pm
        ON pm.ponto_id = p.id
    INNER JOIN materiais m
        ON m.id = pm.material_id
    ORDER BY p.nome, m.nome
""").fetchall()

for ponto, material in resultados:
    print(f"{ponto} -> {material}")


conexao.close()

print("\nConsulta de relacionamento finalizada.")