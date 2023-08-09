def main():

    pali = str(input("ingrese un palindromo: "))
    if(pali[::-1]==pali):
        print("es un palindromo")
    else:
        print("no es un palindromo")



if __name__ == '__main__':
    main()