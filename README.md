# spider-ibge

Repositório para raspagem de dados do [Instituto Brasileiro de Geografia e Estatística](https://www.ibge.gov.br/).



## requisitos

Os seguintes requisitos são necessários:

- [Python](https://www.python.org/downloads/) versão 3.7.7 ou superior
- [Scrapy](https://scrapy.org/download/) versão 2.4.1 ou superior



## repositório

O projeto foi criado utilizando o comando:

```bash
scrapy startproject ibge web
```

> 
> Antes de executar o próximo comando, certifique-se de estar dentro do diretório `web`.
> 

Já a criação do robô para raspagem dos dados foi por meio do seguinte comando:

```bash
scrapy genspider Municipios ibge.gov.br
```


# comandos

> 
> Antes de executar o próximo comando, certifique-se de estar dentro do diretório `web`.
> 

Para execução do robô utilizando o seguinte comando:

```bash
scrapy runspider ibge/spiders/Municipios.py
```
