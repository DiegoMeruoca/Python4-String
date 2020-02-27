# Exemplo 2 - Converter Maiuscula e Minuscula
S = "O Rato roeu a roupa do Rei de Roma"   # cria a String
S = S.lower()  # Converte os caracteres da String para minúsculos e a sobrescreve
print(S)
S = S.upper()  # Converte os caracteres da String para maiúsculos e a sobrescreve
print(S)
S = S.title()  # Converte cada primeira letra em maiusculo
print(S)
S = S.capitalize()  # Converte só a primeira letra em maiusculo
print(S)
S = "SIM"  # Atribui SIM a S
print(S == "sim")  # Retorna False, pois SIM é diferente de sim
print(S == "sim".upper())  # Retorna True, pois SIM é igual SIM
