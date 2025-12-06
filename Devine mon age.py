# print sert a afficher du texte a l'utilisateur et les guillement "" servent a afficher du texte sinon on insert une variable
print("Hi my G !")
# l'instruction while sert a créer une boucle et le True lance la boucle
while True:
    # je créer une variable year au quel je demande a l'utilisateur décrire son année et le int veut dire que j'attend une valeur
    year=int(input("Give me your Year of birth "))
    print("Thank !")
    # je créer une toute nouvelle variable qui vas faire le calcul 2025 moins l'année que l'utilisateur a inserer
    age = 2025 - year
    # le f sert a inserer la fonction {age} au quel j'affiche le résultat de ma variables
    print(f"You are {age} year old !")
    # je créer une autre variable x qui va demander a l'utilisateur si il veut recommencer ou non
    x=input("Let's retry ? (O/N)")
    # je mes mon instruction dans la boucle if et je mes la variable x que l'utilisateur a entré et si il a indiquer "N" et bien cet instruction vas ce lancer
    if x=="N":
        print("Good Bye !")
        print("Adam ©")
        # break sert a mettre fin a la boucle
        break