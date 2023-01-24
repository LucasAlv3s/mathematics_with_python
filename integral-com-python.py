# -*- coding: utf-8 -*-
"""
Cálculo de área por integral definida.

Um túnel deve ser lacrado com uma tampa de concreto. A seção transversal 
do túnel e a tampa de concreto têm contornos de um arco de parábola e mesmas 
dimensões. Para determinar o custo da obra, um engenheiro deve calcular a área 
sob o arco parabólico em questão. Usando o eixo horizontal no nível do chão e 
o eixo de simetria da parábola como eixo vertical, obteve a seguinte equação 
para a parábola: y = 9 – x^2, sendo x e y medidos em metros. Qual a área sob o 
arco parabólico, sendo que, os preços costumam variar entre R$40,00 e R$150,00 o m^2 (ano base de 2021) e a opção mais econômica geralmente é o concreto armado?

9 - x^2 = 0

9 = x^2

x = √9

x = +3 ou -3
"""

import matplotlib.pyplot as plt
import numpy as np # arrays multidimensionais.
x1 = np.arange(-4,5,1)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Move left y-axis and bottim x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.plot(x1, 9-x1**2 )
plt.show()



from sympy import * # impostanto a biblioteca
x = Symbol('x') # definindo o símbolo
init_printing(pretty_print=True) # para representar visualmente a integral
Integral(9-x**2,(x, -3, 3))

area = Integral(9-x**2,(x, -3, 3)).doit()
print('A área é:', area, 'm^2')

print('Menor custo: ','R$', area*40)
print('Maior custo:','R$', area*150)