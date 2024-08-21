# controllers/message_controller.py
from flask import request, jsonify
from flask.views import MethodView
from services.chatgpt_service import ChatGPTService
from services.tts_service import TTSService
import re

class MessageController(MethodView):

    def __init__(self):
        self.chat_service = ChatGPTService()
        self.tts_service = TTSService()

    def post(self):
        # Obtém a mensagem do corpo da requisição
        user_message = request.json.get('message')
        if not user_message:
            return jsonify({"error": "Mensagem não fornecida"}), 400

        # Chama o serviço ChatGPT para obter uma resposta
        response_text = self.chat_service.get_response(user_message)

        # Normaliza o texto da resposta
        normalized_text = self.normalize_text(response_text)

        # Gera um arquivo de áudio com a resposta normalizada usando o TTSService
        audio_file_path = "output-response.wav"
        self.tts_service.text_to_speech(normalized_text, file_path=audio_file_path)

        # Retorna a resposta e o caminho do arquivo de áudio
        return jsonify({"response": normalized_text, "audio_file": audio_file_path})

    @staticmethod
    def normalize_text(text):
        # Remove caracteres especiais, mantendo apenas letras, números e alguns sinais de pontuação
        text = re.sub(r'[^A-Za-z0-9À-ÿ .,?!]', '', text)
        # Substitui múltiplos espaços por um único
        text = re.sub(r'\s+', ' ', text)
        # Remove espaços extras no início e no fim
        text = text.strip()
        return text
