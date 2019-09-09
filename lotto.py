from random import *

lotto = []              

for i in range(49):
    lotto.append(i+1) # erstellt eine Liste von 49 Zahlen durch erhöhen von i

for i in range(100000):
    number1 = randint(0,48) # Zwei random zahlen 
    number2 = randint(0,48) # für den Variablen / Uahlen Tausch in der Liste
    lotto[number1], lotto[number2] = lotto[number2], lotto[number1] #Variablen Tausch - Number 1 mit Number 2

print(lotto)
if True:
    rr = randint(1,8)
    if rr == 1:
        print(lotto[0:6]) # Druckt die ersten 6 Zahlen der Liste
    if rr == 2:
        print(lotto[6:12])
    if rr == 3:
        print(lotto[12:18])
    if rr == 4:
        print(lotto[18:24])
    if rr == 5:
        print(lotto[24:30])
    if rr == 6:
        print(lotto[30:36])
    if rr == 7:
        print(lotto[36:42])
    if rr == 8:
        print(lotto[42:48])