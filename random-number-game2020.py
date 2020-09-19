# This is a random number guessing game
import random
print('Huhu, wie heisst Du denn?')
name = input()
print('Super, ' + name + ', I denke gerade an eine Zahl zwischen 1 und 20')
geheimZahl = random.randint(1, 20)
for anzahlRaten in range(1, 7):
    print("Bitte rate mal.")
    geraten = int(input())
    if geraten < geheimZahl:
        print('Meine Zahl ist groesser')
    elif geraten > geheimZahl:
        print('Meine Zahl ist kleiner')
    else:
        break # will break for correct guess
if geraten == geheimZahl:
    print('Super, ' + name + ', das war genau meine Zahl! Du hast sie mit ' + str(anzahlRaten) + ' Versuchen erraten!')
else:
    print('Nein, die Zahl an die ich dachte war ' + str(geheimZahl)) + print('Gut gemacht')

