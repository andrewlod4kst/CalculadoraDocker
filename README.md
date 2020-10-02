# CalculadoraDocker
Prática com o Docker e FastAPI com uma calculadora com 5 containers: calculadora, soma, subtração, multiplicação e divisão<br>
Host: 127.0.0.1<br>
Porta da calculadora: 8000<br>
Porta da soma: 8100<br>
Porta da subtração: 8200<br>
Porta da multiplicação: 8300<br>
Porta da divisão: 8400<br><br>

É somente necessário acessar a porta da calculadora, pois ela recebe todos os parâmetros (função, num1 e num2) e delega para os outros componentes.<br>
Como fazer build com o Docker Compose:
  - Abra a linha de comando na pasta que contém todos os arquivos
  - Digite docker-compose build
  - Assim que todas as imagens tiverem sido construídas, digite docker-compose up
<br>
Como usar:<br>
Browser:
  - Entre em 127.0.0.1:8000/docs
  - Clique em "POST"
  - Clique em "Try it out"
  - Escolha uma das opções como função: soma, subtracao, multiplicacao, divisao
  - Escolha os dois números
  - Clique em Execute
  - O resultado estará localizado em "Response body"
<br>
Curl request:
  - Cole o seguinte comando na linha de comando: curl -X POST "http://127.0.0.1:8000/" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"funcao\":\"subtracao\", \"num1\":1, \"num2\":2}"
<br>
Informações sobre a estrutura do projeto:<br><br>

Dockerfile: O projeto possui 5 Dockerfiles, um para cada container.<br>
As dependências incluídas nos Dockerfiles são: Python 3.8, Uvicorn, FastAPI, Pydantic e Request.<br>
Os Dockerfiles também estabelecem qual porta será usada por qual container, e definem o comando do Uvicorn para inicializar cada aplicação.<br>

docker-compose.yml: Estabelece os links entre os containers para que eles consigam se comunicar, suas portas e o Dockerfile necessário para construir a imagem de cada container.
<br><br>
Arquivos Python:
<br><br>
Calculadora mestre:<br>
calculadora.py: Recebe os argumentos funcao (str), num1 (int) e num2 (int) e delega para um outro container dependendo da função pedida, por meio de um POST request.<br><br>

Funções da calculadora: Recebem os argumentos num1 (int) e num2 (int) e retornam um JSON com a chave "resultado" e o resultado como valor.<br>
soma.py: Soma os dois números.<br>
subtracao.py: Subtrai os dois números.<br>
multiplicacao.py: Acumula o num2 por num1 vezes por meio de requests ao container soma.<br>
divisao.py: Conta quantas vezes é necessário subtrair num2 de num1 para que num1 seja menor.
