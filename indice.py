

leitura = open("Bolsa.csv","r")
leitura2 = open("indice.txt","w")


colunaNIS = 7 



def escolheOnis(l):
    return l[0]

linhas = []
leitura.seek(0,2)
tamanho = leitura.tell()
leitura.seek(0)
leitura.readline()
while (leitura.tell() < tamanho):
    
    i = leitura.tell()
    l = leitura.readline()
    linha_fragmentada = l.split("\t")
    nis = linha_fragmentada[7]
    
    linhas.append((nis,i))
    

linhas = sorted(linhas, key = escolheOnis)
tamanholista = len(linhas)

leitura2.seek(0)

for j in range(0,tamanholista):
    
    li = linhas[j]
    
    leitura2.write("O nis ")
    leitura2.write(li[0])
    leitura2.write(" está na posicao:")
    leitura2.write(str(li[1]))
    leitura2.write("\n")

print("pronto!")    
leitura.close()
leitura2.close()
