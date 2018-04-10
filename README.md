# codigos python

Codigos das atividades de IC

## Atividade 1 - Definições Condicionais

1. Defina a função `pd(c)` cuja avaliação associa o consumo de dados em gigabytes com o valor pago em reais, calculado conforme as situações abaixo. O cálculo do custo de consumo fracionários são aproximados para o inteiro mais próximo (por exemplo, 6.3GB é cobrado como 7GB).
   * Para consumos até 2GB, o valor é 20
   * Para consumos maiores que 2GB, até 5GB, o valor é 20 + 5 por cada GB
   * Para consumos maiores que 5GB, até 10GB, o valor é 40 + 3 por cada GB
   * Para consumos acima de 10GB, o valor é 60 + 1,5 por cada GB
1. Considere um retângulo cujos extremos superior esquerdo e inferior direito são definidos pelas coordenadas cartesianas **(x1,y1)** e **(x2,y2)**. Defina a função `tq(x1,y1,x2,y2)` que verifica se o retângulo ocupa os quatro quadrantes do plano cartesiano.

## Atividade 2 - Lista de Exercícios

**Exercício 1**: Defina a função `intersec(x1,y1,x2,y2,x3,y3,x4,y4)` que sucede se, no plano cartesiano, há intersecção entre dois retângulos definidos pelos pontos superior esquerdo e inferior direito: **(x1,y1)** e **(x2,y2)** para o primeiro retângulo e **(x3,y3)** e **(x4,y4)** para o segundo.


**Exercício 2**: A tarifação de uma ligação telefônica internacional é feita do seguinte modo: O valor mínimo é de R$5, que dá direito a uma ligação de até 5 minutos. Quando a duração é de até 10 minutos, são cobrados R$7. Ligações com mais de 10 minutos pagam R$1 por cada minuto adicional (somados aos R$7 iniciais). Defina a função `tarifa(m)` que associa o valor do custo da ligação com duração de `m` minutos. Por exemplo:
```python
>>> tarifa(12)
9
```
**Exercício 3**: Um torcedor fanático deseja confeccionar uma bandeira do Brasil "estilizada" para usar durante os jogos olímpicos de 2016. Ele já tem a quantidade de panos verde e azul exatas e precisa saber quantos metros de pano amarelo vai precisar comprar. Calcule a quantidade de pano amarelo (em metros quadrados), considerando que a bandeira está no plano cartesiano, e que sabemos os valores dos pontos superior esquerdo **(x1, y1)** e inferior direito **(x2, y2)** do retângulo conforme ilustrado na figura abaixo:
```python
>>> pano_amarelo(x1,y1,x2,y2)
```
![Bandeira do Brasil][bandeiraBR.jpg]

[bandeiraBR.jpg]: atividade-2/bandeiraBR.jpg "Bandeira do Brasil"

A parte verde é um retângulo de lados **(y1-y2)** e **(x2-x1)**. A parte em amarelo refere-se a um quadrado "girado" em 90 graus com diagonal igual a **(y1-y2)**. O círculo azul refere-se a um círculo com diâmetro igual a **(y1-y2)**.
