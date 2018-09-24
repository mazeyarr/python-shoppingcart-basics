# -*- coding: UTF-8 -*-
import sys


def main(argv):
    # intro()
    producten = maakProducten()

    product4 = {
        'Artikelnummer': 4,
        'Artikelnaam': 'Druiven pitloos wit',
        'Schap': 'Fruit',
        'Prijs': 1.99,
        'Amount': 1
    }
    product5 = {
        'Artikelnummer': 5,
        'Artikelnaam': 'Broccoli',
        'Schap': 'Groente',
        'Prijs': 0.89,
        'Amount': 1
    }

    producten = voegProductToe(producten, product4)
    producten = voegProductToe(producten, product5)

    producten = verhoogPrijs(producten, 3, 23)

    schappen = berekenTotaalPrijsPerSchap(producten)

    for product in producten:
        print("Artikelnummer: " + str(product.get('Artikelnummer')) + " | " + product.get('Artikelnaam') + " | " + "€"+str(product.get('Prijs')).replace('.', ','))

    print('-----------')
    print('Prijs Per Schap:')

    for schap, prijs in schappen.items():
        print(schap + ': ' + '€' + str(prijs))


    mijnBoodschappenlijst = []
    while(True):
        print('Uw Boodschappen:')
        print('----------------------')
        for productId in mijnBoodschappenlijst:
            product = vindProduct(producten, 'Artikelnummer', productId)
            print(product.get('Artikelnaam') + ' | ' + 'Prijs: ' + '€' + str(product.get('Prijs')))
        print('€' + str(berekenMijnBoodschappenTotaal(producten, mijnBoodschappenlijst)))
        print('----------------------')

        newItem = cInput('Wat \'Artikelnummer\' moet erbij?')
        if newItem == '':
            cInput('Wat \'Artikelnummer\' moet erbij?')
        else:
            newItem = vindProduct(producten, 'Artikelnummer', int(newItem))


        if(newItem):
            plaatsOpMijnBoodschappenlijst(mijnBoodschappenlijst, newItem)
        else:
            print('----------------------')
            print('Product bestaat niet!')
            print('----------------------')
    pass

def intro():
    naam = cInput('Wat is je naam?')
    klas = cInput('In welke klas zit je?')
    print('Welkom, ' + naam + 'van klas \'' + klas +'\'')

def maakProducten():
    product1 = {
        'Artikelnummer': 1,
        'Artikelnaam': 'Komkommer',
        'Schap': 'Groente',
        'Prijs': 0.95,
    }
    product2 = {
        'Artikelnummer': 2,
        'Artikelnaam': 'Tandpasta',
        'Schap': 'Drogisterij',
        'Prijs': 2.99,
    }
    product3 = {
        'Artikelnummer': 3,
        'Artikelnaam': 'Ei',
        'Schap': 'Zuivel',
        'Prijs': 0.30,
    }
    producten = [product1, product2, product3]
    return producten

def voegProductToe(producten, newProduct):
    producten.append(newProduct)
    return producten

def verhoogPrijs(producten, id, percentage):
    for product in producten:
        if(product.get('Artikelnummer')== id):
            product['Prijs'] = round((product.get('Prijs') / 100) * (100 + percentage), 2)
    return producten

def berekenTotaalPrijsPerSchap(producten):
    schappen = {}
    for product in producten:
        schap = product.get('Schap')
        if schap in schappen.keys():
            schappen[product.get('Schap')] += round(product.get('Prijs'))
        else:
            schappen[schap] = product.get('Prijs')
    return schappen

def vindProduct(producten, key, zoekQuery):
    resultaat = False
    for product in producten:
        if product.get(key) == zoekQuery:
            resultaat = product
    return resultaat

def plaatsOpMijnBoodschappenlijst(lijst, keuze):
    lijst.append(keuze.get('Artikelnummer'))

def berekenMijnBoodschappenTotaal(producten, gebruikerLijst):
    totaal = 0.00
    for productId in gebruikerLijst:
        totaal += vindProduct(producten, 'Artikelnummer', productId).get('Prijs')
    return round(totaal, 2)

def cInput(inputText):
    userInput = input(inputText).strip()

    if userInput == 'exit':
        exit(0)
    elif userInput == '':
        print('U heeft een incorrect input gegeven')

    return userInput
if __name__ == '__main__':
    main(sys.argv)
