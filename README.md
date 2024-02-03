# Roll-Dice
This is a simple project of an algorithm that rolls D&amp;D dice with modifiers at a command prompt.

## Funcionamento
O código foi construído no PyCharm e funciona com seu terminal, contudo, ele é melhor executado em um prompt de comando separado. Existem quatro comandos que o usuário pode usar, são: 'roll', 'set', 'clear' e 'quit'.

### Rolando Dados

#### Rotina de Coleta
O primeiro e principal comando 'roll' aceita uma série de parâmetros, por padrão limitados a apenas 2 digítios, para permitir rolagens de dados no seguinte formato: roll 1d20+5-2, onda a expressão máxima seria roll 99
Para validar o formato usado o algoritmo usa um padrão **Regex** para varrer a string que o usuário oferece como input. O primeiro parâmetro é a quantidade de dados a serem rolados, seguido do tipo de dado limitado por uma variável interna que só permite os tipos de dados: d100, d50, d20, d12, d10, d8, d6, d4, d3 e d2. O terceiro parâmetro são os modificadores, eles são coletados na ordem: modificador_positivo, modificador_negativo; caso o algoritmo não o encontre-os nessa ordem, ele irá coletar apenas o que respeita a ordem, por exemplo:
roll 1d20-4+2
Para o pârametro de modificadores, ele vai coletar apenas o '-4'

#### Rolando Dados
Para rolar dados o algoritmo usa de um simples **randint** da biblioteca random do python para gerar números pseudo-aleatórios e armazena-los numa lista, após isso os valores são somados com a função de alta ordem **reduce** da biblioteca functools. Os modificadores são armazenados em lista, se o usuário passou um valor para eles a lista será somada também com a função **reduce** e terá um valor final a ser somado nas rolagens.

### Definindo Classe de Dificuldade de Teste
#### Rotina de Coleta
Classe de dificuldade de teste (CD) é um conceito em muitos jogos de RPG de mesa, não exclusivo do D&D, onde um valor é definido e somente se considerado um _sucesso_ no teste caso o valor tirado nos dados seja maior que o CD do teste. O comando 'set' também usa um padrão Regex para coletar o input do usuário, sendo esse limitado a dois digitos. 
