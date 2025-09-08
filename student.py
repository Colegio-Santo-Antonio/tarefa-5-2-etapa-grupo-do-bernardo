# Leia uma linha com o número do cartão
numero = input()

# Remove espaços (caso existam)
numero = numero.replace(" ", "")

# Convertemos para uma lista de inteiros
digitos = [int(d) for d in numero]

# Começamos da direita (posição -1), então invertemos para facilitar
digitos = digitos[::-1]

soma = 0

for i, d in enumerate(digitos):
    if i % 2 == 1:  # cada segundo dígito (começando do penúltimo)
        d = d * 2
        if d > 9:
            d -= 9
    soma += d

# Verificamos se a soma é divisível por 10
if soma % 10 == 0:
    print("Cartão válido")
else:
    print("Cartão inválido")
  
