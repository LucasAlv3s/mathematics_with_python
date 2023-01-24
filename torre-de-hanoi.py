# -*- coding: utf-8 -*-

def mover_disco(inicio,fim):
    print("Mova o disco de",inicio,"para",fim)

def mover_torre(disco,partida, chegada, intermediario):
  if disco == 1:
    # Move o disco e finaliza a função
    mover_disco(partida,chegada)
  else:
      mover_torre(disco-1,partida,intermediario,chegada)
      mover_disco(partida,chegada)
      mover_torre(disco-1,intermediario,chegada,partida)


mover_torre(1,"A","B","C")