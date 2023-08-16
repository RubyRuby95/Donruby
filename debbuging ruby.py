def suma_10(lista1: list = [2,4,7], lista2: list = [1,5,3]) -> str:

    lista_final=[]
    for i in lista1:
        for j in lista2:
            lista_final.append(i)
            lista_final.append(j)
        lista_final.append(i)     
    print(lista_final)
    lista_final = []       

          
    if (lista_final[0]+lista_final[1]+lista_final[2] == 10):
        print('1')
    else:
        print('0')

def main():
    
    return suma_10()

if __name__ == "__main__":
    main()