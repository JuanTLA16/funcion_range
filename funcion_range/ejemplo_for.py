
frase = input("Digite una frase: ")
vocales = "aeiouAEIOU"
numero_vocales = 0
for i in frase:
    if i in vocales:
        numero_vocales = numero_vocales + 1
print("En la frase hay " + str(numero_vocales) + " vocales")