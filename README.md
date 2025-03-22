# 📌 Amazon Price Tracker  
> Um bot simples em Python que monitora o preço de produtos na Amazon e envia alertas por e-mail quando houver uma queda de preço.

## 🚀 Descrição  
Este script acessa a página de um produto na Amazon, extrai o preço atual e o compara com um preço-alvo definido.  
Caso o preço caia abaixo do valor desejado, ele envia uma notificação por e-mail automaticamente.  

---

## 🛠 Tecnologias Utilizadas  
- 🐍 **Python 3.x**  
- 🌐 **Requests** (para fazer requisições HTTP)  
- 🔎 **BeautifulSoup4** (para extração de dados da página)  
- ✉️ **smtplib** (para envio de e-mails)  

---

## 📦 Instalação e Uso  

### 🔹 1️⃣ Clonar o repositório  
```bash
git clone https://github.com/seu-usuario/amazon-price-tracker.git
cd amazon-price-tracker

```
2️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```

🔹 3️⃣ Configurar o script

# URL do produto na Amazon
URL = "https://www.amazon.com.br/dp/B0B5F4M5YF"

# Preço alvo desejado
PRECO_ALVO = 1500.00  

# Credenciais do e-mail (configure seu e-mail e senha)
remetente = "seuemail@gmail.com"
senha = "sua_senha"
destinatario = "destinatario@gmail.com"


🔹 4️⃣ Executar o script

```bash

python tracker.py

```
