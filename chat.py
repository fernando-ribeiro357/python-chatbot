import os
import urllib3
import pygame
import random
import string
from gtts import gTTS
from datetime import datetime
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate
from rich.console import Console
from rich.markdown import Markdown

urllib3.disable_warnings()

load_dotenv()

ollama_url=os.getenv('OLLAMA_URL')
ollama_model=os.getenv('OLLAMA_MODEL')
chat = ChatOllama(base_url=ollama_url,model=ollama_model)

def resposta_bot(mensagens):
    system = '''Você é um assistente útil que fica feliz em ajudar.
    Suas respostas devem sempre considerar apenas a sua base de conhecimento.
    Caso não saiba responder a alguma pergunta ou não tenha conhecimento da resposta, diga que não sabe.
    '''
    mensagens_modelo = [('system', system)]
    mensagens_modelo += mensagens
    template = ChatPromptTemplate.from_messages(mensagens_modelo)
    chain = template | chat
    retorno = chain.invoke({}).content
    return retorno

def prompt():
    ''' 
    Função para receber o prompt do usuário e fazer a 
    requisição ao chat com o prompt fornecido
    '''
    try:
        print('''
        ───████████───
        ──▐▀▀▀▀▀▀▀▀▌──
        ─▐▐  ▀  ▀  ▌▌─
        ──▐──▄▄▄▄──▌──
        ──▐  █▄▄█  ▌──
        
        Bem vindo ao ChatBot. 
        
🤖 Como posso te ajudar?
        ''')

        mensagens = []
        while True:
            pergunta = input(f'[x: sair]\n🙂 >>> ')
            if pergunta.lower() == 'x':
                sair()
                break

            mensagem = ('user', pergunta)
            mensagens.append(mensagem)
            history(mensagem);
            resposta = resposta_bot(mensagens)
            mensagem = ('assistant', resposta)
            mensagens.append(mensagem)
            history(mensagem);
            print(f'🤖 >>> \n')
            console = Console()
            markdown = Markdown(resposta)
            console.print(markdown)
            tts(resposta)
            print('\n')

        print('Obrigado por me consultar, estarei sempre aqui para te ajudar. 🤖\n')
    except KeyboardInterrupt:
        print("Sinal de interrupção recebido. Encerrando...")

def sair():
    print('\nSaindo do programa...\n')

def history(tupla):    
    try:
        now = datetime.now()
        data_hora = now.strftime('%Y-%m-%d %H:%M:%S')
        data = now.strftime('%Y-%m-%d')
        caminho_do_arquivo = f'./history_{data}.txt'
        # Abre o arquivo no modo 'w' (write), que sobrescreve o arquivo se já existir
        with open(caminho_do_arquivo, 'a') as arquivo:
            # Escreve a variável no arquivo
            arquivo.write(data_hora + ' : ' + str(tupla) + '\n')
    except Exception as e:
        print(f"Ocorreu um erro ao escrever o arquivo: {e}")


def tts(text: str, lang="pt", slow=False, file_name: str | None = None):
    '''Função para converter o texto em voz (tts) utilizando a bibioteca gTTS
        e o pygame.mixer para executar o áudio gerado pelo texto fornecido
    '''
    file_name = file_name or random_mp3_fname()
    file_path = f"/tmp/{file_name}"

    tts = gTTS(text=text, lang=lang, slow=slow)
    tts.save(file_path)

    # 初始化 pygame mixer
    pygame.mixer.init()
    # 加載 MP3 文件
    pygame.mixer.music.load(file_path)
    # 播放音頻
    pygame.mixer.music.play()
    # 等待音頻播放完畢
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    # 停止播放器
    pygame.mixer.music.stop()
    # 刪除臨時文件
    os.remove(file_path)

def random_mp3_fname(str_size=12, allowed_chars=string.ascii_letters) -> str:
    fname = ''.join(random.choice(allowed_chars) for x in range(str_size))
    return f"{fname}.mp3"


def main():
    '''
    Função principal que inicia o programa 
    '''
    os.system('clear')    
    prompt()


if __name__ == '__main__':
    main()