# 🤖 Chat com IA usando LangChain + Groq + Streamlit

Este projeto é uma aplicação de chat com inteligência artificial construída com Streamlit e LangChain, utilizando modelos da Groq API.

---

## 🚀 Instruções de Instalação

### 1. Criar um diretório do projeto

```bash
#Criando diretorio
mkdir chat-ia-groq
cd chat-ia-groq
```
---
### 2. Criando ambiente virtual
---
```bash
#Criando o ambiente virtual com Python
python -m venv env
source env/bin/activate  # Para Linux/Mac
# ou
env\Scripts\activate     # Para Windows
```

---
### 3. Instalando dependências
---
```bash 
#instalando dependencias
pip install -r requirements.txt
```

---
### 4. Criando arquivo .env
---
```bash
#Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:
GROQ_API_KEY="sua_chave_api_aqui"
```

---
### 5. Executando Projeto
---

```bash
#Após instalar as dependências e configurar sua chave de API, execute o seguinte comando:
streamlit run Chatmodels.py
```
