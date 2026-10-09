INSERT INTO pontos_coleta (id, nome, endereco, bairro, cidade) VALUES
(
    1,
    'Gerência de Meio Ambiente (Prefeitura)',
    'Av. Marcelo Miranda Soares, 1077',
    'Centro',
    'Sonora - MS'
),
(
    2,
    'Secretaria de Obras e Serviços Urbanos',
    'Rua da Saudade, s/n',
    'Centro',
    'Sonora - MS'
),
(
    3,
    'Ponto de Coleta de Pilhas e Baterias',
    'Av. Edson Aparecido Fernandes de Campos, 650',
    'Centro',
    'Sonora - MS'
);

INSERT INTO materiais (id, nome) VALUES
(1, 'Celulares'),
(2, 'Computadores'),
(3, 'Cabos'),
(4, 'Fontes'),
(5, 'Placas de circuito'),
(6, 'Monitores'),
(7, 'Televisores antigos'),
(8, 'Impressoras'),
(9, 'Micro-ondas'),
(10, 'Pilhas alcalinas e comuns'),
(11, 'Baterias de celular'),
(12, 'Fones portáteis');

INSERT INTO ponto_material (ponto_id, material_id) VALUES
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(1, 5),

(2, 6),
(2, 7),
(2, 8),
(2, 9),

(3, 10),
(3, 11),
(3, 12);