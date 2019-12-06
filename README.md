# VaiDarLike
* Repositório dedicado a introduzir conhecimentos de _Deep Learning_  aplicados à *DataSets* disponibilizados pela plataforma [Youtube](https://www.youtube.com)


<p align="center">
    <img width="300" alt="logo" src="https://user-images.githubusercontent.com/40740008/69905393-99382280-1391-11ea-9b94-4be24f0517e8.png">
</p>

<p align="center">
    <sub>"Vai Dar Like?"</sub>
</p>


# Mas o que é o *YouTube*?
<p align="justify"> &emsp;&emsp;<i>Youtube</i> é uma plataforma de compartilhamento de vídeos onde qualquer usuário pode assistir, compartilhar, dar <i>like</i>, comentar e dar upload dos seus próprios vídeos. Os serviços do <i>Youtube</i> podem ser acessados de qualquer plataforma que possua suporte para o <i>Youtube</i>.</p>
<p align="justify"> &emsp;&emsp;Criado desde 2005 por três ex-funcionários do <i>PayPal</i> - Chad Hurley, Steve Chen e Jawed Karim, a plataforma ajuda milhões de pessoas a se interagirem em volta de conteúdos que elas têm em comum.</p>
<p align="justify"> &emsp;&emsp;Os milhares de vídeos que são enviados para o <i>Youtube</i> diariamente possuem inúmeras maneiras de interação entre o produtor de conteúdo e o seu público, como <i>likes</i>, comentários e o compartilhamento de vídeo.</p>

# Sobre o **_Vai Dar Like_**
<p align="justify"> &emsp;&emsp;Com o aumento exponencial de <i>upload</i> de vídeos, é necessário que haja títulos e thumbnails que sejam chamativos o suficiente para que o público se interesse pelo seu conteúdo. Pensando nisso, desenvolvemos um algoritmo que auxilia criadores de conteúdo do <i>YouTube</i> a criarem títulos para obter um maior engajamento em seus vídeos. Utilizamos para tal, um dataset com dados sobre vídeos que fizeram sucesso no YouTube. Processamos esses dados utilizando uma <i><b>Rede Neural Long Short Term Memory</b></i> que será explicada logo a seguir.

<p align="center">
    <img width="300" alt="logo" src="https://user-images.githubusercontent.com/40740008/69905506-3051aa00-1393-11ea-92f9-8d629fc16e77.gif">
</p>

<br>


# Gerando títulos por *LSTM*

<p align="justify"> &emsp;&emsp; A Modelagem de Linguagem é o principal problema para várias tarefas de processamento de linguagem natural, como falas para texto, sistema de conversação e resumo de texto. Um modelo de linguagem treinado aprende a probabilidade de ocorrência de uma palavra com base na sequência anterior de palavras usadas no texto. Os modelos de idiomas podem ser operados em nível de caractere, nível de sentença ou mesmo a nível de parágrafo. Neste projeto utilizamos um modelo de linguagem para gerar texto em linguagem natural implementando e treinando a <b><b>Rede Neural Recorrente <b>(RNN)</b></b></b> de última geração.
<a href="https://medium.com/phrasee/neural-text-generation-generating-text-using-conditional-language-models-a37b69c7cd4b">Fonte</a></p>
<br>
<p align="justify"> &emsp;&emsp;A modelagem de linguagem requer dados de entrada de sequência, pois, dada uma sequência (de palavras/tokens), o objetivo é prever a próxima palavra.</p>
<img src="https://user-images.githubusercontent.com/42192251/69904838-97b72c00-138a-11ea-810d-bbaeec27951e.png" alt="Italian Trulli">
<br>
<p align="justify"> &emsp;&emsp; Diferentemente das redes neurais <i>feed-forward</i> nas quais as saídas de ativação são propagadas apenas em uma direção, as saídas de ativação dos neurônios se propagam em ambas as direções (das entradas às saídas e das saídas às entradas) nas redes neurais recorrentes. Isso cria <i>loops</i> na arquitetura da rede neural, que atua como um "estado de memória" dos neurônios. Este estado permite que os neurônios se lembrem do que foi aprendido durante a execução.</p>

<p align="justify"> &emsp;&emsp;O estado da memória nas <b>RNNs</b> oferece uma vantagem sobre as redes neurais tradicionais, mas um problema chamado <i>Vanishing Gradient</i> está associado a elas. Nesse problema, ao aprender com um grande número de camadas, fica muito difícil para a rede aprender e ajustar os parâmetros das camadas anteriores. Para resolver esse problema, um novo tipo de <b>RNNs</b>, chamado Modelos LSTMs (<i>Long Short Term Memory</i>), foi desenvolvido.</p>

<p align="justify"> &emsp;&emsp;Os LSTMs têm um estado adicional chamado "estado da célula" através do qual a rede faz ajustes no fluxo de informações. A vantagem desse estado é que o modelo pode lembrar ou esquecer as inclinações mais seletivamente.</p>

### Adicionamos três camadas no modelo:
#### Camada de Entrada: 
Obtém a sequência de palavras como entrada "Camada LSTM": Calcula a saída usando unidades LSTM. Adicionamos 100 unidades na camada, mas esse número pode ser ajustado posteriormente. 
#### Camada de <i>Droupout</i>:
Uma camada de regularização que desliga aleatoriamente as ativações de alguns neurônios na camada LSTM. Ajuda na prevenção do excesso de encaixe. 
#### <b>Camada opcional</b> - Camada de Saída: 
Calcula a probabilidade da melhor palavra possível como saída. Deve-se executar este modelo para um total de 50 épocas, porém, pode-se aumentar o número de épocas.


### Como executar

Pré-requisitos: Virtualenv.

* **Primeiro passo**: Vá até a pasta raíz do projeto e crie um ambiente virtual.  


```bash
$ virtualenv -p python3 venv
```

* **Segundo passo**: Após criação do ambiente, basta acessá-lo.  

```bash
$ source venv/bin/activate
```

* **Terceiro passo**: Instale as dependências do projeto.
```bash
$ pip3 install -r requirements.txt
```

* **Quarto passo**: Execute o jupyter-notebook
```bash
$ jupyter-notebook
```

* **Quinto passo**: Navegue até a opção _cell_ e escolha a opção _"Run All"_. 
**O computador pode demorar um pouco para executar todos os algoritmos**

Caso queira parar o ambiente virtual, apenas digite ```deactivate``` e espere.

<p align="center">

| Aluno | Matrícula | *GitHub* |
| --- | --- | --- |
| Bruno Alves Félix | 16/0114705 | [Bruno-Felix](https://github.com/Bruno-Felix) |
| Caio Vinícius Fernandes de Araújo | 17/0138798 | [caiovfernandes](https://github.com/caiovfernandes) |
| Felipe Dias Soares Lima | 16/0006163 | [filypsdias](https://github.com/filypsdias) |
| Guilherme Mendes Pereira | 17/0129411 | [guilherme-mendes](https://github.com/guilherme-mendes) |
| Lucas Dutra Ferreira do Nascimento | 17/0050939 | [lucasdutraf](https://github.com/lucasdutraf) |
| Lucas Fellipe Carvalho Moreira | 16/0133394 | [lucasfcm9](https://github.com/lucasfcm9) |

</p>
