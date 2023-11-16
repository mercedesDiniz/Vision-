# Projeto App Vison$

Proposta: Um aplicativo para auxiliar deficientes visuais na identificação de cédulas de dinheiro, usando o sensor da câmera do smartphone e um sistema de reconhecimento, o app verbaliza o valor da nota e oferece maior autonomia ao usuário em atividades simples do dia a dia.

Palavras-Chave: Computação Móvel, Inclusão Digital, Inteligência Artificial, Interação Humano-Computador e Visão Computacional.

# Overview

Organização dos diretorios:
- /weights_trained
- /detection_algorithm
- /doc

- [Paper no Overleaf](https://www.overleaf.com/read/qsrfmnhvzrdv#1fb1a9)
- [Tabela de pesos testados](https://docs.google.com/spreadsheets/d/1qQWjE0bRPcIuYDuA-tXGYIFENlgSXxBJwYTWF7itZHY/edit?usp=sharing)
- [Notas](https://docs.google.com/document/d/1o4Y88ro4Ai_DdEM-NswhRqFp_U7o71gf_jGCvHdvslA/edit?usp=drive_link)

> Recomenda-se que os scripts de treino, presentes no diretorio /training_algorithm, sejam imprtados para o ambiente no Colab.

# Primeiros passos:

##  Environment
Crie o ambiente virtual dentro do diretorio /detection_algorithm (caso o mesmo ainda não tenha sido criado anteriormente), com o comando:
```copy
python3 -m venv yolo7_environment
```
Ative o ambiente virtual:
```
source yolo7_environment/bin/activate 
```
### Outros comandos:
- Desativar o ambiente virtual:
    ```
    deactivate
    ```
- Exportarmos um arquivo com todas bibliotecas que o nosso projeto contém:
    ```
    pip freeze > requirements.txt
    ```
- Instalando de forma automática todas as bibliotecas presentes no arquivo requirements.txt
    ```
    pip install -r requirements.txt  
    ```
- [Ambientes virtuais em Python](https://www.alura.com.br/artigos/ambientes-virtuais-em-python)
- [Doc: venv — Creation of virtual environments](https://docs.python.org/3/library/venv.html)

## Download do repositorio do YOLOv7 e instalação dos requirements
Primeiro clone o repositorio:
~~~bash
git clone https://github.com/SkalskiP/yolov7.git
~~~
Após o dowload entre no diretorio /yolov7, verifique e instale o requirements:
~~~bash
cd yolov7
git checkout fix/problems_associated_with_the_latest_versions_of_pytorch_and_numpy
pip install -r requirements.txt
~~~

## Importe o Dataset
Instale a biblioteca do Roboflow:
 ~~~bash
pip install roboflow
~~~

Importe o projeto do Roboflow, para iso verifique se o seguinte trecho de codigo está presente no notebook:
~~~bash
from roboflow import Roboflow
rf = Roboflow(api_key="sua-key")
project = rf.workspace("vision-fbche").project("cedulas-de-real-brasileiro")
dataset = project.version(3).download("yolov7")
~~~

# Referencias:
- [Roboflow notebooks](https://github.com/roboflow/notebooks)
- [Github - YOLOv7](https://github.com/WongKinYiu/yolov7)
- [Github - YOLOv8](https://github.com/ultralytics/ultralytics)
- [Doc Roboflow - Generate Augmented Images](https://docs.roboflow.com/datasets/image-augmentation)
