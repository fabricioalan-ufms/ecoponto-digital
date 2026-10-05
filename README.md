# ♻️ EcoPonto Digital — Sonora/MS

Aplicação web desenvolvida como MVP acadêmico para a disciplina de **Projeto Integrador de Tecnologia da Informação II**, do curso de **Tecnologia da Informação da Universidade Federal de Mato Grosso do Sul (UFMS)**.

O EcoPonto Digital utiliza tecnologia web para facilitar o acesso a informações relacionadas ao descarte correto de resíduos eletroeletrônicos e à localização de pontos de recebimento.

---

## 📌 Contexto e problema

O descarte inadequado de Resíduos de Equipamentos Eletroeletrônicos (REEE) representa um problema ambiental e social.

Celulares, computadores, carregadores, cabos, baterias, pilhas e outros equipamentos não devem ser descartados juntamente com os resíduos domésticos comuns.

Além do problema ambiental, existe a dificuldade de encontrar, de maneira simples e centralizada, informações sobre:

* locais adequados para descarte;
* materiais aceitos em cada ponto;
* logística reversa;
* cuidados antes do descarte;
* orientações ambientais.

O projeto busca responder a essa necessidade por meio de uma aplicação web simples e acessível.

---

## 💡 Solução proposta

O **EcoPonto Digital** é um MVP (*Minimum Viable Product* — Produto Mínimo Viável) que centraliza informações relacionadas ao descarte de resíduos eletroeletrônicos.

A aplicação permite ao usuário:

* localizar pontos de recebimento;
* pesquisar locais cadastrados;
* consultar materiais aceitos;
* visualizar a região por meio do Google Maps;
* acessar orientações de descarte;
* consultar perguntas frequentes;
* enviar sugestões.

O objetivo não é substituir órgãos públicos, empresas ou sistemas oficiais de logística reversa, mas demonstrar como uma solução tecnológica pode facilitar o acesso da comunidade às informações.

---

## ⚠️ Aviso sobre os pontos de coleta

> **Os pontos apresentados nesta versão são utilizados para fins de demonstração acadêmica do MVP EcoPonto Digital.**
>
> A disponibilização pública da aplicação dependerá da validação das informações junto aos responsáveis pelos locais de recebimento.

Portanto, os registros utilizados no sistema não devem ser considerados automaticamente como pontos oficialmente homologados ou atualmente disponíveis para recebimento de resíduos.

---

## 🚀 Funcionalidades

### 🗺️ Mapa da região

Visualização integrada da região urbana de **Sonora - MS** utilizando Google Maps.

### 🔎 Pesquisa de pontos de coleta

Permite pesquisar os registros disponíveis utilizando informações como:

* nome;
* bairro;
* cidade;
* material aceito.

### 📍 Pontos de coleta

Os pontos são apresentados por meio de cards contendo informações como:

* nome do local;
* endereço;
* bairro;
* cidade;
* materiais recebidos.

### 🧭 Integração com Google Maps

Cada ponto possui acesso ao Google Maps para facilitar a localização e consulta do endereço informado.

### ♻️ Orientações sobre descarte

Área educativa com informações relacionadas a:

* descarte correto;
* cuidados ambientais;
* resíduos eletrônicos;
* pilhas e baterias;
* segurança das informações pessoais;
* logística reversa.

### ❓ Perguntas frequentes — FAQ

Página com respostas para dúvidas comuns relacionadas ao descarte de equipamentos eletrônicos.

### 💬 Sugestões

Formulário para que usuários possam registrar contribuições e sugestões relacionadas ao projeto.

As informações são armazenadas localmente utilizando SQLite.

### 📱 Layout responsivo

A interface foi desenvolvida para se adaptar a:

* computadores;
* notebooks;
* tablets;
* smartphones.

---

## 🛠️ Tecnologias utilizadas

### Back-end

* **Python**
* **Flask**
* **SQLite3**

### Front-end

