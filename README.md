# AG-math-func-UFLA-IA
Este projeto é um trabalho realizado pelos alunos **Gustavo Rodrigues Sousa** e **Luiz Carlos Coelho Conde** para a disciplina de Inteligência Artificial ministrada pelo professor **Ahmed Ali Abdalla Esmin** pelo DCC da **UFLA** no **primeiro semestre de 2020**. 

## Requisitos
Para executar este programa, é necessário ter o Python instalado (versão 3 ou acima)

## Executar
Para executar o programa:
```bash
python main.py
```
ou
```bash
python3 main.py
```
Caso você tenha mais de uma versão do python instaladas.

## Instruções
Aparecerá na tela todas a população inicial e final com o melhor individuo da população final impresso indicado 

## Resultados
Deram bons resultados convergindo para o **-10**, que é de fato o max da função nos limites [-10, 10] porém as vezes quando a população inicial não inicia com nenhum negativo ou os negativos da população inicial sãõ mal adapitados converge para o 10. Porém com mais gerações pode existir uma mutação que converge o primeiro gene (do negativo/positivo), podendo então, dizer que realmente converge para o resultado correto!

**Tempo**  
Gerações  | Tempo
------------- | -------------
5 | 2.00ms
500 | 113.97ms
5000 | 1.02ms
50000 | 11047.01ms

Testes feitos em um processador Intel Core i5-2440M com 2x4GB de Ram em windows.

## Problemas encontrados
- No Windows o jogo pode aparecer como "Não respondendo" em algum momento, mas ele continua executando mesmo assim, pra isso é só esperar um pouco.
- Tentamos adicionar threads para evitar que a heurística fosse executada por tempo indeterminado, mas não adiantou muito.

### Desinstalar o PyGame
```bash
pip uninstall pygame
```
