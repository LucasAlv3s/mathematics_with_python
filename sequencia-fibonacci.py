# -*- coding: utf-8 -*-
"""

Força bruta
"""

# Commented out IPython magic to ensure Python compatibility.
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fib(n - 1) + fib(n - 2) #soma dos números anteriores

def all_fib(n):
    fibs = []
    for i in range(n):
        fibs.append(fib(i)) #criando a lista dos números. Ex, n = 5: [1,2,3,4,5]
    
    return fibs

# %time print(all_fib(10))

"""Programação Dinâmica"""

# Commented out IPython magic to ensure Python compatibility.
def all_fib_dp(n):
    fibs = []
    for i in range(n):
        if i < 2:
            fibs.append(i)
        else:
            fibs.append(fibs[i - 2] + fibs[i - 1])
    
    return fibs

# %time print(all_fib(10))