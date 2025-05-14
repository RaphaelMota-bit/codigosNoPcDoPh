# app.py
from flask import Flask, request
import speech_recognition as sr
import re
from pydub import AudioSegment
import requests

from pydub import AudioSegment
from pydub.utils import which

AudioSegment.converter = which("C:/Users/Pedro Henique/Desktop/codes_fael - Copy/ffmpeg-7.1.1-essentials_build/ffmpeg-7.1.1-essentials_build/bin/ffmpeg.exe")


app = Flask(__name__)

def processa_comando(texto):
    texto = re.sub(r'[^a-zA-Z0-9 ]', '', texto.lower())
    comandos = []

    for palavra in texto.split():
        if palavra == "som":
            comandos.append("ligar")
        elif palavra == "amor":
            comandos.append("desligar")

    return comandos

@app.route('/')
def index():
    return open("site_audio.html").read()

@app.route('/upload_audio', methods=['POST'])
def upload_audio():
    file = request.files['audio']
    file.save('audio.webm')

    # Converte para WAV
    sound = AudioSegment.from_file('audio.webm')
    sound.export('audio.wav', format='wav')

    # Reconhecimento de voz
    r = sr.Recognizer()
    with sr.AudioFile('audio.wav') as source:
        audio = r.record(source)
        try:
            texto = r.recognize_google(audio, language="pt-BR")
            comandos = processa_comando(texto)

            # Envia para Arduino se estiver rodando localmente
            for cmd in comandos:
                try:
                    requests.post("http://127.0.0.1:5001/comando", data={"cmd": cmd})
                except:
                    print(f"Erro ao enviar comando: {cmd}")

            return texto
        except sr.UnknownValueError:
            return "Não entendi o áudio."
        except sr.RequestError as e:
            return f"Erro no reconhecimento: {e}"

if __name__ == '__main__':
    app.run()
