import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
BANCO = BASE_DIR / "ecoponto.db"

conexao = sqlite3.connect(BANCO)
cursor = conexao.cursor()


print("=" * 60)
print("ECOPONTO DIGITAL - DEMONSTRAÇÃO CRUD - MÓDULO 3")
print("=" * 60)


# Limpeza preventiva caso algum teste anterior tenha ficado no banco
cursor.execute("""
    DELETE FROM materiais
    WHERE nome IN (
        'Material Teste Módulo 3',
        'Material Teste Módulo 3 Atualizado'
    )
""")
conexao.commit()


# =====================================================
# 1. INSERT
# =====================================================

print("\n1. INSERT")
print("-" * 60)

cursor.execute("""
    INSERT INTO materiais (nome)
    VALUES (?)
""", ("Material Teste Módulo 3",))

conexao.commit()

print("INSERT executado com sucesso.")
print("Registro inserido: Material Teste Módulo 3")

input("\nTire o print do INSERT e pressione ENTER para continuar...")


# =====================================================
# 2. SELECT
# =====================================================

print("\n2. SELECT")
print("-" * 60)

cursor.execute("""
    SELECT id, nome
    FROM materiais
    WHERE nome = ?
""", ("Material Teste Módulo 3",))

resultado = cursor.fetchall()

print("Resultado da consulta:")
for registro in resultado:
    print(registro)

input("\nTire o print do SELECT e pressione ENTER para continuar...")


# =====================================================
# 3. UPDATE
# =====================================================

print("\n3. UPDATE")
print("-" * 60)

cursor.execute("""
    UPDATE materiais
    SET nome = ?
    WHERE nome = ?
""", (
    "Material Teste Módulo 3 Atualizado",
    "Material Teste Módulo 3"
))

conexao.commit()

print("UPDATE executado com sucesso.")

cursor.execute("""
    SELECT id, nome
    FROM materiais
    WHERE nome = ?
""", ("Material Teste Módulo 3 Atualizado",))

resultado = cursor.fetchall()

print("Registro após atualização:")
for registro in resultado:
    print(registro)

input("\nTire o print do UPDATE e pressione ENTER para continuar...")


# =====================================================
# 4. DELETE
# =====================================================

print("\n4. DELETE")
print("-" * 60)

cursor.execute("""
    DELETE FROM materiais
    WHERE nome = ?
""", ("Material Teste Módulo 3 Atualizado",))

conexao.commit()

print("DELETE executado com sucesso.")

cursor.execute("""
    SELECT id, nome
    FROM materiais
    WHERE nome = ?
""", ("Material Teste Módulo 3 Atualizado",))

resultado = cursor.fetchall()

print("Resultado da consulta após exclusão:")
print(resultado)

conexao.close()

print("\nDemonstração CRUD finalizada.")