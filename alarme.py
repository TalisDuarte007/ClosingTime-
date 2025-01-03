import ttkbootstrap as ttk
from tkinter import filedialog, messagebox, Listbox
import pygame
import threading
import time
import json
import os
from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw

from add_to_startup import add_to_startup

# Arquivo para salvar as configurações
CONFIG_FILE = "alarms_config.json"

# Inicializa o mixer do pygame
pygame.mixer.init()

# Variável global para o ícone da bandeja
tray_icon = None

# Função para salvar configurações
def save_config(alarms):
    with open(CONFIG_FILE, "w") as f:
        json.dump(alarms, f)

# Função para carregar configurações
def load_config():
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Função para tocar áudio usando pygame
def play_sound(audio_file):
    try:
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # Aguarda até o som terminar
            time.sleep(0.1)
    except pygame.error as e:
        messagebox.showerror("Erro ao reproduzir áudio", f"Erro: {e}")

# Função para monitorar alarmes
def check_alarms():
    while True:
        current_time = time.strftime("%H:%M")
        if current_time in alarms:
            play_sound(alarms[current_time])
            time.sleep(60)  # Evita tocar o áudio repetidamente no mesmo minuto
        time.sleep(1)

# Função para alternar entre telas
def show_frame(frame):
    frame.tkraise()

# Minimizar o app para a bandeja
def minimize_to_tray():
    global tray_icon
    root.withdraw()  # Esconde a janela principal

    # Criar ícone na bandeja se não existir
    if not tray_icon:
        tray_icon = create_tray_icon()

    tray_icon.visible = True  # Mostra o ícone na bandeja

