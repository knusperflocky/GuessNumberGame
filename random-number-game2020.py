# This is a random number guessing game
import random
print("Huhu, wie heisst Du denn?")
name = input()
print('Super, ' + name + ', I denke gerade an eine Zahl zwischen 1 und 20.')
print('Wieviel mal moechtest Du raten?')
try:
    maxNumberTries = int(input())
except:
    print("Bitte eine ganze Zahl eingeben")
geheimZahl = random.randint(1, 20) # needs try/catch error
richtigeZahl = False
for anzahlRaten in range(1, maxNumberTries):
    print("Bitte rate mal.")
    geraten = int(input())
    if geraten < geheimZahl:
        print('Meine Zahl ist groesser')
    elif geraten > geheimZahl:
        print('Meine Zahl ist kleiner')
    else:
        richtigeZahl = True
        #print('Super, ' + name + ', das war genau meine Zahl! Du hast sie mit ' + str(anzahlRaten) + ' Versuchen erraten!')
        print('Super, ',name,', das war genau meine Zahl! Du hast sie mit ' ,anzahlRaten, ' Versuchen erraten!')
        break # will break for correct guess
if richtigeZahl == False:
    print('Nein, die Zahl an die ich dachte war',geheimZahl,'Gut gemacht')      
#if geraten == geheimZahl:
  #  print('Super, ' + name + ', das war genau meine Zahl! Du hast sie mit ' + str(anzahlRaten) + ' Versuchen erraten!')
#else:
 #   print('Nein, die Zahl an die ich dachte war ' + str(geheimZahl)) + print('Gut gemacht')

#while approach: start with global variable T/F and set to T/F if correct
#function that returns number back. so you would say 
# maxNumberTriesInput = input()
# maxNumberTries = setMaxNumberTries()
# function checkValidWholeNumber(myNumber){
#   try:
#        checkedNumber = int(myNumber)
#        return int(checkedNumber)
#   except:
#       print("has to be whole number, try again")
#       maxNumberTriesInput = input()
#       checkValidWholeNumber(maxNumberTriesInput) 
# }