# Envio de Mensagens via WhatsApp com Supabase + Z-API

Projeto em Python que lê contatos cadastrados no Supabase e envia mensagens personalizadas via WhatsApp usando a Z-API.

---

## Setup da tabela no Supabase

No painel do Supabase, crie uma tabela chamada `contacts` com as colunas:

| Coluna   | Tipo   | Observação                        |
|----------|--------|-----------------------------------|
| id       | int8   | Primary Key, gerado automaticamente |
| nome     | text   | Not null                          |
| telefone | text   | Not null. Formato: 5511999999999  |

Ou rode direto no SQL Editor do Supabase:

```sql
create table if not exists contacts (
    id bigint generated always as identity primary key,
    nome text not null,
    telefone text not null
);
```

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
