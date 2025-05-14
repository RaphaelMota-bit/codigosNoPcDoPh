# comando_arduino.py
from flask import Flask, request
import serial
import time

arduino = serial.Serial('COM3', 9600)  # Ajuste a porta correta
time.sleep(2)

app = Flask(__name__)

@app.route('/comando', methods=['POST'])
def comando():
    cmd = request.form['cmd']
    if cmd == 'ligar':
        arduino.write(b'ligar\n')
        return 'LED ligado'
    elif cmd == 'desligar':
        arduino.write(b'desligar\n')
        return 'LED desligado'
    else:
        return 'Comando inválido'

if __name__ == '__main__':
    app.run(port=5001)
