# JSON FILE

Modulo para a leitura e escrita de JSON em arquivos de forma simplificada.

#### Como Usar
```
# faz a importação do modulo
from jsonFile import JSN

# definição de uma váriavel com referência a classe
# não é necessário, pois todas as funções são estáticas
j = JSN

# definição do caminho do arquivo
# caso não seja passado nenhum arquivo, será gerado uma exceção do tipo FilePathNotDefined
j._set_file('config.json')

# faz a leitura do json no arquivo

conf = j.read()

# faz a escrita do json no arquivo
# recebe um dicionário como dados para escrever
j.write()
```
