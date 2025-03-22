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
URL = "https://www.amazon.com.br/que-importa-seu-resultado-potencialize/dp/6555440376/ref=sr_1_1_sspa?dib=eyJ2IjoiMSJ9.3dD30-1CcCM3jTOLmPcHI41RFeUB4X-mYRrMVlYlQqmwkeArb3lGk9P6MHePOHt_u_r-nbY4Y406n403S3goYeqUgm4pBIZgFesxB0hXvyTJPLXv4DqCfvOSwMF0zMM1_LBl0nhIuuZbPMIMOEgPiMiWOL_Orhvf2ndlzA-YxXRQybmoK8EdkDIIpHaalZzLzEY93iAObz6A3QrwdTMMq5fMTkpWud6RRbGhRRPCwkppolqFDd7z6VfqnL1-BM6EievRgtuHMgdeK9MuWZpW45cXjbFz5IIVDcv-EFJORh4.YTtcRKAUQk2FdnNLiVppK1fadTtnJOQ-brvfk5ddzug&dib_tag=se&keywords=produto&qid=1742667072&sr=8-1-spons&ufe=app_do%3Aamzn1.fos.6d798eae-cadf-45de-946a-f477d47705b9&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"

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
