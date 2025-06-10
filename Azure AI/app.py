
### 3. **docs/implementation.md**

import azure.cognitiveservices.speech as speechsdk

def transcribe_audio(file_path):
    speech_key = "<YOUR_SPEECH_API_KEY>"
    region = "<YOUR_REGION>"
    
    # Configuração do serviço de fala
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=region)
    audio_config = speechsdk.audio.AudioConfig(filename=file_path)
    
    # Criação do reconhecedor
    recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    
    # Transcrição
    result = recognizer.recognize_once()
    
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return result.text
    else:
        return "Erro na transcrição: " + result.error_details

# Exemplo de uso
audio_path = "data/input_audio/audio_example.wav"
transcribed_text = transcribe_audio(audio_path)
print("Texto transcrito:", transcribed_text)
