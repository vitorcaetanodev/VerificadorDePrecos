import requests
from bs4 import BeautifulSoup
import smtplib

# Configurações do produto
URL = "https://www.amazon.com.br/dp/B0B5F4M5YF"
HEADERS = {"User-Agent": "Mozilla/5.0"}
PRECO_ALVO = 1500.00  # Defina o preço desejado

# Função para buscar o preço
def verificar_preco():
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")
    
    preco_str = soup.find("span", {"class": "a-price-whole"}).get_text()
    preco_atual = float(preco_str.replace(".", "").replace(",", "."))  # Convertendo para número

    if preco_atual <= PRECO_ALVO:
        enviar_email(preco_atual)

# Função para enviar alerta por e-mail
def enviar_email(preco_atual):
    remetente = "seuemail@gmail.com"
    senha = "sua_senha"
    destinatario = "destinatario@gmail.com"
    
    mensagem = f"🔥 O preço caiu! Agora está R$ {preco_atual}. Compre agora: {URL}"
    
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(remetente, senha)
        server.sendmail(remetente, destinatario, f"Subject: Alerta de Preço\n\n{mensagem}")

# Executar a verificação
verificar_preco()
