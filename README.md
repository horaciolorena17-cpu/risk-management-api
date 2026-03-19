# risk-management-api
API para gerenciamento de riscos de segurança da informação (Projeto Integrador)
# Risk Management API

API desenvolvida em Python para gerenciamento de riscos de segurança da informação.

## Funcionalidades
- Cadastro de riscos
- Classificação automática (baixo, médio, alto)
- Listagem de riscos

## Como executar

1. Instale o Flask:
pip install flask

2. Execute:
python app.py

3. Acesse:
http://127.0.0.1:5000

## Exemplo

POST /risco

{
  "descricao": "Falha de segurança",
  "probabilidade": 4,
  "impacto": 5
}
