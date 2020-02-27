# Para não termos problemas com maiúsculas e minúsculas na hora de comparar
S = "João comprou um carro"
print("joão" in S.lower())
# Compara se joão(Minúsculo) esta em S convertida em minúsculo, neste caso True
print("CARRO" in S.upper())
# Compara se CARRO(Maiúsculo) esta em S convertida em maiúsculo, neste caso True
print("comprou" not in S.lower())
# Compara se comprou(Minúsculo) não esta em S convertida em minúsculo, neste caso False

