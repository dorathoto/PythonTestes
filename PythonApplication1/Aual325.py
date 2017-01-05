# Ler o arquivo mensagem.txt e gravar em cripto.txt trocando todas vogais por '*'
texto = open('mensagem.txt', 'r')
saida = open('cripto.txt','w')

with open('mensagem.txt') as texto:
    t = texto.read()
    print(texto.read())
    for letra in t:
        if letra.lower() in 'aeiou':
            saida.write('*')
        else:
            saida.write(letra)

#for linha in texto.readlines():
#    for letra in linha:
#        if letra.lower() in 'aeiou':
#            saida.write('*')
#        else:
#             saida.write(letra)
#texto.close()
#saida.close()