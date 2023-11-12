import requests

def simulate_client(image_path):
    url = "http://127.0.0.1:5000/process_image"  # Substitua pelo URL do seu servidor

    files = {'image': ('image.jpg', open(image_path, 'rb'), 'image/jpeg')}
    response = requests.post(url, files=files)

    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Failed to process image'}

# Substitua 'path_da_sua_imagem.jpg' pelo caminho da imagem que você deseja enviar
result = simulate_client('test01.jpeg')

if 'error' in result:
    print(f"Erro: {result['error']}")
else:
    print("Cédulas detectadas:")
    for currency in result['detected_currencies']:
        print(f"Valor: {currency['value']}, Quantidade: {currency['count']}")
    print(f"Valor total: {result['total_value']}")


