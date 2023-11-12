from flask import Flask, request, jsonify
import cv2
import numpy as np

app = Flask(__name__)

def detect_currencies(image_path):
    # Aqui você deve implementar a lógica de detecção de cédulas usando o modelo YOLO
    # Substitua este exemplo pela implementação real

    # Exemplo de detecção fictícia
    image = cv2.imread(image_path)
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

    image = request.files['image']

    # Salva a imagem temporariamente no servidor
    temp_image_path = '/tmp/temp_image.jpg'  # Você pode ajustar o local e nome do arquivo conforme necessário
    image.save(temp_image_path)

    # Faça a detecção de cédulas usando o modelo YOLO
    detected_currencies, total_value = detect_currencies(temp_image_path)

    # Envia a resposta para o aplicativo
    response = {
        'detected_currencies': detected_currencies,
        'total_value': total_value
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