* **HTML5**
* **CSS3**
* **Bootstrap 5**
* **Bootstrap Icons**

### Interface

* **Plus Jakarta Sans — Google Fonts**
* Design responsivo
* Componentes personalizados em CSS

### Serviços externos

* **Google Maps**

---

## 🧩 Requisitos funcionais principais

* **RF01** — Exibir informações sobre descarte correto de resíduos eletrônicos.
* **RF02** — Permitir consultar pontos de coleta cadastrados.
* **RF03** — Permitir pesquisar pontos por nome, cidade ou bairro.
* **RF04** — Informar os materiais aceitos em cada ponto.
* **RF05** — Disponibilizar perguntas frequentes.
* **RF06** — Permitir envio de sugestões.
* **RF07** — Armazenar informações necessárias em banco de dados.
* **RF08** — Armazenar as sugestões enviadas pelos usuários.

---

## ⚙️ Requisitos não funcionais principais

* Interface responsiva.
* Navegação simples e intuitiva.
* Compatibilidade com navegadores modernos.
* Persistência de informações utilizando SQLite.
* Organização do código-fonte.
* Documentação de instalação e execução.
* Uso de tecnologias web amplamente disponíveis.

---

## 📂 Estrutura do projeto

```text
EcoPontoDigital/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── static/
│   └── css/
│       └── style.css
│
└── templates/
    ├── index.html
    ├── pontos.html
    ├── orientacoes.html
    ├── faq.html
    └── sugestoes.html
```

### Descrição dos principais arquivos

| Arquivo/Pasta      | Finalidade                                            |
| ------------------ | ----------------------------------------------------- |
| `app.py`           | Aplicação Flask, rotas, consultas e regras do sistema |
| `requirements.txt` | Dependências necessárias para executar o projeto      |
| `templates/`       | Páginas HTML processadas pelo Flask                   |
| `static/css/`      | Arquivos responsáveis pela estilização                |
| `ecoponto.db`      | Banco SQLite criado/utilizado localmente              |
| `README.md`        | Documentação do projeto                               |
| `.gitignore`       | Define arquivos que não devem ser enviados ao Git     |

---

# ▶️ Como executar

## 1. Pré-requisitos

É necessário possuir:

* Python 3 instalado;
* pip;
* navegador web;
* Git, caso deseje clonar o repositório.

Para conferir o Python:

```bash
python --version
```

---

## 2. Clonar o repositório

Depois que o projeto estiver publicado no GitHub:

```bash
git clone https://github.com/fabricioalan-ufms/ecoponto-digital
```

Entre na pasta:

```bash
cd EcoPontoDigital
```

> Substitua `<URL_DO_REPOSITORIO>` pelo endereço real do projeto no GitHub.

---

## 3. Criar o ambiente virtual

No Windows:

```powershell
python -m venv venv
```

---

## 4. Ativar o ambiente virtual

No PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Caso o PowerShell bloqueie a execução do script, utilize primeiro:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Depois:

```powershell
.\venv\Scripts\Activate.ps1
```

Quando estiver ativo, o terminal deverá apresentar algo semelhante a:

```text
(venv) PS C:\...\EcoPontoDigital>
```

---

## 5. Instalar as dependências

Execute:

```powershell
pip install -r requirements.txt
```

As principais dependências utilizadas pelo projeto são Flask e seus componentes necessários.

---

## 6. Executar a aplicação

Execute:

```powershell
python app.py
```

O terminal deverá apresentar endereço semelhante a:

```text
http://127.0.0.1:5000
```

---

## 7. Acessar o sistema

Abra no navegador:

```text
http://127.0.0.1:5000
```

A página inicial do EcoPonto Digital será exibida.

---

# 🧪 Utilização

## Consultar pontos de coleta

Acesse:

```text
/pontos
```

ou utilize a opção **Pontos de Coleta** no menu principal.

---

## Pesquisar

Na página de pontos de coleta, utilize o campo de busca para procurar registros relacionados ao termo informado.

