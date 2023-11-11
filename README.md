# Projeto App Vison$

Proposta: Um aplicativo para auxiliar deficientes visuais na identificação de cédulas de dinheiro, usando o sensor da câmera do smartphone e um sistema de reconhecimento, o app verbaliza o valor da nota e oferece maior autonomia ao usuário em atividades simples do dia a dia.

Palavras-Chave: Computação Móvel, Inclusão Digital, Inteligência Artificial, Interação Humano-Computador e Visão Computacional.

# Overview

Organização dos diretorios:
- /weights_trained
- /training_algorithm
- /detection_algorithm
- /doc
- [Paper no Overleaf](https://www.overleaf.com/read/qsrfmnhvzrdv#1fb1a9)
- [Tabela de pesos testados](https://docs.google.com/spreadsheets/d/1qQWjE0bRPcIuYDuA-tXGYIFENlgSXxBJwYTWF7itZHY/edit?usp=sharing)
- [Notas](https://docs.google.com/document/d/1o4Y88ro4Ai_DdEM-NswhRqFp_U7o71gf_jGCvHdvslA/edit?usp=drive_link)

> Recomenda-se que os scripts de treino, presentes no diretorio /training_algorithm, sejam imprtados para o ambiente no Colab.
## Dataset
Importe o projeto do Roboflow por meio do seguinte codigo:
~~~bash
!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="sua-key")
project = rf.workspace("vision-fbche").project("cedulas-de-real-brasileiro")
dataset = project.version(2).download("yolov7")
~~~

# Referencias:
- [Roboflow notebooks](https://github.com/roboflow/notebooks)
- [Github - YOLOv7](https://github.com/WongKinYiu/yolov7)
- [Github - YOLOv8](https://github.com/ultralytics/ultralytics)
- [Doc Roboflow - Generate Augmented Images](https://docs.roboflow.com/datasets/image-augmentation)
