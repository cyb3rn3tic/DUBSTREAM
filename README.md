# DUBSTREAM ⚡

> **Addon de Streaming para Stremio focado em conteúdo dublado com interface otimizada e player profissional.**

O **DUBSTREAM** é um projeto desenvolvido como parte da jornada de estudos em **Sistemas de Informação**, utilizando uma arquitetura moderna baseada em microserviços, conteinerização e deploy automatizado em nuvem.

---

## 🚀 Instalação Rápida

Para instalar este addon no seu Stremio, utilize o link do manifesto abaixo:

[![Install Stremio Addon](https://img.shields.io/badge/Instalar%20no-Stremio-blueviolet?style=for-the-badge&logo=stremio)](stremio://dubstream.onrender.com/manifest.json)

**Link do Manifesto (Copie e cole no Stremio):**
https://dubstream.onrender.com/manifest.json

### 🛠️ Como instalar manualmente:
1. Abra o seu aplicativo **Stremio**.
2. Vá até a aba de **Addons** (ícone de peça de quebra-cabeça).
3. Cole o link do manifesto na barra de pesquisa superior.
4. Clique em **Instalar**.

---

## ✨ Diferenciais do Projeto

* **Player Customizado:** Interface de transição com *loader* dinâmico para uma experiência de usuário (UX) mais fluida.
* **Performance Elevada:** Desenvolvido com **FastAPI**, garantindo baixa latência nas requisições.
* **Infraestrutura em Nuvem:** Totalmente conteinerizado com **Docker** e hospedado no **Render**.
* **Deploy Contínuo (CI/CD):** Sincronização automática entre o repositório GitHub e o servidor de produção.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** [Python 3.11+](https://www.python.org/)
* **Framework Web:** [FastAPI](https://fastapi.tiangolo.com/)
* **Servidor ASGI:** [Uvicorn](https://www.uvicorn.org/)
* **Template Engine:** [Jinja2](https://jinja.palletsprojects.com/)
* **Container:** [Docker](https://www.docker.com/)
* **Hospedagem:** [Render](https://render.com/)

---

## 📁 Estrutura do Repositório

SKYFLIX/
├── templates/          # Interface do player (HTML/CSS/JS)
├── app.py              # Lógica da API e rotas do Manifesto
├── Dockerfile          # Instruções de montagem do container Linux
├── requirements.txt    # Dependências do projeto
└── LICENSE             # Licença de uso (GPLv3)

---

## 📜 Licença

Este projeto está licenciado sob a **GNU General Public License v3.0 (GPLv3)**. Você pode redistribuí-lo e/ou modificá-lo sob os termos da licença, garantindo que o código permaneça sempre aberto.

---
**Desenvolvido por Osmar Steffen** 🎓  