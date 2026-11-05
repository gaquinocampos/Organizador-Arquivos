# Organizador-Arquivos

**Automação de Processos e Organização de Arquivos com Python**

---

## Sobre o Projeto

O **AutoFile Organizer** nasceu da necessidade de resolver um problema comum do dia a dia: pastas de downloads e diretórios de trabalho lotados de arquivos misturados.

Trata-se de um script em Python que lê o conteúdo de uma pasta específica, identifica o formato de cada arquivo pelas extensões (`.pdf`, `.png`, `.py`, etc.) e os distribui automaticamente em subdiretórios categorizados. A ideia é eliminar o trabalho manual de arrastar arquivos e manter o ambiente limpo com poucas linhas de código.

---

## Objetivos

* **Automatizar rotinas:** Eliminar o trabalho repetitivo de classificar e mover arquivos manualmente.
* **Organização estruturada:** Manter diretórios locais limpos e previsíveis.
* **Simplicidade técnica:** Utilizar apenas bibliotecas nativas do Python, dispensando instalações complexas de dependências externas.

---

## Funcionalidades

* [x] **`setup_dirs()`:** Verifica se as pastas de categorias (Documentos, Imagens, Códigos, Outros) existem e as cria caso necessário.
* [x] **`organizar()`:** Varre o diretório alvo, lê a extensão de cada arquivo e executa a movimentação para o destino correto.

---

## Tecnologias Utilizadas

* **[Python](https://www.python.org/):** Linguagem utilizada para estruturar a lógica de varredura e movimentação.
* **`os` & `shutil`:** Módulos padrão da biblioteca do Python focados na manipulação de caminhos e operações do sistema de arquivos.
* **[Git](https://git-scm.com/) & [GitHub](https://github.com/):** Ferramentas de controle de versão e hospedagem do código.

---

## Estrutura do Repositório

```text
.
├── organizador.py         # Script principal de automação
├── meus_arquivos/         # Pasta alvo simulada para testes
└── README.md              # Documentação oficial do projeto

```
