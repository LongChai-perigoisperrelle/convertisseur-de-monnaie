from forex_python.converter import CurrencyRates 


def convertir_monnaie(somme, unitesource, unitefinale):
    c = CurrencyRates()
    
    result = c.convert(unitesource, unitefinale, somme)

    return result



somme = int(input("Somme a convertir : "))
unitesource = input("Monnaie d'origine : ").upper()
unitefinale = input("Monnaie à échanger : ").upper()

resultat = convertir_monnaie(somme, unitesource, unitefinale)

print(resultat)