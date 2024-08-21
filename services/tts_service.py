import lightning as L
from TTS.api import TTS
import re
import os
from dotenv import load_dotenv

load_dotenv()

class TTSService(L.LightningModule):
    def __init__(self, model_name="tts_models/multilingual/multi-dataset/xtts_v2", use_gpu=False):
        self.tts = TTS(model_name, gpu=use_gpu)

    def text_to_speech(self, text, file_path, speaker_wav=None, language="pt", split_sentences=True, speed=1.5):
        if speaker_wav is None:
            speaker_wav = ["sam_model.wav"]
        
        # Ajusta o texto para melhorar a prosódia antes de gerar o áudio
        text = self.adjust_text_for_prosody(text)
        
        # Use a instância tts para chamar o método tts_to_file
        self.tts.tts_to_file(
            text=text,
            file_path=file_path,
            speaker_wav=speaker_wav, 
            language=language,
            split_sentences=split_sentences,
            speed=speed,  # Ajuste a velocidade da fala
        )
        print(f"Audio saved as {file_path}")

    # Método adicional para ajustar mais nuances
    def adjust_text_for_prosody(self, text):
        # Remove emojis e caracteres especiais desnecessários
        text = re.sub(r'[^\w\s,;.!?]', '', text)

        # Substitui múltiplos espaços por um único espaço
        text = re.sub(r'\s+', ' ', text)

        # Substitui pontos finais por vírgulas para evitar pronúncia literal do ponto
        text = text.replace(". ", ", ").replace(".", ",")  # Mantém a entonação natural

        # Adiciona pausa após reticências e vírgulas
        text = text.replace("...", "...,").replace(",", ", ")

        # Corrige espaços antes de pontuações
        text = re.sub(r'\s+([,.!?])', r'\1', text)

        return text.strip()
