from flask import Flask, request, jsonify
import cv2
import numpy as np

app = Flask(__name__)

def detect_currencies(image):
    # Lógica de detecção usando YOLO
    # ...

    # Exemplo de resposta fictícia
    detected_currencies = [{'value': 10, 'count': 2}, {'value': 20, 'count': 1}]
    total_value = sum(currency['value'] * currency['count'] for currency in detected_currencies)

    return detected_currencies, total_value

@app.route('/process_image', methods=['POST'])
def process_image():
    # Recebe a imagem da requisição
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'})

    image = cv2.imdecode(np.frombuffer(request.files['image'].read(), np.uint8), cv2.IMREAD_UNCHANGED)

    # Faça a detecção de cédulas usando o modelo YOLO
    detected_currencies, total_value = detect_currencies(image)

    # Envia a resposta para o aplicativo
    response = {
        'detected_currencies': detected_currencies,
        'total_value': total_value
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)