print("""
    Encuentra la tecla secreta
      por cada vez que aciertes ganaras 10 puntos
      llega a los 100 para ganar aunque...
      nunca sabras si has acertado""")
gameover = False
win = False
points = 0
while not gameover:
    key = input("Key? ")
    if key == " ":
        points = points + 10
    
    if key == "w":
        gameover = True
    
    if points >= 100:
        gameover = True
        win = True    


if win :
    print('Ganaste!')
else:
    print('Bye bye loserrrr!')    