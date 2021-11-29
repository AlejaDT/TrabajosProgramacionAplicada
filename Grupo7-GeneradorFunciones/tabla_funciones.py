import math as m
COLS = 1024

coseno = [m.cos((2*m.pi*i)/COLS) for i in range (COLS)]
rampa = [i for i in range (1024)]
escalon = [m.cos(0) if i>512 else m.cos(m.pi) for i in range (COLS)]
escalonL = [i if i!=512 else 512 for i in range (COLS)]