Exemplos:

```text
pilhas
```

```text
celular
```

```text
Centro
```

---

## Orientações

Acesse a opção:

```text
Orientações
```

para visualizar informações relacionadas ao descarte correto.

---

## FAQ

A opção:

```text
FAQ
```

apresenta respostas para dúvidas frequentes.

---

## Sugestões

Na página:

```text
Sugestões
```

o usuário pode preencher o formulário disponibilizado pela aplicação.

---

# 📱 Responsividade

O projeto utiliza Bootstrap e CSS personalizado para adaptação da interface a diferentes tamanhos de tela.

A aplicação pode ser utilizada em:

* desktop;
* notebook;
* tablet;
* smartphone.

---

# 🗃️ Banco de dados

O projeto utiliza **SQLite** por sua simplicidade e adequação a um MVP acadêmico.

O banco permite armazenar informações necessárias para funcionamento local da aplicação.

O arquivo:

```text
ecoponto.db
```

não é versionado no GitHub por estar incluído no `.gitignore`.

A aplicação pode criar sua estrutura local durante a execução conforme as configurações implementadas no projeto.

---

## 📊 Levantamento exploratório com a comunidade

Como complemento à identificação do problema, foi realizado um levantamento exploratório por meio de formulário eletrônico com o objetivo de compreender como moradores de Sonora/MS lidam com o descarte de resíduos eletrônicos e com a busca por informações sobre locais adequados de recebimento.

O formulário recebeu 42 respostas. Destas, 32 foram de participantes que declararam residir em Sonora/MS e foram consideradas prioritariamente na análise da problemática local.

Entre os moradores de Sonora/MS participantes da pesquisa:

- 78,1% afirmaram não saber onde realizar corretamente o descarte ou possuir dúvidas;
- 75% afirmaram não conhecer um ponto de recebimento de lixo eletrônico no município;
- 53,1% afirmaram já ter enfrentado dificuldade para encontrar informações sobre descarte;
- 84,4% consideraram útil ou muito útil a existência de uma solução digital que reúna informações sobre descarte correto e pontos de recebimento;
- 78,1% indicaram interesse em encontrar informações sobre locais de descarte.

Os dados foram analisados de forma agrupada, preservando a identidade dos participantes. O levantamento possui caráter exploratório e foi utilizado como apoio à análise da necessidade e ao desenvolvimento acadêmico do MVP EcoPonto Digital.

# 📊 Escopo do MVP

O MVP foi propositalmente mantido simples.

Foram priorizados recursos capazes de demonstrar o funcionamento da solução sem adicionar complexidade desnecessária.

## Incluído no MVP

* consulta de pontos;
* busca;
* mapa;
* orientações;
* FAQ;
* sugestões;
* responsividade;
* persistência local.

## Recursos possíveis para versões futuras

* painel administrativo;
* autenticação de administradores;
* validação e atualização automática dos pontos;
* geolocalização do usuário;
* cálculo automático de distância;
* integração com APIs oficiais;
* cadastro de novos pontos por instituições;
* notificações sobre campanhas de coleta;
* aplicação mobile.

---

# 🎯 Objetivo acadêmico

O projeto busca aplicar conhecimentos relacionados a:

* desenvolvimento web;
* engenharia de requisitos;
* banco de dados;
* experiência do usuário;
* responsividade;
* desenvolvimento de MVP;
* sustentabilidade;
* resolução de problemas utilizando Tecnologia da Informação.

A proposta também busca relacionar conhecimentos acadêmicos a uma demanda social e ambiental.

---

# 🎓 Projeto acadêmico

Projeto desenvolvido no contexto da disciplina:

**Projeto Integrador de Tecnologia da Informação II**

Universidade Federal de Mato Grosso do Sul — **UFMS**

Curso: **Tecnologia da Informação**

---

## ♻️ EcoPonto Digital

**Tecnologia aplicada à informação, sustentabilidade e descarte responsável.**
