## Linux
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
deactivate

## Windows
python -m venv MBA # Criar o ambiente virtual
.\MBA\Scripts\activate # Ativar o ambiente virtual
pip install -r .\requirements.txt # Instalando as bibliotecas necessárias
deactivate # Desativar o ambiente virtual