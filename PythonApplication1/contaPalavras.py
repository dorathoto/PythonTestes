arq = open('alice.txt')
texto = arq.read()
texto = texto.lower()
import string
for c in string.punctuation: #caracteres especiais
    texto = texto.replace(c, ' ')   #remove eles
texto = texto.split()

dic = {}
for p in texto:
    if p not in dic:
        dic[p] = 1
    else:
        dic[p] += 1
print ('Alice aparece %s vezes' %dic['alice'])
arq.close()