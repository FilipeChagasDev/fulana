# Fulana

Fulana é uma assistente virtual, como Alexa e Siri, desenvolvida em Python para fins educacionais.

## Instruções de uso

Primeiro, instale as dependências executando o seguinte comando no terminal:

```sh
pip install -r requirements.txt
```

Em seguida, crie uma chave para a API do serviço [console.groq.com](https://console.groq.com/). Depois disso, crie um arquivo ``.env`` no mesmo diretório em que os scripts ``fulana.py`` e ``funcoes.py`` estão, e insira a chave neste arquivo da seguinte forma:

```
GROQ_API_KEY=SUA_CHAVE_AQUI
```

Obviamente, você deve substituir SUA_CHAVE_AQUI pela chave obtida no site do Groq.

Por fim, execute o script ``fulana.py`` utilizando o comando ``python fulana.py``.


## Exemplos de solicitações

As operações que atualmente são suportadas são:

* Criar diretório
* Deletar diretório
* Verificar se um diretório ou arquivo existe
* Criar e escrever um arquivo de texto
* Ler um arquivo de texto
* Deletar um arquivo

Você pode testar os seguintes pedidos para a Fulana:

```
Crie uma pasta chamada "festa" e, dentro dessa pasta, crie um arquivo chamado "convidados.txt" contendo os nomes dos seguintes convidados: Beatriz Paulino da Silva, Fernando Augusto Henrique, Antonio Mendes Muniz e Carla Nogueira dos Santos. Cada nome deve ficar em uma linha do arquivo. 
```

```
Mostre o conteúdo do arquivo "convidados.txt", dentro da pasta "festa".
```

```
Delete o arquivo "convidados.txt", que está dentro da pasta "festa", e depois delete a pasta "festa" também.
```