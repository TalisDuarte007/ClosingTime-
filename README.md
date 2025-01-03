# ClosingTime

![Badge de Versão](https://img.shields.io/badge/vers%C3%A3o-1.0.0-blue)
![Status do Projeto](https://img.shields.io/badge/status-vers%C3%A3o%20beta-blue)

**ClosingTime** é um aplicativo de alarmes com notificações personalizadas. Ele foi projetado para auxiliar academias, lojas e outros locais a anunciarem horários importantes, como fechamento, início de aulas ou qualquer evento agendado. É simples, personalizável e adaptável a outros cenários!
## Índice

- [Download](#Download)
- [Descrição do Projeto](#descrição-do-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Contribuição](#contribuição)
- [Licença](#licença)
- [Contato](#contato)

## Download
   Baixe a última versão do aplicativo aqui: 
   [![Download](http://img.shields.io/badge/Download-v1.0.0-blue)](https://github.com/TalisDuarte007/ClosingTime-/releases)

## Descrição do Projeto

   Este projeto visa simplificar as operações diárias em pequenas empresas, permitindo gerenciar alarmes incluindo sons para gerenciar horarios de fechamento ou pequenos anuncios internos.

## Tecnologias Utilizadas

- **Python**: Linguagem principal.
- **PyInstaller**: Para criar o executável.
- **ttkbootstrap**: Para criar uma interface gráfica moderna.
- **Pygame**: Para reprodução de áudio.
- **Pystray**: Para gerenciamento do ícone na bandeja do sistema

 ## Pré-requisitos
- Python 3.12 ou superior.
- Dependências listadas no requirements.txt:

   ```bash
    pip install -r requirements.txt

## Instalação

1. **Clone o repositório**:

   ```bash
    git clone https://github.com/TalisDuarte007/ClosingTime-.git
    cd ClosingTime-


2. **Crie o Executável: Certifique-se de que o PyInstaller está instalado:**:

    ```bash
    pip install pyinstaller
    pyinstaller --onefile --noconsole alarme.py

    O executável estará na pasta dist/.


3. **Configure a Pasta de Alarmes:**:

    O aplicativo cria automaticamente uma pasta chamada Alarmes na raiz do executável para que você organize os arquivos de áudio usados nos alarmes.


## Como Usar

Adicione Alarmes:

1. Abra o aplicativo.
-    Clique em "Adicionar Alarme".
-    Escolha um horário e selecione o arquivo de áudio desejado.

2. Verifique ou Delete Alarmes:

-    Clique em "Verificar Alarmes" para visualizar os alarmes configurados.
-    Selecione e delete alarmes conforme necessário.

3. Minimizar para Bandeja:

-    Feche ou minimize o aplicativo para mantê-lo funcionando na bandeja do sistema.
-    Clique com o botão direito no ícone da bandeja para restaurar ou fechar.

## Contribuição

Contribuições são bem-vindas! Siga os passos abaixo:

1. Fork o Repositório.

2. Crie um Branch:

    ```bash
    git checkout -b minha-nova-funcionalidade

3. Faça suas Alterações.

4. Faça o Commit:
    ```bash
    git commit -m "Adiciona nova funcionalidade"

5. Envie as Alterações:
    ```bash
    git push origin minha-nova-funcionalidade

6. Crie um Pull Request.


## Licença

Este projeto está licenciado sob a Licença MIT. Para mais detalhes, consulte o arquivo LICENSE.

## Contato

Nome: Talis Duarte
E-mail: tcd07@hotmail.com

Este é um README provisório para o projeto "ClosingTime". À medida que o desenvolvimento avança, mais detalhes e instruções serão adicionados.