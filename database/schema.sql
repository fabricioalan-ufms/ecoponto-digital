PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS pontos_coleta (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    endereco TEXT NOT NULL,
    bairro TEXT NOT NULL,
    cidade TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS materiais (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS ponto_material (
    ponto_id INTEGER NOT NULL,
    material_id INTEGER NOT NULL,

    PRIMARY KEY (ponto_id, material_id),

    FOREIGN KEY (ponto_id)
        REFERENCES pontos_coleta(id)
        ON DELETE CASCADE,

    FOREIGN KEY (material_id)
        REFERENCES materiais(id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS sugestoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    mensagem TEXT NOT NULL,
    data_envio TEXT NOT NULL
);