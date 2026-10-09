-- =====================================================
-- EcoPonto Digital
-- Demonstração de operações CRUD - Módulo 3
-- =====================================================

-- CREATE / INSERT
-- Insere um registro temporário para demonstração.
INSERT INTO materiais (nome)
VALUES ('Material Teste Módulo 3');


-- READ / SELECT
-- Consulta o registro criado.
SELECT
    id,
    nome
FROM materiais
WHERE nome = 'Material Teste Módulo 3';


-- UPDATE
-- Atualiza o nome do registro temporário.
UPDATE materiais
SET nome = 'Material Teste Módulo 3 Atualizado'
WHERE nome = 'Material Teste Módulo 3';


-- READ APÓS UPDATE
-- Confirma a atualização.
SELECT
    id,
    nome
FROM materiais
WHERE nome = 'Material Teste Módulo 3 Atualizado';


-- DELETE
-- Remove o registro temporário.
DELETE FROM materiais
WHERE nome = 'Material Teste Módulo 3 Atualizado';


-- READ APÓS DELETE
-- Confirma que o registro foi removido.
SELECT
    id,
    nome
FROM materiais
WHERE nome = 'Material Teste Módulo 3 Atualizado';