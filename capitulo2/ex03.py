def comparar():
  string1 = input("Escreva True ou False: ").lower()
  string2 = input("Escreva True ou False: ").lower()
  if string1 == string2:
    print("São iguais")
  else:
    print("São diferentes")
  return string1, string2

a, b = comparar()
