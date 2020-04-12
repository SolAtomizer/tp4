def fibonacci (rang) :

    # Cas de départ où pour le premier élément de la série = 0
    if rang == 0 :
        return 0
    # Cas de départ où pour le deuxième élément de la série = 1
    elif rang == 1 :
        return 1
    else :
        # Appel récursif ou fibonacci (n) = fibonacci (n-1) + fibonacci (n-2)
        return fibonacci(rang - 1) + fibonacci(rang - 2)
