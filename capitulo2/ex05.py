def lista_frutas():
    frutas = []

    for i in range(5):
        fruta = input()
        frutas.append(fruta)

    return frutas

frutas = lista_frutas()
print("Lista de frutas:", frutas)