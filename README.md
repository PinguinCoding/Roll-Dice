# Roll-Dice
This is a simple project of an algorithm that rolls D&amp;D dice with modifiers at a command prompt.

## Funcionamento
O código foi construído no PyCharm e funciona com seu terminal, contudo, ele é melhor executado em um prompt de comando separado. Existem quatro comandos que o usuário pode usar, são: 'roll', 'set', 'clear' e 'quit'.

### Rolando Dados

#### Rotina de Coleta
O primeiro e principal comando 'roll' aceita uma série de parâmetros para permitir rolagens de dados no seguinte formato: roll 1d20+5-2. Para validar o formato usado o algoritmo usa um padrão Regex para varrer a string que o usuário oferece como input. O primeiro parâmetro é a quantidade de dados a serem rolados, seguido do tipo de dado limitado por uma variável interna que só permite os tipos de dados: d100, d50, d20, d12, d10, d8, d6, d4, d3 e d2. O terceiro parâmetro são os modificadores, eles devem estar na ordem: modificador_positivo, modificador_negativo; caso contrário o algoritmo somente irá pegar parcialmente os modificadores. 
