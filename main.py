from supabase import create_client
from dotenv import load_dotenv
import requests
import os

load_dotenv()

# ======================
# SUPABASE
# ======================

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

# ======================
# Z-API
# ======================

INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
TOKEN = os.getenv("ZAPI_TOKEN")
CLIENT_TOKEN = os.getenv("ZAPI_CLIENT_TOKEN")

URL = f"https://api.z-api.io/instances/{INSTANCE_ID}/token/{TOKEN}/send-text"

HEADERS = {
    "Client-Token": CLIENT_TOKEN,
    "Content-Type": "application/json"
}

# ======================
# BUSCA CONTATOS
# ======================

response = (
    supabase
    .table("contacts")
    .select("*")
    .limit(3)
    .execute()
)

contacts = response.data

if not contacts:
    print("[AVISO] Nenhum contato encontrado no banco de dados.")
    exit()

print(f"[INFO] {len(contacts)} contato(s) encontrado(s).\n")

# ======================
# ENVIA MENSAGENS
# ======================

for contact in contacts:

    nome = contact.get("nome", "desconhecido")
    telefone = contact.get("telefone", "")

    if not telefone:
        print(f"[AVISO] Contato '{nome}' sem telefone. Pulando...")
        continue

    mensagem = f"Olá, {nome} tudo bem com você?"

    payload = {
        "phone": telefone,
        "message": mensagem
    }

    try:
        resp = requests.post(URL, json=payload, headers=HEADERS)

        print(f"Status: {resp.status_code} | Resposta: {resp.text}")

        if resp.status_code == 200:
            print(f"[SUCESSO] Mensagem enviada para {nome} ({telefone})")
        else:
            print(
                f"[ERRO] Falha ao enviar para {nome} - "
                f"Status: {resp.status_code} - {resp.text}"
            )

    except Exception as e:
        print(f"[ERRO] Exceção ao enviar para {nome}: {e}")
