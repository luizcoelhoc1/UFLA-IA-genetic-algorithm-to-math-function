# AG-math-func-UFLA-IA
Este projeto é um trabalho realizado pelos alunos **Gustavo Rodrigues Sousa** e **Luiz Carlos Coelho Conde** para a disciplina **GAC112** ministrada pelo professor **JOAQUIM QUINTEIRO UCHOA** pelo DCC da **UFLA** no **primeiro semestre de 2021**. 

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
Aparecerá na tela uma tupla das duas sequencias alinhadas com o score final dela

## Resultados
Par 3: TTACACCTAGC e TAGCAATTTTTTCC
Score 1: Acerto: +3, Erro: -2, Espaço: -3

Para o par 3 e score 1 que pode ser conferido a cima, foi encontrado o seguinte resultado: ('T-AACCAAACCTAGC', 'TTA-C-A--TTTTCC', -8)
onde os dois primeiros valores são as sequências alinhadas onde - representa o gap e o -8 seria a pontuação final desse alinhamento baseada no Score 1.
