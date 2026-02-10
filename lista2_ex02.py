def palavra_ou_frase():
  frase = input("Digite uma frase: ")
  quant_caracteres = len(frase)
  primeira_letra = frase[0]
  ultima_letra = frase[-1]
  string_invertida = frase[::-1]
  return frase, quant_caracteres, primeira_letra, ultima_letra, string_invertida

frase, quant_caracteres, primeira_letra, ultima_letra, string_invertida = palavra_ou_frase()
print(f"{quant_caracteres} \n{primeira_letra} \n{ultima_letra} \n{string_invertida}")