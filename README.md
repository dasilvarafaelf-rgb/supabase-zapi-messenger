# Envio de Mensagens via WhatsApp com Supabase + Z-API

Projeto em Python que lê contatos cadastrados no Supabase e envia mensagens personalizadas via WhatsApp usando a Z-API.

---

## Setup da tabela no Supabase

No painel do Supabase, crie uma tabela chamada `contacts` com as colunas:

| Coluna    | Tipo | Observação       |
|-----------|------|------------------|
| id        | int8 | Primary Key      |
| nome      | text |                  |
| telefone  | text | Formato: 5511999999999 |

---

## Variáveis de ambiente (.env)

Crie um arquivo `.env` na raiz do projeto com base no `.env.example`:

```
SUPABASE_URL=https://seu-projeto.supabase.co
SUPABASE_KEY=sua_anon_key
ZAPI_INSTANCE_ID=seu_instance_id
ZAPI_TOKEN=seu_token
ZAPI_CLIENT_TOKEN=seu_client_token
```

## Como rodar

```bash
pip install -r requirements.txt
python main.py
```
