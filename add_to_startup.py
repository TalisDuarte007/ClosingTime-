import os
import sys

from win32com.client import Dispatch


def add_to_startup():
    """Adiciona o aplicativo à inicialização do Windows."""
    # Diretório de inicialização do usuário
    startup_folder = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")

    # Nome do atalho
    shortcut_path = os.path.join(startup_folder, "Alarmes para Academia.lnk")

    # Caminho do executável
    executable = sys.executable  # Obtém o caminho do Python ou do executável do aplicativo

    # Verifica se o atalho já existe
    if not os.path.exists(shortcut_path):
        # Cria o atalho
        shell = Dispatch("WScript.Shell")
        shortcut = shell.CreateShortcut(shortcut_path)
        shortcut.TargetPath = executable
        shortcut.WorkingDirectory = os.path.dirname(executable)
        shortcut.IconLocation = executable
        shortcut.save()

        print("Aplicativo adicionado à inicialização do Windows.")
    else:
        print("O aplicativo já está configurado para iniciar com o Windows.")
