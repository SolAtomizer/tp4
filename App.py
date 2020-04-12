hauteur = 10
i = 0

while i < hauteur:
    nbX = int((hauteur - i)/2)
    nbY = (hauteur - i)%2

    j=0
    while j < nbX:
        print('X', end="", flush=True)
        j = j+1

    j=0
    while j < nbY:
        print('Y', end="", flush=True)
        j = j+1

    j=0
    while j < nbX:
        print('X', end="", flush=True)
        j = j+1

    i = i+1
    print("\r")