# Criar ícone na bandeja
def create_tray_icon():
    # Desenhar ícone simples
    image = Image.new("RGB", (64, 64), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    draw.rectangle((16, 16, 48, 48), fill=(0, 128, 255))

    # Função para restaurar a janela
    def restore_window(icon, item=None):
        global tray_icon
        tray_icon.visible = False  # Oculta o ícone da bandeja
        root.deiconify()  # Mostra a janela principal

    # Função para fechar o aplicativo
    def quit_app(icon, item=None):
        icon.visible = False
        icon.stop()
        root.destroy()

    # Criar menu da bandeja
    menu = Menu(
        MenuItem("Restaurar", restore_window),
        MenuItem("Fechar", quit_app),
    )

    # Criar o ícone da bandeja
    icon = Icon("Alarmes para Academia", image, "Alarmes", menu)

    # Rodar o ícone em uma thread separada
    threading.Thread(target=icon.run, daemon=True).start()

    return icon

# Função para adicionar alarmes
def add_alarm():
    time_input = time_entry.get()
    if not time_input:
        messagebox.showerror("Erro", "Por favor, insira um horário.")
        return
    try:
        # Valida o formato do horário
        time.strptime(time_input, "%H:%M")
    except ValueError:
        messagebox.showerror("Erro", "O horário deve estar no formato HH:MM.")
        return

    audio_path = filedialog.askopenfilename(
        title="Selecione o arquivo de áudio",
        filetypes=[("Arquivos de áudio", "*.mp3 *.wav")]
    )
    if not audio_path:
        return

    alarms[time_input] = audio_path
    save_config(alarms)
    messagebox.showinfo("Sucesso", f"Alarme configurado para {time_input}!")
    show_frame(main_frame)  # Retorna à tela principal

# Função para deletar alarme selecionado
def delete_alarm():
    selected = alarm_list.curselection()
    if not selected:
        messagebox.showerror("Erro", "Selecione um alarme para deletar.")
        return
    selected_item = alarm_list.get(selected[0])
    selected_time = selected_item.split(" - ")[0]

    # Remove o alarme do dicionário e atualiza a lista
    del alarms[selected_time]
    save_config(alarms)
    update_alarm_list()
    messagebox.showinfo("Sucesso", f"Alarme para {selected_time} deletado!")

# Atualiza a lista de alarmes
def update_alarm_list():
    alarm_list.delete(0, "end")  # Substituí tk.END por "end"
    for time, audio in alarms.items():
        audio_name = os.path.basename(audio)  # Mostra apenas o nome do arquivo
        alarm_list.insert("end", f"{time} - {audio_name}")


# Carrega configurações salvas
alarms = load_config()

# Interface gráfica principal
root = ttk.Window(themename="darkly")
root.title("Alarmes para Academia")
root.geometry("400x400")

# Configuração para centralizar todos os elementos na janela
root.grid_rowconfigure(0, weight=1)  # Dá peso às linhas
root.grid_columnconfigure(0, weight=1)  # Dá peso às colunas

# Remover botão de fechar e maximizar
root.protocol("WM_DELETE_WINDOW", minimize_to_tray)
root.resizable(False, False)

# Criação de frames
main_frame = ttk.Frame(root)
add_alarm_frame = ttk.Frame(root)
view_alarms_frame = ttk.Frame(root)


for frame in (main_frame, add_alarm_frame, view_alarms_frame):
    frame.grid(row=0, column=0, sticky="nsew")  # Centraliza os frames

# Tela principal
main_label = ttk.Label(main_frame, text="Alarmes para Academia", font=("Arial", 16), anchor="center")
main_label.grid(row=1, column=0, pady=(20, 10), columnspan=2)  # Alterei a linha para 1

add_button = ttk.Button(main_frame, text="Adicionar Alarme", bootstyle="success", command=lambda: show_frame(add_alarm_frame))
add_button.grid(row=2, column=0, pady=(10, 5), columnspan=2)

view_button = ttk.Button(main_frame, text="Verificar Alarmes", bootstyle="primary", command=lambda: [update_alarm_list(), show_frame(view_alarms_frame)])
view_button.grid(row=3, column=0, pady=(5, 20), columnspan=2)

# Adicione linhas vazias para centralizar verticalmente
main_frame.grid_rowconfigure(0, weight=1)  # Linha superior vazia
main_frame.grid_rowconfigure(4, weight=1)  # Linha inferior vazia
main_frame.grid_columnconfigure(0, weight=1)

# Tela para adicionar alarmes
add_label = ttk.Label(add_alarm_frame, text="Adicionar Alarme", font=("Arial", 16))
add_label.grid(row=1, column=0, pady=(20, 10), columnspan=2)  # Alterei a linha para 1

time_label = ttk.Label(add_alarm_frame, text="Horário (HH:MM):")
time_label.grid(row=2, column=0, pady=(10, 5))

time_entry = ttk.Entry(add_alarm_frame, width=10)
time_entry.grid(row=2, column=1, pady=(10, 5))

save_button = ttk.Button(add_alarm_frame, text="Salvar Alarme", bootstyle="success", command=add_alarm)
save_button.grid(row=3, column=0, pady=(5, 10), columnspan=2)

back_button_add = ttk.Button(add_alarm_frame, text="Voltar", bootstyle="secondary", command=lambda: show_frame(main_frame))
back_button_add.grid(row=4, column=0, pady=(10, 20), columnspan=2)

# Adicione linhas vazias para centralizar verticalmente
add_alarm_frame.grid_rowconfigure(0, weight=1)  # Linha superior vazia
add_alarm_frame.grid_rowconfigure(5, weight=1)  # Linha inferior vazia
add_alarm_frame.grid_columnconfigure((0, 1), weight=1)

# Tela para verificar alarmes
view_label = ttk.Label(view_alarms_frame, text="Alarmes Configurados", font=("Arial", 16))
view_label.grid(row=1, column=0, pady=(20, 10), columnspan=2)  # Alterei a linha para 1

alarm_list = Listbox(view_alarms_frame, width=40, height=10, bg="black", fg="white", selectbackground="green", selectforeground="black")
alarm_list.grid(row=2, column=0, pady=(10, 10), columnspan=2)

delete_button = ttk.Button(view_alarms_frame, text="Deletar Alarme", bootstyle="danger", command=delete_alarm)
delete_button.grid(row=3, column=0, pady=(5, 10), columnspan=2)

back_button_view = ttk.Button(view_alarms_frame, text="Voltar", bootstyle="secondary", command=lambda: show_frame(main_frame))
back_button_view.grid(row=4, column=0, pady=(10, 20), columnspan=2)

# Adicione linhas vazias para centralizar verticalmente
view_alarms_frame.grid_rowconfigure(0, weight=1)  # Linha superior vazia
view_alarms_frame.grid_rowconfigure(5, weight=1)  # Linha inferior vazia
view_alarms_frame.grid_columnconfigure((0, 1), weight=1)

# Inicia com a tela principal
show_frame(main_frame)

# Inicia o monitor de alarmes em segundo plano
threading.Thread(target=check_alarms, daemon=True).start()

# Executa a interface
add_to_startup()
root.mainloop()
