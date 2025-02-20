# Filipe Chagas, 2025

from funcoes import funcoes
from dotenv import load_dotenv
from groq import Groq
import json
import os


def prompt_instrutivo():
    with open('prompt.txt', 'r') as f:
        parte1 = f.read()

    parte2 = '\n'.join([f'- Função número {i}: {funcao.__doc__}' for i, funcao in funcoes.items()])
    
    return f'{parte1}\n{parte2}'


def submeter(prompt_usuario):
    client = Groq(api_key=os.getenv('GROQ_API_KEY'))
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": prompt_instrutivo()
            },
            {
                "role": "user",
                "content": prompt_usuario
            }
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False,
        response_format={"type": "json_object"},
        stop=None
    )
    #print(completion.choices[0].message.content)
    return json.loads(completion.choices[0].message.content)


def pos_processamento(analise_llm):
    comandos = analise_llm['comandos']
    mensagem = analise_llm['mensagem']
    retornos = ['<ERRO>']*len(comandos)
    for i in range(len(comandos)):
        numero = comandos[i]['funcao']
        argumentos = comandos[i]['argumentos']
        try:
            funcao = funcoes[numero]
            retornos[i] = funcao(*argumentos)
        except Exception as ex:
            print(f'OCORREU UMA FALHA NESTA OPERAÇÃO. DESCRIÇÃO DO PROBLEMA: {ex}')
            break
    return mensagem.format(*retornos)
    

if __name__ == '__main__':
    load_dotenv()
    prompt_usuario = input('Peça algo para a Fulana: ')
    analise_llm = submeter(prompt_usuario)
    mensagem = pos_processamento(analise_llm)
    print(f'Fulana responde: {mensagem}')