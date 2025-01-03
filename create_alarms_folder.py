import os
import sys


def create_alarms_folder():
    """Cria a pasta 'Alarmes' na mesma localização do executável ou script."""
    # Obter o caminho base do executável ou script
    if getattr(sys, 'frozen', False):  # Executável gerado pelo PyInstaller
        base_path = os.path.dirname(sys.executable)
    else:  # Script Python em execução
        base_path = os.path.dirname(os.path.abspath(__file__))

    # Caminho completo da pasta Alarmes
    alarms_folder = os.path.join(base_path, "Alarmes")

    # Verifica se a pasta existe, se não, cria
    if not os.path.exists(alarms_folder):
        os.makedirs(alarms_folder)
        print(f"Pasta 'Alarmes' criada em: {alarms_folder}")
    else:
        print(f"Pasta 'Alarmes' já existe em: {alarms_folder}")

    return alarms_folder
