def table_verite(fonction, variables):
    nb_variables = len(variables)
    print("Table de vérité de la fonction", fonction)
    print(" " + " | ".join(variables) + " | " + fonction)
    print("-" * (nb_variables * 3 + len(fonction) + 3))
    for i in range(2 ** nb_variables):
        valeurs = [int(b) for b in format(i, '0' + str(nb_variables) + 'b')]
        valeurs_texte = [str(v) for v in valeurs]
        resultat = int(eval(fonction, dict(zip(variables, valeurs))))
        print(" " + " | ".join(valeurs_texte) + " | " + str(resultat))

fonction_logique = input("Entrez la fonction logique (utilisez les opérateurs logiques:and, or): ")
variables = input("Entrez les variables séparées par des espaces: ").split()

table_verite(fonction_logique, variables)

def premiere_forme_canonique(fonction):
    forme = []
    for i, char in enumerate(fonction):
        if char == '1':
            forme.append(f"X{i+1}")
        elif char == '0':
            forme.append(f"~X{i+1}")
    return " ∧ ".join(forme)

def deuxieme_forme_canonique(fonction):
    forme = []
    for i, char in enumerate(fonction):
        if char == '0':
            forme.append(f"X{i+1}")
        elif char == '1':
            forme.append(f"~X{i+1}")
    return " ∨ ".join(forme)

fonction_logique = input("Entrez la fonction logique (sous forme de 0 et 1")

print("Première forme canonique:", premiere_forme_canonique(fonction_logique))
print("Deuxième forme canonique:", deuxieme_forme_canonique(fonction_logique))