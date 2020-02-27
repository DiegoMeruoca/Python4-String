S = "Alo Mundo"  # cria a String
print(S)  # Imprim a String
print(S[0])  # Imprime só o A, referente aposição 0 assim como numa lista
# S[0]="a"-> se tentar mudar o conteúdo da String como na lista,
#  retorna erro,pois não é possivel
L = list(S)  # transforma cada caractee da String em um elemento da lista
print(L)  # Imprime a lista
L[0] = "a"  # Na lista podemos alterar o conteúdo, diferentementeda String
print(L)
S = "".join(L)  # Tranasforma os elementos dalista em uma String
print(S)
