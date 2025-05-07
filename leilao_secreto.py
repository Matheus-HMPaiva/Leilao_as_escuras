from logo import logo 
print(logo)

print("Olá!")

lances = {}
continuar_lances = True

while continuar_lances:
    nome = input("Qual é o seu nome? ")
    valor = int(input("Qual é o seu lance? R$"))
    lances[nome] = valor

    mais_lances = input("Há mais algum participante? Digite 'sim' ou 'não':\n").lower()
    if mais_lances == "não":
        continuar_lances = False

def maior_lance(dicionario_lances):
    vencedor = ""
    maior_valor = 0
    for participante in dicionario_lances:
        valor_lance = dicionario_lances[participante]
        if valor_lance > maior_valor:
            maior_valor = valor_lance
            vencedor = participante
    print(f"O vencedor é {vencedor} com um lance de R${maior_valor}.")

# Chamar a função após finalizar os lances
maior_lance(lances)
