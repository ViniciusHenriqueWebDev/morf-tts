import os
import requests
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

class ChatGPTService:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")  # Pega a chave da API do arquivo .env
        self.api_url = "https://api.openai.com/v1/chat/completions"  # Corrigido para o endpoint correto

    def get_response(self, user_message):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "gpt-4o-mini",  # Certifique-se de que o modelo esteja correto
            "messages": [{"role": "user", "content": user_message}],  # Estrutura adequada para o endpoint de chat
        }

        response = requests.post(self.api_url, headers=headers, json=data)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"].strip()
        else:
            return f"Erro: {response.status_code}, {response.text}"

# Exemplo de uso:
chat_service = ChatGPTService()
response = chat_service.get_response("Como está o tempo hoje?")
print(response)
