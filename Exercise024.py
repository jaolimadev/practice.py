# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

CityName = input("Input City Name: ")

if "joão","lucas","mateus","santos","santo","são" in CityName.lower():
    print("This Brazilian city does have a religious name.") 
else: 
    print("This Brazilian city does NOT have a religious name.")