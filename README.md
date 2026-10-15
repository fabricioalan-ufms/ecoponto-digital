# EcoPonto Digital

Aplicação web para consulta de pontos demonstrativos de recebimento de resíduos eletroeletrônicos e orientações sobre descarte responsável.

Projeto acadêmico desenvolvido ao longo dos **Projetos Integradores de Tecnologia da Informação I, II e III** da **Universidade Federal de Mato Grosso do Sul (UFMS)**, com foco em **Sonora - MS**.

**Aplicação online:** [fabricioalanufms.pythonanywhere.com](https://fabricioalanufms.pythonanywhere.com/)  
**Código-fonte:** [GitHub — ecoponto-digital](https://github.com/fabricioalan-ufms/ecoponto-digital)

## Sobre o projeto

O EcoPonto Digital é um MVP construído com Flask e SQLite. A aplicação reúne informações educativas, materiais associados a pontos cadastrados e um canal de sugestões.

> **Dados demonstrativos:** os pontos exibidos não foram validados como locais oficiais de recebimento. Os endereços não devem ser utilizados como confirmação de que um estabelecimento recebe resíduos eletrônicos.

## Funcionalidades

- Consulta e pesquisa de pontos por nome, endereço, bairro, cidade ou material.
- Visualização dos materiais associados a cada ponto cadastrado.
- Integração com Google Maps para consulta de endereços e rotas.
- Orientações sobre descarte e proteção de dados pessoais.
- Perguntas frequentes (FAQ).
- Formulário de sugestões com persistência em SQLite.
- Interface responsiva para computadores e dispositivos móveis.

## Tecnologias

| Área | Ferramentas |
| --- | --- |
| Back-end | Python, Flask |
| Banco de dados | SQLite |
| Interface | HTML5, CSS3, Bootstrap, Jinja2 |
| Integração externa | Google Maps |
| Qualidade e versionamento | unittest, Git, GitHub |

## Evolução do projeto

| Etapa | Entregas principais |
| --- | --- |
| **Projeto Integrador I** | Análise do problema e levantamento inicial de requisitos. |
| **Projeto Integrador II** | Desenvolvimento do MVP, modelagem do banco relacional, documentação e testes funcionais. |
| **Projeto Integrador III** | Inspeção dos artefatos, correções, plano de testes, plano de desenvolvimento seguro e plano de CI/CD. |

No Projeto Integrador II, foram registrados **8 testes automatizados e 12 verificações funcionais manuais**, aprovados nos cenários avaliados. Os planos de segurança e CI/CD elaborados no Projeto Integrador III descrevem propostas de evolução; sua elaboração não significa que todos os controles e pipelines estejam implantados.

## Estrutura do repositório

```text
ecoponto-digital/
├── app.py
├── database/
│   ├── schema.sql
│   ├── dados_iniciais.sql
│   └── ...
├── docs/
├── static/
│   └── css/
├── templates/
│   ├── index.html
│   ├── pontos.html
│   ├── orientacoes.html
│   ├── faq.html
│   └── sugestoes.html
├── tests/
│   └── test_ecoponto.py
├── .gitignore
├── requirements.txt
└── README.md
```

O banco relacional contém quatro tabelas: `pontos_coleta`, `materiais`, `ponto_material` e `sugestoes`. A tabela `ponto_material` representa o relacionamento muitos-para-muitos entre pontos e materiais. O arquivo local `ecoponto.db` não deve ser publicado quando contiver dados de usuários.

## Executar localmente

**Pré-requisitos:** Python 3, pip e Git.

No PowerShell do Windows:

```powershell
git clone https://github.com/fabricioalan-ufms/ecoponto-digital.git
cd ecoponto-digital
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Acesse `http://127.0.0.1:5000` no navegador.

A execução por `python app.py` inicializa o banco SQLite com os dados demonstrativos, quando necessário. Em hospedagens WSGI, a inicialização deve ser configurada separadamente.

## Testes automatizados

Execute na raiz do repositório:

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```

Os oito testes cobrem carregamento das páginas, pontos iniciais, pesquisa, validação do formulário, persistência de sugestões e integridade relacional. Cada teste utiliza um banco SQLite temporário.

## Publicação e limitações

A versão demonstrativa tem endereço público no PythonAnywhere, que fornece o ambiente de execução da aplicação Flask. O GitHub mantém o código-fonte e o histórico de versões; o GitHub Pages, isoladamente, não executa Python nem SQLite.

A hospedagem exige cuidados com a persistência e o backup do SQLite, o tratamento dos dados enviados pelo formulário e as configurações de segurança. Mesmo com o site acessível publicamente, os pontos cadastrados continuam **demonstrativos e não validados** como locais oficiais de recebimento.

## Autor

**Fabricio Alan Rocha** — Tecnologia da Informação, UFMS.

[Repositório no GitHub](https://github.com/fabricioalan-ufms/ecoponto-digital)
