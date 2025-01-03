import os
import sys  # Import necessário


def create_alarms_folder():
    """Cria a pasta 'Alarmes' na mesma localização do executável, se não existir."""
    # Obter o caminho da pasta onde o executável está rodando
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

    # Caminho completo da pasta Alarmes
    alarms_folder = os.path.join(base_path, "Alarmes")

    # Verifica se a pasta existe, se não, cria
    if not os.path.exists(alarms_folder):
        os.makedirs(alarms_folder)
        print(f"Pasta 'Alarmes' criada em: {alarms_folder}")
    else:
        print(f"Pasta 'Alarmes' já existe em: {alarms_folder}")

    return alarms_folder
