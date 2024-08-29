# Coding Dojo

**Guilda JEDI Incolume - Grupo Python Incolume**

- _[Seja membro da Guilda JEDI Incolume](https://discord.gg/eBNamXVtBW)_

---

## Problema

**Validação CNPJ**

<article id="components">
<h3>
<p>Decifrando o Algoritmo do CNPJ</p>
</h3>
<div>
<p>O CNPJ é composto por quatorze algarismos, divididos em três blocos:</p>
<ul>
<li>o primeiro, que representa o número da inscrição propriamente dito;</li>
<li>o segundo, localizado após a barra, que representa um código único para a matrix ou filial;</li>
<li>o terceiro, representados pelos dois últimos valores chamados de dígitos verificadores (DV).</li>
</ul>
<p>Os dígitos verificadores (DV) são criados a partir dos doze primeiros. O cálculo é feito em duas etapas utilizando o módulo de divisão 11.</p>
<p>Para exemplificar o processo e tornar mais fácil a explicação vamos calcular os dígitos verificadores de um CNPJ hipotético, por exemplo, 11.444.777/0001-XX.</p>
<p><strong><em>Calculando o Primeiro Dígito Verificador</em></strong></p>
<p>O primeiro dígito é calculado utilizando-se o seguinte algoritmo.</p>
<p><strong>1)</strong> Distribua os 12 primeiros dígitos em um quadro colocando os pesos 5,4,3,2,9,8,7,6,5,4,3,2 abaixo da esquerda para a direita, conforme representação abaixo:</p>
<div align="center" class="normal">
<center>
<table width="80%" border="1" cellpadding="2" cellspacing="1" style="margin-bottom: 20px">
<tbody>
<tr>
<td align="middle" width="8%">1</td>
<td align="middle" width="8%">1</td>
<td align="middle" width="8%">4</td>
<td align="middle" width="8%">4</td>
<td align="middle" width="8%">4</td>
<td align="middle" width="8%">7</td>
<td align="middle" width="8%">7</td>
<td align="middle" width="8%">7</td>
<td align="middle" width="8%">0</td>
<td align="middle" width="8%">0</td>
<td align="middle" width="7%">0</td>
<td align="middle" width="13%">1</td>
</tr>
<tr>
<td align="middle" width="8%">5</td>
<td align="middle" width="8%">4</td>
<td align="middle" width="8%">3</td>
<td align="middle" width="8%">2</td>
<td align="middle" width="8%">9</td>
<td align="middle" width="8%">8</td>
<td align="middle" width="8%">7</td>
<td align="middle" width="8%">6</td>
<td align="middle" width="8%">5</td>
<td align="middle" width="8%">4</td>
<td align="middle" width="7%">3</td>
<td align="middle" width="13%">2</td>
</tr>
</tbody>
</table>
</center>
</div>
<p><strong>2)</strong> Multiplique os valores de cada coluna:</p>
<div align="center" class="normal">
<center>
<table width="80%" border="1" cellpadding="2" cellspacing="1" style="margin-bottom: 20px">
<tbody>
<tr>
<td align="middle" width="8%">1</td>
<td align="middle" width="8%">1</td>
<td align="middle" width="8%">4</td>
<td align="middle" width="8%">4</td>
<td align="middle" width="8%">4</td>
<td align="middle" width="8%">7</td>
<td align="middle" width="8%">7</td>
<td align="middle" width="8%">7</td>
<td align="middle" width="8%">0</td>
<td align="middle" width="8%">0</td>
<td align="middle" width="7%">0</td>
<td align="middle" width="13%">1</td>
</tr>
<tr>
<td align="middle" width="8%">5</td>
<td align="middle" width="8%">4</td>
<td align="middle" width="8%">3</td>
<td align="middle" width="8%">2</td>
<td align="middle" width="8%">9</td>
<td align="middle" width="8%">8</td>
<td align="middle" width="8%">7</td>
<td align="middle" width="8%">6</td>
<td align="middle" width="8%">5</td>
<td align="middle" width="8%">4</td>
<td align="middle" width="7%">3</td>
<td align="middle" width="13%">2</td>
</tr>
<tr>
<td align="middle">5</td>
<td align="middle">4</td>
<td align="middle">12</td>
<td align="middle">8</td>
<td align="middle">36</td>
<td align="middle">56</td>
<td align="middle">49</td>
<td align="middle">42</td>
<td align="middle">0</td>
<td align="middle">0</td>
<td align="middle">0</td>
<td align="middle">2</td>
</tr>
</tbody>
</table>
</center>
</div>
<p><strong>3)</strong> Calcule o somatório dos resultados (5+4+...+0+2) = 214</p>
<p><strong>4)</strong> O resultado obtido (214) será divido por 11. Considere como quociente apenas o valor inteiro, o resto da divisão será responsável pelo cálculo do primeiro dígito verificador.</p>
<p>Vamos acompanhar: 214 dividido por 11 obtemos 19 como quociente e 5 como resto da divisão. Caso o resto da divisão seja menor que 2, o nosso primeiro dígito verificador se torna 0 (zero), caso contrário subtrai-se o valor obtido de 11, que é nosso caso. Sendo assim nosso dígito verificador é 11-5, ou seja, <strong>6</strong> (seis).</p>
<p>Já temos portanto parte do CNPJ, confira: 11.444.777/0001-<strong>6</strong>X.</p>
<p><strong><em>Calculando o Segundo Dígito Verificador</em></strong></p>
<p><strong>1)</strong> Para o cálculo do segundo dígito será usado o primeiro dígito verificador já calculado. Montaremos uma tabela semelhante a anterior só que desta vez usaremos na segunda linha os valores 6,5,4,3,2,9,8,7,6,5,4,3,2 já que estamos incorporando mais um algarismo para esse cálculo. Veja:</p>
<div align="center" class="normal">
<center>
<table width="80%" border="1" cellpadding="2" cellspacing="1" style="margin-bottom: 20px">
<tbody>
<tr>
<td align="middle" width="7%">1</td>
<td align="middle" width="7%">1</td>
<td align="middle" width="7%">4</td>
<td align="middle" width="7%">4</td>
<td align="middle" width="7%">4</td>
<td align="middle" width="7%">7</td>
<td align="middle" width="7%">7</td>
<td align="middle" width="7%">7</td>
<td align="middle" width="7%">0</td>
<td align="middle" width="7%">0</td>
<td align="middle" width="6%">0</td>
<td align="middle" width="7%">1</td>
<td align="middle" width="17%">6</td>
</tr>
<tr>
<td align="middle" width="7%">6</td>
<td align="middle" width="7%">5</td>
<td align="middle" width="7%">4</td>
<td align="middle" width="7%">3</td>
<td align="middle" width="7%">2</td>
<td align="middle" width="7%">9</td>
<td align="middle" width="7%">8</td>
<td align="middle" width="7%">7</td>
<td align="middle" width="7%">6</td>
<td align="middle" width="7%">5</td>
<td align="middle" width="6%">4</td>
<td align="middle" width="7%">3</td>
<td align="middle" width="17%">2</td>
</tr>
</tbody>
</table>
</center>
</div>
<p><strong>2)</strong> Na próxima etapa faremos como na situação do cálculo do primeiro dígito verificador, multiplicaremos os valores de cada coluna e efetuaremos o somatório dos resultados obtidos: (6+5+...+3+12) = 221.</p>
<div align="center" class="normal">
<center>
<table width="80%" border="1" cellpadding="2" cellspacing="1" style="margin-bottom: 20px">
<tbody>
<tr>
<td align="middle" width="7%">1</td>
<td align="middle" width="7%">1</td>
<td align="middle" width="7%">4</td>
<td align="middle" width="7%">4</td>
<td align="middle" width="7%">4</td>
<td align="middle" width="7%">7</td>
<td align="middle" width="7%">7</td>
<td align="middle" width="7%">7</td>
<td align="middle" width="7%">0</td>
<td align="middle" width="7%">0</td>
<td align="middle" width="6%">0</td>
<td align="middle" width="7%">1</td>
<td align="middle" width="17%">6</td>
</tr>
<tr>
<td align="middle" width="7%">6</td>
<td align="middle" width="7%">5</td>
<td align="middle" width="7%">4</td>
<td align="middle" width="7%">3</td>
<td align="middle" width="7%">2</td>
<td align="middle" width="7%">9</td>
<td align="middle" width="7%">8</td>
<td align="middle" width="7%">7</td>
<td align="middle" width="7%">6</td>
<td align="middle" width="7%">5</td>
<td align="middle" width="6%">4</td>
<td align="middle" width="7%">3</td>
<td align="middle" width="17%">2</td>
</tr>
<tr>
<td align="middle">6</td>
<td align="middle">5</td>
<td align="middle">16</td>
<td align="middle">12</td>
<td align="middle">8</td>
<td align="middle">63</td>
<td align="middle">56</td>
<td align="middle">49</td>
<td align="middle">0</td>
<td align="middle">0</td>
<td align="middle">0</td>
<td align="middle">3</td>
<td align="middle">12</td>
</tr>
</tbody>
</table>
</center>
</div>
<p><strong>3)</strong> Realizamos novamente o cálculo do módulo 11. Dividimos o total do somatório por 11 e consideramos o resto da divisão.</p>
<p>Vamos acompanhar: 230 dividido por 11 obtemos 20 como quociente e 10 como resto da divisão. </p>
<p><strong>4)</strong> Caso o valor do resto da divisão seja menor que 2, esse valor passa automaticamente a ser zero, caso contrário (como no nosso exemplo) é necessário subtrair o valor obtido de 11 para se obter o dígito verificador, como realizado no cálculo do primeiro dígito. Logo, 11-10 = <strong>1</strong> é o nosso segundo dígito verificador.</p>
<p>Chegamos ao final dos cálculos e descobrimos que os dígitos verificadores do nosso CNPJ hipotético são os números <strong>6</strong> e <strong>1</strong>, portanto o CNPJ ficaria assim: 11.444.777/0001-61.</p>
<p>O <a href="https://www.geradorcnpj.com">gerador de cnpj</a> apresentado neste site funciona com base neste algoritmo. A rotina de gerar CNPJ 's válidos, inicialmente sorteia 9 números. Calcula-se o 1o dígito verificador e integra-se o mesmo aos 9 números iniciais. Prossegue-se com o cálculo do segundo dígito verificador como ensinado. Ao final, o criador de CNPJ emite um número de CNPJ válido.</p>
<p>A geração de CPF's válidos funciona de maneira análoga. Caso seja do seu interesse, consulte mais informações sobre o <a href="https://www.geradorcpf.com/algoritmo_do_cpf.htm">algoritmo do cpf</a>.
</p></div></article>

## Exemplos

<details>
  <summary>Spoiler?</summary>
   Considerar em caso de fatoração:

    > modo pythônico
    > sem condicionais
    > estruturas performáticas
    > redução de complexidade ciclomática
    > análise assintótica de algoritmos (big O)

</details>

N/A - Exemplos de solução e resposta do problema. Geralmente utilizado para validar os testes do TDD.

## Artefatos

- [dojo](./__init__.py)
- [tests](./test_20240530.py)


## Referências
- https://www.geradorcnpj.com/algoritmo_do_cnpj.htm
N/A - Referências para o dojo, o problema ou para elicidações extras.

---

&copy; Incolume.com.br
