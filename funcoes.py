# Filipe Chagas, 2025
import os


def criar_diretorio(caminho):
    """Função relacionada à intenção de criar um diretório. Requer um argumento: o caminho do diretório (string). Não tem retorno."""
    print(f'CRIANDO DIRETÓRIO {caminho}')
    if not os.path.exists(caminho):
        os.mkdir(caminho)
    else:
        print(f'ALERTA: {caminho} já existe')
        assert os.path.isdir(caminho), f'{caminho} não é um diretório.'


def deletar_diretório(caminho):
    """Função relacionada à intenção de deletar um diretório. Requer um argumento: o caminho do diretório (string). Não tem retorno."""
    print(f'DELETANDO DIRETÓRIO {caminho}')
    os.rmdir(caminho)


def criar_arquivo(caminho, conteudo):
    """Função relacionada à intenção de criar um arquivo de texto. Requer dois argumentos: o primeiro é o caminho do arquivo (string), e o segundo é o texto a ser escrito no arquivo (string). Não tem retorno."""
    print(f'CRIANDO E ESCREVENDO ARQUIVO {caminho}')
    with open(caminho, 'w') as f:
        f.write(conteudo)


def ler_aquivo(caminho):
    """Função relacionada à intenção de ler um arquivo de texto. Requer um argumento: o caminho do arquivo (string). Retorna o conteúdo do arquivo (string)."""
    print(f'LENDO O ARQUIVO {caminho}')
    with open(caminho, 'r') as f:
        texto = f.read()
    return texto


def deletar_arquivo(caminho):
    """Função relacionada à intenção de deletar um arquivo. Requer um argumento: o caminho do arquivo (string). Não tem retorno."""
    print(f'DELETANDO O ARQUIVO {caminho}')
    os.remove(caminho)


def verificar_existencia(caminho):
    """Função relacionada à intenção de verificar se um arquivo ou diretório existe. Requer um argumento: o caminho do arquivo (string). Retorna as strings 'existe' ou 'não existe'."""
    if os.path.exists(caminho):
        return 'existe'
    else:
        return 'não existe'


funcoes = {
    1: criar_diretorio,
    2: deletar_diretório,
    3: criar_arquivo,
    4: ler_aquivo,
    5: deletar_arquivo,
    6: verificar_existencia
}