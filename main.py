from TTS.api import TTS

# Crie uma instância da classe TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)

# Use a instância tts para chamar o método tts_to_file
tts.tts_to_file(
    text="A expressão para inglês ver é uma gíria brasileira que se refere a algo que é feito apenas para parecer... ou dar uma impressão, sem uma intenção real ou efetiva por trás.",
    file_path="output.wav",
    speaker_wav=["sam_model.wav"], 
    language="pt",
    split_sentences=True,
    speed=0.9  # Ajuste a velocidade da fala
)

print("Audio saved as output.wav")
