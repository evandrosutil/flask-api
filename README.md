Repositório com código de uma API REST escrita em Python usando Flask e que consome a [API do Genius](https://docs.genius.com/#/getting-started-h1)



Idealmente, a API roda em uma instância EC2. É possível fazer uma consulta pelo browser no endereço

```
http://3.12.104.77:5000/artist?artist=<nome_artista>
```

A consulta também pode ser feita via linha de comando

```
curl http://3.12.104.77:5000/artist?artist=<nome_artista>
```

O retorno é um dicionário que tem o nome do artista como chave e as 10 musicas mais populares como valores.

Também é possível passar a opção `cache=False`
```
curl http://3.12.104.77:5000/artist?artist=<nome_artista>&cache=False
```

nesses casos, a consulta não será cacheada e o valor será salvo em uma coleção no DynamoDB.



Também é possível rodar localmente, para tanto, primeiro é preciso clonar o repositório 

```
git@github.com:evandrosutil/flask-api.git
```
Depois, configurado o [`aws-cli`](https://aws.amazon.com/pt/cli/), deve ser feito deploy do DynamoDB com o cloudformation

```
aws cloudformation deploy --template-file=dynamo.yaml --stack-name=falskapp
```

Gerar [access token do Genius](https://docs.genius.com/#/authentication-h1)
Fazer o build com o docker-compose

```
docker-compose up --build
```
Com isso é possível fazer a requisição em `http://localhost:5000/artist
