# Compilador
A interface usa Framework Flask

Para testar, use o terminal com seguinte comando:
```
python3 Interface.py 
```
# Documentação
   ### Lexico:
   - Tokens da palavra resevada:      
   int, float, String, boolean, True , False , return , if , for ,  in , or , and , == , != ,
   <= , >= , ! , + , - , * , ^ , / , % , " , = , // , { , } , ( , ) , [ , ] , print , input 
   - Expressão Regular:
   Deve ser obrigatoriamente iniciado com a-z ou A-Z podendo conter a-z ou A-Z ou 0-9
   

- A sintaxe é baseada em “espaços” ou “\s”, onde as palavras reservadas e identificadores devem ser separadas pelo espaços para reconhecer a sintaxe. Ex: int x = 0 (Aceita) | int x=0 (não aceita)


### Exemplos da linguagem
```python
//Declaração de variaveis
int x = 0
float y = 0
int array = []

//Atribuição
x = 1
x = x + 1
array = 1 2 3 4 5
array[0] = 0

//Condição
if x > 0 {
   //Seu codigo aqui
}

//Laço de Repetição
for i in array {
   //Seu codigo aqui
}

//Entrada
input Digite o valor de x &x

//Saida
print o valor de x= &x
```
## Exemplos

* Léxico
    * ![](https://media.giphy.com/media/XE7obhdNoO0HvFnNEl/giphy.gif)
 ## Implementações
  - [x] Léxico
  - [ ] Sintático
  - [ ] Semântico
  - [ ] Compilador
